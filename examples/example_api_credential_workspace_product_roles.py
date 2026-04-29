"""
Create a Cribl.Cloud API Credential Example (Organization and Workspace User, Product Editor)

This example demonstrates how to create a new API Credential with the User Role on
an Organization and a Workspace, and the Editor Role on all Products.

1. Create an SDK client with OAuth2 client credentials using the client_oauth security scheme.
2. Create a new API Credential with:
   - User Role on the Organization and the `main` Workspace.
   - Editor on all Cribl products in the `main` Workspace.
   - An optional IP allowlist to restrict API access for the API Credential to the specified IPv4 CIDR range.

Use the returned client_id and client_secret for the new API Credential in subsequent
requests. The client_secret is only returned on create.

Prerequisites: Replace the placeholder values for ORG_ID, CLIENT_ID, and CLIENT_SECRET with
your Organization ID and the Client ID and Secret for an existing API Credential. You need
these values for an existing API Credential to authenticate this script.

To get the Client ID and Secret for an existing API Credential, follow the steps at
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud.

To use the new API Credential for later SDK calls, you need its client_id and client_secret.
When create succeeds, the object returned from api_credentials.create(...) includes client_id,
client_secret, name, and the other APICredentialCreateResponseSchema fields. Read the new
client_secret as response.client_secret on that same object. The API returns client_secret
only in the create response (not in GET responses). Do not print or log the client_secret. 
Pass the client_id and client_secret for the new API Credential into client_oauth when you 
construct the CriblMgmtPlane client for later SDK calls.

Client Secrets are sensitive information and should be kept private.
"""

from cribl_mgmt_plane import CriblMgmtPlane, errors, models

# Cribl.Cloud configuration: Replace the placeholder values
CLIENT_ID = "your-client-id"  # Replace with the OAuth2 Client ID for an existing API Credential
CLIENT_SECRET = "your-client-secret"  # Replace with the OAuth2 Client Secret for an existing API Credential
ORG_ID = "your-org-id"  # Replace with the Organization ID

# Token URL and audience for Cribl.Cloud OAuth2
TOKEN_URL = "https://login.cribl.cloud/oauth/token"
AUDIENCE = "https://api.cribl.cloud"

IP_ALLOWLIST = ["203.0.113.0/24"]  # Replace with your IPv4 CIDR range.

# All product identifiers exposed by this SDK for workspace-scoped roles.
ALL_CRIBL_PRODUCTS = (
    models.Product.STREAM,
    models.Product.SEARCH,
    models.Product.LAKE,
    models.Product.EDGE,
)


def main():
    main_workspace_editor_products = [
        models.ProductRoleSchema(product=product, role=models.Role.EDITOR)
        for product in ALL_CRIBL_PRODUCTS
    ]

    roles = models.APICredentialRolesSchema(
        organization_role=models.OrganizationRole.USER,
        workspaces=[
            models.WorkspaceRoleSchema(
                workspace_id="main",
                workspace_role=models.WorkspaceRole.USER,
                products=main_workspace_editor_products,
            ),
        ],
    )

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
        try:
            response = cmp_client.api_credentials.create(
                organization_id=ORG_ID,
                name="Product-Editor",
                description="Editor Role on all Cribl Products",
                enabled=True,
                roles=roles,
                ip_allowlist=IP_ALLOWLIST,
            )
            print(
                "✅ Created API Credential "
                f"name={response.name!r} client_id={response.client_id!r}"  # type: ignore
            )

        except errors.CriblMgmtPlaneError as e:
            if e.status_code == 401:
                print("⚠️ Authentication failed! Check your CLIENT_ID and CLIENT_SECRET.")
            elif e.status_code == 429:
                print("⚠️ Uh oh, you've reached the rate limit! Try again in a few seconds.")
            else:
                print(f"❌ Something went wrong: {e.message}")


if __name__ == "__main__":
    main()
