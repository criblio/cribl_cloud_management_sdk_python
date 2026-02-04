# ApiCredentials

## Overview

Operations related to API credentials

### Available Operations

* [list](#list) - List API Credentials for an Organization
* [create](#create) - Create an API Credential
* [update](#update) - Update an API Credential
* [delete](#delete) - Delete an API Credential
* [get](#get) - Get an API Credential

## list

Get a list of all API Credentials for the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.apiCredentials.listApiCredentials" method="get" path="/v1/organizations/{organizationId}/api-credentials" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane(
    security=models.Security(
        client_oauth=models.SchemeClientOauth(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://api.cribl.cloud",
        ),
    ),
) as cmp_client:

    res = cmp_client.api_credentials.list(organization_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `organization_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | The <code>id</code> of the Organization whose API Credentials you want to list. |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.V1APICredentialsListAPICredentialsResponse](../../models/v1apicredentialslistapicredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a new API Credential for the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.apiCredentials.createApiCredential" method="post" path="/v1/organizations/{organizationId}/api-credentials" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane(
    security=models.Security(
        client_oauth=models.SchemeClientOauth(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://api.cribl.cloud",
        ),
    ),
) as cmp_client:

    res = cmp_client.api_credentials.create(organization_id="<id>", name="Auto-Manage-Workspaces", description="Used for automated Workspace management", enabled=True, workspace_id="main", roles={
        "organization_role": models.OrganizationRole.ADMIN,
        "workspaces": [
            {
                "workspace_id": "main",
                "workspace_role": models.WorkspaceRole.ADMIN,
                "products": [
                    {
                        "product": models.Product.STREAM,
                        "role": models.Role.ADMIN,
                    },
                ],
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `organization_id`                                                                    | *str*                                                                                | :heavy_check_mark:                                                                   | The <code>id</code> of the Organization where you want to create the API Credential. |                                                                                      |
| `name`                                                                               | *str*                                                                                | :heavy_check_mark:                                                                   | Human-readable name of the API Credential.                                           | Auto-Manage-Workspaces                                                               |
| `description`                                                                        | *str*                                                                                | :heavy_check_mark:                                                                   | Brief description of the purpose and usage for the API Credential.                   | Used for automated Workspace management                                              |
| `enabled`                                                                            | *bool*                                                                               | :heavy_check_mark:                                                                   | If <code>true</code>, the API Credential is enabled. Otherwise, <code>false</code>.  | true                                                                                 |
| `workspace_id`                                                                       | *str*                                                                                | :heavy_check_mark:                                                                   | Unique ID of the Workspace.                                                          | main                                                                                 |
| `roles`                                                                              | [models.APICredentialRolesSchema](../../models/apicredentialrolesschema.md)          | :heavy_check_mark:                                                                   | Role assignments for the API Credential.                                             |                                                                                      |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |                                                                                      |

### Response

**[models.V1APICredentialsCreateAPICredentialResponse](../../models/v1apicredentialscreateapicredentialresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update the specified API Credential.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.apiCredentials.updateApiCredential" method="patch" path="/v1/organizations/{organizationId}/api-credentials/{apiCredentialId}" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane(
    security=models.Security(
        client_oauth=models.SchemeClientOauth(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://api.cribl.cloud",
        ),
    ),
) as cmp_client:

    res = cmp_client.api_credentials.update(organization_id="<id>", api_credential_id="<id>", name="Auto-Manage-Workspaces", description="Used for automated Workspace management", enabled=True, roles={
        "organization_role": models.OrganizationRole.ADMIN,
        "workspaces": [
            {
                "workspace_id": "main",
                "workspace_role": models.WorkspaceRole.ADMIN,
                "products": [
                    {
                        "product": models.Product.STREAM,
                        "role": models.Role.ADMIN,
                    },
                ],
            },
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `organization_id`                                                                     | *str*                                                                                 | :heavy_check_mark:                                                                    | The <code>id</code> of the Organization whose API Credential you want to update.      |                                                                                       |
| `api_credential_id`                                                                   | *str*                                                                                 | :heavy_check_mark:                                                                    | The <code>clientId</code> of the API Credential to update.                            |                                                                                       |
| `name`                                                                                | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Human-readable name of the API Credential.                                            | Auto-Manage-Workspaces                                                                |
| `description`                                                                         | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Brief description of the purpose and usage for the API Credential.                    | Used for automated Workspace management                                               |
| `enabled`                                                                             | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | If <code>true</code>, the API Credential is enabled. Otherwise, <code>false</code>.   | true                                                                                  |
| `roles`                                                                               | [Optional[models.APICredentialRolesSchema]](../../models/apicredentialrolesschema.md) | :heavy_minus_sign:                                                                    | Role assignments for the API Credential.                                              |                                                                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.DefaultErrorDTO](../../models/defaulterrordto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete the specified API Credential.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.apiCredentials.deleteApiCredential" method="delete" path="/v1/organizations/{organizationId}/api-credentials/{apiCredentialId}" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane(
    security=models.Security(
        client_oauth=models.SchemeClientOauth(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://api.cribl.cloud",
        ),
    ),
) as cmp_client:

    res = cmp_client.api_credentials.delete(organization_id="<id>", api_credential_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `organization_id`                                                                | *str*                                                                            | :heavy_check_mark:                                                               | The <code>id</code> of the Organization whose API Credential you want to delete. |
| `api_credential_id`                                                              | *str*                                                                            | :heavy_check_mark:                                                               | The <code>clientId</code> of the API Credential to delete.                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[models.DefaultErrorDTO](../../models/defaulterrordto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Get the specified API Credential.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.apiCredentials.getApiCredential" method="get" path="/v1/organizations/{organizationId}/api-credentials/{apiCredentialId}" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane(
    security=models.Security(
        client_oauth=models.SchemeClientOauth(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://api.cribl.cloud",
        ),
    ),
) as cmp_client:

    res = cmp_client.api_credentials.get(organization_id="<id>", api_credential_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `organization_id`                                                                  | *str*                                                                              | :heavy_check_mark:                                                                 | The <code>id</code> of the Organization whose API Credential you want to retrieve. |
| `api_credential_id`                                                                | *str*                                                                              | :heavy_check_mark:                                                                 | The <code>clientId</code> of the API Credential to retrieve.                       |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[models.V1APICredentialsGetAPICredentialResponse](../../models/v1apicredentialsgetapicredentialresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |