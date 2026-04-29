"""
Cribl.Cloud Authentication Example

This example demonstrates how to configure authentication on Cribl.Cloud 
using OAuth2 credentials.

1. Create an SDK client with OAuth2 client credentials using the 
client_oauth security scheme.
2. Automatically handle token exchange and refresh.
3. Validate the connection by checking health status and listing Workspaces.
 
Prerequisites: Replace the placeholder values for ORG_ID, CLIENT_ID, and 
CLIENT_SECRET with your Organization ID and Client ID and Secret.  
To get your Client ID and Secret, follow the steps at 
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud. 
Your Client ID and Secret are sensitive information and should be kept private.

NOTE: This example is for Cribl.Cloud only. 
It does not require .env file configuration.
"""

import asyncio
from cribl_mgmt_plane import CriblMgmtPlane, errors, models


# Cribl.Cloud configuration: Replace the placeholder values
CLIENT_ID = "your-client-id"  # Replace with your OAuth2 Client ID
CLIENT_SECRET = "your-client-secret"  # Replace with your OAuth2 Client Secret
ORG_ID = "your-org-id"  # Replace with your Organization ID

# Token URL and audience for Cribl.Cloud OAuth2
TOKEN_URL = "https://login.cribl.cloud/oauth/token"
AUDIENCE = "https://api.cribl.cloud"


async def main():
    # Create authenticated SDK client with OAuth2
    client_oauth = models.SchemeClientOauth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_url=TOKEN_URL,
        audience=AUDIENCE,
    )

    security = models.Security(client_oauth=client_oauth)
    
    async with CriblMgmtPlane(security=security) as cmp_client:
        try:
            print("✅ Cribl.Cloud Management Plane SDK client created")

            # Validate connection with health check
            health_response = await cmp_client.health.get_async()
            status = health_response.status or "unknown"  # type: ignore
            print(f"✅ Health check passed! Status: {status}")

            # List all Workspaces for the Organization
            workspaces_response = await cmp_client.workspaces.list_async(
                organization_id=ORG_ID
            )
            items = workspaces_response.items  # type: ignore
            count = workspaces_response.count  # type: ignore

            message = f"✅ Client works! Found {count} Workspace(s):" if items else f"✅ Client works! No Workspaces found for Organization {ORG_ID}"
            print(message)

            for ws in items:
                alias_display = f" ({ws.alias})" if ws.alias else ""
                print(f"  • {ws.workspace_id}{alias_display} - {ws.state.value} in {ws.region.value}")

        except errors.CriblMgmtPlaneError as e:
            if e.status_code == 401:
                print("⚠️ Authentication failed! Check your CLIENT_ID and CLIENT_SECRET.")
            elif e.status_code == 429:
                print("⚠️ Uh oh, you've reached the rate limit! Try again in a few seconds.")
            else:
                print(f"❌ Something went wrong: {e.message}")


if __name__ == "__main__":
    asyncio.run(main())
