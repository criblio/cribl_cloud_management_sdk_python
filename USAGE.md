<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from cribl_mgmt_plane import CriblMgmtPlane
import os


with CriblMgmtPlane(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
) as cmp_client:

    cmp_client.dummy_service_status()

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from cribl_mgmt_plane import CriblMgmtPlane
import os

async def main():

    async with CriblMgmtPlane(
        server_url="https://api.example.com",
        bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
    ) as cmp_client:

        await cmp_client.dummy_service_status_async()

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->