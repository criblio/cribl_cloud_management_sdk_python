# CriblMgmtPlane SDK

## Overview

Cribl Cloud Management API: Lorem Ipsum

### Available Operations

* [dummy_service_status](#dummy_service_status) - Service status

## dummy_service_status

Service status

### Example Usage

<!-- UsageSnippet language="python" operationID="dummyServiceStatus" method="get" path="/status" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane
import os


with CriblMgmtPlane(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
) as cmp_client:

    cmp_client.dummy_service_status()

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