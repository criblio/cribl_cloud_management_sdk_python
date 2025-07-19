# cribl_cloud_management_sdk_python
<!-- Start Summary [summary] -->
## Summary

Cribl Cloud Management API: Lorem Ipsum
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [cribl_cloud_management_sdk_python](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#criblcloudmanagementsdkpython)
  * [SDK Installation](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#retries)
  * [Error Handling](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#error-handling)
  * [Custom HTTP Client](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#resource-management)
  * [Debugging](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install cribl-mgmt-plane
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add cribl-mgmt-plane
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from cribl-mgmt-plane python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "cribl-mgmt-plane",
# ]
# ///

from cribl_mgmt_plane import CriblMgmtPlane

sdk = CriblMgmtPlane(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable         |
| ------------- | ---- | ----------- | ---------------------------- |
| `bearer_auth` | http | HTTP Bearer | `CRIBLMGMTPLANE_BEARER_AUTH` |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [CriblMgmtPlane SDK](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/docs/sdks/criblmgmtplane/README.md)

* [dummy_service_status](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/docs/sdks/criblmgmtplane/README.md#dummy_service_status) - Service status

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from cribl_mgmt_plane import CriblMgmtPlane
from cribl_mgmt_plane.utils import BackoffStrategy, RetryConfig
import os


with CriblMgmtPlane(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
) as cmp_client:

    cmp_client.dummy_service_status(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from cribl_mgmt_plane import CriblMgmtPlane
from cribl_mgmt_plane.utils import BackoffStrategy, RetryConfig
import os


with CriblMgmtPlane(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
) as cmp_client:

    cmp_client.dummy_service_status()

    # Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`CriblMgmtPlaneError`](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/./src/cribl_mgmt_plane/errors/criblmgmtplaneerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from cribl_mgmt_plane import CriblMgmtPlane, errors
import os


with CriblMgmtPlane(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
) as cmp_client:

    try:

        cmp_client.dummy_service_status()

        # Use the SDK ...


    except errors.CriblMgmtPlaneError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`CriblMgmtPlaneError`](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/./src/cribl_mgmt_plane/errors/criblmgmtplaneerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CriblMgmtPlaneError`](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/./src/cribl_mgmt_plane/errors/criblmgmtplaneerror.py)**:
* [`ResponseValidationError`](https://github.com/criblio/cribl_cloud_management_sdk_python/blob/master/./src/cribl_mgmt_plane/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from cribl_mgmt_plane import CriblMgmtPlane
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CriblMgmtPlane(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from cribl_mgmt_plane import CriblMgmtPlane
from cribl_mgmt_plane.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = CriblMgmtPlane(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `CriblMgmtPlane` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from cribl_mgmt_plane import CriblMgmtPlane
import os
def main():

    with CriblMgmtPlane(
        server_url="https://api.example.com",
        bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
    ) as cmp_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with CriblMgmtPlane(
        server_url="https://api.example.com",
        bearer_auth=os.getenv("CRIBLMGMTPLANE_BEARER_AUTH", ""),
    ) as cmp_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from cribl_mgmt_plane import CriblMgmtPlane
import logging

logging.basicConfig(level=logging.DEBUG)
s = CriblMgmtPlane(server_url="https://example.com", debug_logger=logging.getLogger("cribl_mgmt_plane"))
```

You can also enable a default debug logger by setting an environment variable `CRIBLMGMTPLANE_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
