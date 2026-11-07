# Billing.Credits.Timeseries

## Overview

### Available Operations

* [list](#list) - Get credits timeseries

## list

Get credit consumption timeseries data for the specified Organization, broken down by dimensions such as product and usage type.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.billing.getCreditsTimeseries" method="get" path="/v1/organizations/{organizationId}/billing/credits/timeseries" -->
```python
from cribl_mgmt_plane import CriblMgmtPlane, models
from cribl_mgmt_plane.utils import parse_datetime
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

    res = cmp_client.billing.credits.timeseries.list(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"), window=models.BillingWindow.MONTHLY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                                                                          | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The <code>id</code> of the Organization.                                                                                                                                                   |                                                                                                                                                                                            |
| `starting_on`                                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly. | 2025-05-01 00:00:00 +0000 UTC                                                                                                                                                              |
| `ending_before`                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.      | 2025-06-01 00:00:00 +0000 UTC                                                                                                                                                              |
| `window`                                                                                                                                                                                   | [models.BillingWindow](../../models/billingwindow.md)                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | Aggregation granularity for timeseries data. Determines the maximum allowed date range: up to 6 months for daily, up to 7 years for monthly.                                               |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[models.V1BillingGetCreditsTimeseriesResponse](../../models/v1billinggetcreditstimeseriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |