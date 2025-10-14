<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

    res = cmp_client.health.get()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from cribl_mgmt_plane import CriblMgmtPlane, models
import os

async def main():

    async with CriblMgmtPlane(
        security=models.Security(
            client_oauth=models.SchemeClientOauth(
                client_id=os.getenv("CRIBLMGMTPLANE_CLIENT_ID", ""),
                client_secret=os.getenv("CRIBLMGMTPLANE_CLIENT_SECRET", ""),
                token_url=os.getenv("CRIBLMGMTPLANE_TOKEN_URL", ""),
                audience="https://api.cribl.cloud",
            ),
        ),
    ) as cmp_client:

        res = await cmp_client.health.get_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->