# structifyai.ServerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version**](ServerApi.md#version) | **GET** /server/version | Version


# **version**
> version()

Version

Version  Gets the version of the API server.

### Example

```python
import time
import os
import structifyai
from structifyai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = structifyai.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with structifyai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = structifyai.ServerApi(api_client)

    try:
        # Version
        api_instance.version()
    except Exception as e:
        print("Exception when calling ServerApi->version: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

