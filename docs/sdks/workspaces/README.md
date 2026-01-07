# Workspaces

## Overview

Operations related to Workspaces

### Available Operations

* [create](#create) - Create a Workspace in the specified Organization
* [list](#list) - List all Workspaces for the specified Organization
* [update](#update) - Update a Workspace
* [delete](#delete) - Delete a Workspace
* [get](#get) - Get a Workspace

## create

Create a new Workspace in the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.createWorkspace" method="post" path="/v1/organizations/{organizationId}/workspaces" -->
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

    res = cmp_client.workspaces.create(organization_id="<id>", workspace_id="main", alias="Production Environment", description="Main production workspace for customer data processing", tags=[
        "production",
        "customer-data",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `organization_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | The <code>id</code> of the Organization where you want to create the Workspace. |                                                                                 |
| `workspace_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | Unique identifier for the workspace                                             | main                                                                            |
| `alias`                                                                         | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | User-friendly alias for the workspace                                           | Production Environment                                                          |
| `description`                                                                   | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Detailed description of the workspace                                           | Main production workspace for customer data processing                          |
| `tags`                                                                          | List[*str*]                                                                     | :heavy_minus_sign:                                                              | Tags associated with the workspace                                              | [<br/>"production",<br/>"customer-data"<br/>]                                   |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.V1WorkspacesCreateWorkspaceResponse](../../models/v1workspacescreateworkspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list

Get a list of all Workspaces for the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.listWorkspaces" method="get" path="/v1/organizations/{organizationId}/workspaces" -->
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

    res = cmp_client.workspaces.list(organization_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `organization_id`                                                     | *str*                                                                 | :heavy_check_mark:                                                    | The <code>id</code> of the Organization that contains the Workspaces. |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.V1WorkspacesListWorkspacesResponse](../../models/v1workspaceslistworkspacesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update the specified Workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.updateWorkspace" method="patch" path="/v1/organizations/{organizationId}/workspaces/{workspaceId}" -->
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

    res = cmp_client.workspaces.update(organization_id="<id>", workspace_id="<id>", alias="Production Environment", description="Main production workspace for customer data processing", tags=[
        "production",
        "customer-data",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization that contains the Workspace. |                                                                      |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Workspace to update.                      |                                                                      |
| `alias`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | User-friendly alias for the workspace                                | Production Environment                                               |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Detailed description of the workspace                                | Main production workspace for customer data processing               |
| `tags`                                                               | List[*str*]                                                          | :heavy_minus_sign:                                                   | Tags associated with the workspace                                   | [<br/>"production",<br/>"customer-data"<br/>]                        |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.DefaultErrorDTO](../../models/defaulterrordto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete the specified Workspace in the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.deleteWorkspace" method="delete" path="/v1/organizations/{organizationId}/workspaces/{workspaceId}" -->
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

    res = cmp_client.workspaces.delete(organization_id="<id>", workspace_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization that contains the Workspace. |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Workspace to delete.                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.DefaultErrorDTO](../../models/defaulterrordto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Get the specified Workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.workspaces.getWorkspace" method="get" path="/v1/organizations/{organizationId}/workspaces/{workspaceId}" -->
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

    res = cmp_client.workspaces.get(organization_id="<id>", workspace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization that contains the Workspace. |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Workspace to get.                         |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.V1WorkspacesGetWorkspaceResponse](../../models/v1workspacesgetworkspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |