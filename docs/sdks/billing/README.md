# Billing

## Overview

Operations related to Billing and FinOps data

### Available Operations

* [get_contracts_utilization](#get_contracts_utilization) - [In development] Get contract credit utilization
* [get_credits_timeseries](#get_credits_timeseries) - [In development] Get credits timeseries
* [get_credits_stats](#get_credits_stats) - [In development] Get credit balance and consumption
* [get_credits_grants](#get_credits_grants) - [In development] Get credit grants

## get_contracts_utilization

**This endpoint is in development with restricted availability**. We do not recommend using this endpoint in production. Functionality might change without notice. Contact [Cribl Support](https://cribl.io/support/) to request access.

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

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization.                             |                                                                      |
| `starting_on`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Inclusive start of the query date range in ISO 8601 format.          | 2025-05-01 00:00:00 +0000 UTC                                        |
| `ending_before`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Exclusive end of the query date range in ISO 8601 format.            | 2025-06-01 00:00:00 +0000 UTC                                        |
| `window`                                                             | [models.BillingWindow](../../models/billingwindow.md)                | :heavy_check_mark:                                                   | Aggregation granularity for credit utilization data.                 |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.V1BillingGetContractsUtilizationResponse](../../models/v1billinggetcontractsutilizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_credits_timeseries

**This endpoint is in development with restricted availability**. We do not recommend using this endpoint in production. Functionality might change without notice. Contact [Cribl Support](https://cribl.io/support/) to request access.

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

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization.                             |                                                                      |
| `starting_on`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Inclusive start of the query date range in ISO 8601 format.          | 2025-05-01 00:00:00 +0000 UTC                                        |
| `ending_before`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Exclusive end of the query date range in ISO 8601 format.            | 2025-06-01 00:00:00 +0000 UTC                                        |
| `window`                                                             | [models.BillingWindow](../../models/billingwindow.md)                | :heavy_check_mark:                                                   | Aggregation granularity for timeseries data.                         |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.V1BillingGetCreditsTimeseriesResponse](../../models/v1billinggetcreditstimeseriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_credits_stats

**This endpoint is in development with restricted availability**. We do not recommend using this endpoint in production. Functionality might change without notice. Contact [Cribl Support](https://cribl.io/support/) to request access.

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

    res = cmp_client.billing.get_credits_stats(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"), window=models.BillingWindow.MONTHLY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization.                             |                                                                      |
| `starting_on`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Inclusive start of the query date range in ISO 8601 format.          | 2025-05-01 00:00:00 +0000 UTC                                        |
| `ending_before`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Exclusive end of the query date range in ISO 8601 format.            | 2025-06-01 00:00:00 +0000 UTC                                        |
| `window`                                                             | [models.BillingWindow](../../models/billingwindow.md)                | :heavy_check_mark:                                                   | Aggregation granularity for credit balance and consumption.          |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.V1BillingGetCreditsStatsResponse](../../models/v1billinggetcreditsstatsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_credits_grants

**This endpoint is in development with restricted availability**. We do not recommend using this endpoint in production. Functionality might change without notice. Contact [Cribl Support](https://cribl.io/support/) to request access.

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

    res = cmp_client.billing.get_credits_grants(organization_id="<id>", starting_on=parse_datetime("2025-05-01T00:00:00Z"), ending_before=parse_datetime("2025-06-01T00:00:00Z"), window=models.BillingWindow.DAILY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The <code>id</code> of the Organization.                             |                                                                      |
| `starting_on`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Inclusive start of the query date range in ISO 8601 format.          | 2025-05-01 00:00:00 +0000 UTC                                        |
| `ending_before`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Exclusive end of the query date range in ISO 8601 format.            | 2025-06-01 00:00:00 +0000 UTC                                        |
| `window`                                                             | [models.BillingWindow](../../models/billingwindow.md)                | :heavy_check_mark:                                                   | Aggregation granularity for credit grant data.                       |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.V1BillingGetCreditsGrantsResponse](../../models/v1billinggetcreditsgrantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |