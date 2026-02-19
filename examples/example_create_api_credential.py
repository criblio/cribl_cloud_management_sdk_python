"""
Cribl.Cloud Example for Creating a New API Credential

This example demonstrates how to create a new API Credential with specific
Role assignments.

1. Create an authenticated SDK client with OAuth2 credentials.
2. Call api_credentials.create with User Role on the Organization, Member
   Role on the Workspace, and Editor Role on Cribl Stream, Cribl Edge, 
   Cribl Search, and Cribl Lake.
3. Print the details for the created API Credential.

Prerequisites: To use this example, you must first create at least one 
API Credential directly in the Cribl UI. This is necessary because you 
need the CLIENT_ID and CLIENT_SECRET for an existing API Credential to 
create an authenticated SDK client to make this request. Replace the 
placeholder values for CLIENT_ID and CLIENT_SECRET with the correct 
values for an existing API Credential.

See https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud.
Your Client ID and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud only.
"""

from cribl_mgmt_plane import CriblMgmtPlane, models


# Cribl.Cloud configuration: Replace the placeholder values
CLIENT_ID = "your-client-id"  # Replace with your OAuth2 Client ID
CLIENT_SECRET = "your-client-secret"  # Replace with your OAuth2 Client Secret
ORG_ID = "your-org-id"  # Replace with your Organization ID
WORKSPACE_ID = "main"  # Replace with your Workspace ID

# Token URL and audience for Cribl.Cloud OAuth2
TOKEN_URL = "https://login.cribl.cloud/oauth/token"
AUDIENCE = "https://api.cribl.cloud"


def main():
    # Create authenticated SDK client with OAuth2
    with CriblMgmtPlane(
        security=models.Security(
            client_oauth=models.SchemeClientOauth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                token_url=TOKEN_URL,
                audience=AUDIENCE,
            ),
        ),
    ) as cmp_client:

        # Create API Credential with the roles User (Organization), Member (Workspace), and Editor (Cribl Stream/Edge/Search/Lake)
        res = cmp_client.api_credentials.create(
            organization_id=ORG_ID,
            name="Example credential (User/Member/Editor/User)",
            description="User on Organization; Member on Workspace; Editor on Cribl Stream, Cribl Edge, Cribl Search, and Cribl Lake",
            enabled=True,
            workspace_id=WORKSPACE_ID,
            roles={
                "organization_role": models.OrganizationRole.USER,
                "workspaces": [
                    {
                        "workspace_id": WORKSPACE_ID,
                        "workspace_role": models.WorkspaceRole.USER,  # Member
                        "products": [
                            {"product": models.Product.STREAM, "role": models.Role.EDITOR},
                            {"product": models.Product.EDGE, "role": models.Role.EDITOR},
                            {"product": models.Product.SEARCH, "role": models.Role.EDITOR},
                            {"product": models.Product.LAKE, "role": models.Role.EDITOR},
                        ],
                    },
                ],
            },
        )

        # Handle response
        if isinstance(res, models.APICredentialResponseSchema):
            print(f"Created: {res.name} (client_id: {res.client_id})")
        else:
            print(res)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        STATUS_CODE = getattr(error, "status_code", None)
        if STATUS_CODE == 401:
            print("Authentication failed! Check your CLIENT_ID and CLIENT_SECRET.")
        elif STATUS_CODE == 429:
            print("Rate limit reached. Try again in a few seconds.")
        else:
            print(f"Something went wrong: {error}")
