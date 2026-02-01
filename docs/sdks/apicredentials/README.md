# ApiCredentials

## Overview

Operations related to API credentials

### Available Operations

* [list](#list) - List API credentials for an Organization

## list

Retrieve all API credentials for the specified Organization.

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

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `organization_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The <code>id</code> of the Organization that owns the API credentials. |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.V1APICredentialsListAPICredentialsResponse](../../models/v1apicredentialslistapicredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |