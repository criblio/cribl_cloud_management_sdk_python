"""
Create a Cribl.Cloud API Credential Example (Organization Admin)

This example demonstrates how to create a new API Credential with the Admin Role on
an Organization. The Admin Role is effective across the Organization, including
all Workspaces and all products (no Workspace or product matrix is required).

1. Create an SDK client with OAuth2 client credentials using the client_oauth security scheme.
2. Create a new API Credential with Organization-level Admin and an optional IP allowlist 
   to restrict API access for the API Credential to the specified IPv4 CIDR range.

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
        try:
            response = cmp_client.api_credentials.create(
                organization_id=ORG_ID,
                name="Auto-Manage-WorkspacesAuto-Manage-Workspaces",
                description="Used for automated Workspace management",
                enabled=True,
                roles={"organization_role": models.OrganizationRole.ADMIN},
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
