# Workspaces
(*workspaces*)

## Overview

### Available Operations

* [v1_workspaces_create_workspace](#v1_workspaces_create_workspace) - Create a new workspace
* [v1_workspaces_list_workspaces](#v1_workspaces_list_workspaces) - List all workspaces for an organization
* [v1_workspaces_update_workspace](#v1_workspaces_update_workspace) - Update an existing workspace
* [v1_workspaces_delete_workspace](#v1_workspaces_delete_workspace) - Delete a workspace
* [v1_workspaces_get_workspace](#v1_workspaces_get_workspace) - Get a specific workspace by ID

## v1_workspaces_create_workspace

Create a new workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.createWorkspace" method="post" path="/v1/organizations/{organizationId}/workspaces" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane() as cmp_client:

    res = cmp_client.workspaces.v1_workspaces_create_workspace(security=models.V1WorkspacesCreateWorkspaceSecurity(
        oauth2=models.SchemeOauth2(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://publicapi.cribl.cloud",
        ),
    ), organization_id="<id>", workspace_id="main", region=models.WorkspaceCreateRequestDTORegion.US_WEST_2, alias="Production Environment", description="Main production workspace for customer data processing", tags=[
        "production",
        "customer-data",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.V1WorkspacesCreateWorkspaceSecurity](../../models/v1workspacescreateworkspacesecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `organization_id`                                                                                 | *str*                                                                                             | :heavy_check_mark:                                                                                | Organization identifier                                                                           |                                                                                                   |
| `workspace_id`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | Unique identifier for the workspace                                                               | main                                                                                              |
| `region`                                                                                          | [models.WorkspaceCreateRequestDTORegion](../../models/workspacecreaterequestdtoregion.md)         | :heavy_check_mark:                                                                                | AWS region where the workspace is deployed                                                        | us-west-2                                                                                         |
| `alias`                                                                                           | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | User-friendly alias for the workspace                                                             | Production Environment                                                                            |
| `description`                                                                                     | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Detailed description of the workspace                                                             | Main production workspace for customer data processing                                            |
| `tags`                                                                                            | List[*str*]                                                                                       | :heavy_minus_sign:                                                                                | Tags associated with the workspace                                                                | [<br/>"production",<br/>"customer-data"<br/>]                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.WorkspaceSchema](../../models/workspaceschema.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## v1_workspaces_list_workspaces

List all workspaces for an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.listWorkspaces" method="get" path="/v1/organizations/{organizationId}/workspaces" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane() as cmp_client:

    res = cmp_client.workspaces.v1_workspaces_list_workspaces(security=models.V1WorkspacesListWorkspacesSecurity(
        oauth2=models.SchemeOauth2(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://publicapi.cribl.cloud",
        ),
    ), organization_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.V1WorkspacesListWorkspacesSecurity](../../models/v1workspaceslistworkspacessecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `organization_id`                                                                               | *str*                                                                                           | :heavy_check_mark:                                                                              | Organization identifier                                                                         |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.WorkspacesListResponseDTO](../../models/workspaceslistresponsedto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## v1_workspaces_update_workspace

Update an existing workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.updateWorkspace" method="patch" path="/v1/organizations/{organizationId}/workspaces/{workspaceId}" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane() as cmp_client:

    res = cmp_client.workspaces.v1_workspaces_update_workspace(security=models.V1WorkspacesUpdateWorkspaceSecurity(
        oauth2=models.SchemeOauth2(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://publicapi.cribl.cloud",
        ),
    ), organization_id="<id>", workspace_id="<id>", alias="Production Environment", description="Main production workspace for customer data processing", tags=[
        "production",
        "customer-data",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.V1WorkspacesUpdateWorkspaceSecurity](../../models/v1workspacesupdateworkspacesecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `organization_id`                                                                                 | *str*                                                                                             | :heavy_check_mark:                                                                                | Organization identifier                                                                           |                                                                                                   |
| `workspace_id`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | Workspace identifier                                                                              |                                                                                                   |
| `alias`                                                                                           | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | User-friendly alias for the workspace                                                             | Production Environment                                                                            |
| `description`                                                                                     | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Detailed description of the workspace                                                             | Main production workspace for customer data processing                                            |
| `tags`                                                                                            | List[*str*]                                                                                       | :heavy_minus_sign:                                                                                | Tags associated with the workspace                                                                | [<br/>"production",<br/>"customer-data"<br/>]                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.WorkspaceSchema](../../models/workspaceschema.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## v1_workspaces_delete_workspace

Delete a workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.deleteWorkspace" method="delete" path="/v1/organizations/{organizationId}/workspaces/{workspaceId}" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane() as cmp_client:

    cmp_client.workspaces.v1_workspaces_delete_workspace(security=models.V1WorkspacesDeleteWorkspaceSecurity(
        oauth2=models.SchemeOauth2(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://publicapi.cribl.cloud",
        ),
    ), organization_id="<id>", workspace_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.V1WorkspacesDeleteWorkspaceSecurity](../../models/v1workspacesdeleteworkspacesecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `organization_id`                                                                                 | *str*                                                                                             | :heavy_check_mark:                                                                                | Organization identifier                                                                           |
| `workspace_id`                                                                                    | *str*                                                                                             | :heavy_check_mark:                                                                                | Workspace identifier                                                                              |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## v1_workspaces_get_workspace

Get a specific workspace by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.getWorkspace" method="get" path="/v1/organizations/{organizationId}/workspaces/{workspaceId}" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane() as cmp_client:

    res = cmp_client.workspaces.v1_workspaces_get_workspace(security=models.V1WorkspacesGetWorkspaceSecurity(
        oauth2=models.SchemeOauth2(
            client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
            client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
            token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
            audience="https://publicapi.cribl.cloud",
        ),
    ), organization_id="<id>", workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.V1WorkspacesGetWorkspaceSecurity](../../models/v1workspacesgetworkspacesecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `organization_id`                                                                           | *str*                                                                                       | :heavy_check_mark:                                                                          | Organization identifier                                                                     |
| `workspace_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | Workspace identifier                                                                        |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.WorkspaceSchema](../../models/workspaceschema.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |