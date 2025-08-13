# Health
(*health*)

## Overview

### Available Operations

* [get](#get) - Get the health status of the application

## get

Get the health status of the application

### Example Usage

<!-- UsageSnippet language="python" operationID="getHealthStatus" method="get" path="/" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
import os


with CriblMgmtPlane(
    security=models.Security(
        client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
        client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
        audience="https://publicapi.cribl.cloud",
    ),
) as cmp_client:

    cmp_client.health.get()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |