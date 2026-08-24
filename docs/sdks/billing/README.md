# Billing

## Overview

Operations related to Billing and FinOps data

### Available Operations

* [get_contracts_utilization](#get_contracts_utilization) - Get contract credit utilization
* [get_credits_timeseries](#get_credits_timeseries) - Get credits timeseries
* [get_credits_stats](#get_credits_stats) - Get credit balance and consumption
* [get_credits_grants](#get_credits_grants) - Get credit grants

## get_contracts_utilization

Get cumulative credit utilization data grouped by contract period for the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.billing.getContractsUtilization" method="get" path="/v1/organizations/{organizationId}/billing/credits/contracts-utilization" -->
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

    res = cmp_client.billing.get_contracts_utilization(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"), window=models.BillingWindow.MONTHLY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                                                                          | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The <code>id</code> of the Organization.                                                                                                                                                   |                                                                                                                                                                                            |
| `starting_on`                                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly. | 2025-05-01 00:00:00 +0000 UTC                                                                                                                                                              |
| `ending_before`                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                       | :heavy_check_mark:                                                                                                                                                                         | Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.      | 2025-06-01 00:00:00 +0000 UTC                                                                                                                                                              |
| `window`                                                                                                                                                                                   | [models.BillingWindow](../../models/billingwindow.md)                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | Aggregation granularity for credit utilization data. Determines the maximum allowed date range: up to 6 months for daily, up to 7 years for monthly.                                       |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[models.V1BillingGetContractsUtilizationResponse](../../models/v1billinggetcontractsutilizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_credits_timeseries

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

    res = cmp_client.billing.get_credits_timeseries(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"), window=models.BillingWindow.MONTHLY)

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

## get_credits_stats

Get credit balance totals, consumption totals, and contract date ranges for the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.billing.getCreditsStats" method="get" path="/v1/organizations/{organizationId}/billing/credits/stats" -->
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

    res = cmp_client.billing.get_credits_stats(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                | Example                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                          | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | The <code>id</code> of the Organization.                                                                                                   |                                                                                                                                            |
| `starting_on`                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                       | :heavy_check_mark:                                                                                                                         | Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range is 7 years. | 2025-05-01 00:00:00 +0000 UTC                                                                                                              |
| `ending_before`                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                       | :heavy_check_mark:                                                                                                                         | Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range is 7 years.      | 2025-06-01 00:00:00 +0000 UTC                                                                                                              |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |                                                                                                                                            |

### Response

**[models.V1BillingGetCreditsStatsResponse](../../models/v1billinggetcreditsstatsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_credits_grants

Get credit grants (purchases, rollovers, and refunds) for the specified Organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="v1.billing.getCreditsGrants" method="get" path="/v1/organizations/{organizationId}/billing/credits/grants" -->
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

    res = cmp_client.billing.get_credits_grants(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                | Example                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                          | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | The <code>id</code> of the Organization.                                                                                                   |                                                                                                                                            |
| `starting_on`                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                       | :heavy_check_mark:                                                                                                                         | Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range is 7 years. | 2025-05-01 00:00:00 +0000 UTC                                                                                                              |
| `ending_before`                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                       | :heavy_check_mark:                                                                                                                         | Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range is 7 years.      | 2025-06-01 00:00:00 +0000 UTC                                                                                                              |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |                                                                                                                                            |

### Response

**[models.V1BillingGetCreditsGrantsResponse](../../models/v1billinggetcreditsgrantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |