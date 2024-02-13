# structifyai.DatasetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](DatasetApi.md#create) | **POST** /dataset/create | Create a Dataset
[**delete**](DatasetApi.md#delete) | **POST** /dataset/delete | Remove a kg from the database
[**get**](DatasetApi.md#get) | **POST** /dataset/get | Remove a kg from the database
[**list**](DatasetApi.md#list) | **POST** /dataset/list | List knowledge graph
[**query**](DatasetApi.md#query) | **GET** /dataset/query | Remove a kg from the database


# **create**
> create()

Create a Dataset

Create a Dataset  Creates a dataset for the user.

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
    api_instance = structifyai.DatasetApi(api_client)

    try:
        # Create a Dataset
        api_instance.create()
    except Exception as e:
        print("Exception when calling DatasetApi->create: %s\n" % e)
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
**200** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete()

Remove a kg from the database

Remove a kg from the database

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
    api_instance = structifyai.DatasetApi(api_client)

    try:
        # Remove a kg from the database
        api_instance.delete()
    except Exception as e:
        print("Exception when calling DatasetApi->delete: %s\n" % e)
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
**200** | Document deleted successfully |  -  |
**400** | Invalid document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get()

Remove a kg from the database

Remove a kg from the database

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
    api_instance = structifyai.DatasetApi(api_client)

    try:
        # Remove a kg from the database
        api_instance.get()
    except Exception as e:
        print("Exception when calling DatasetApi->get: %s\n" % e)
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
**200** | Document deleted successfully |  -  |
**400** | Invalid document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list()

List knowledge graph

List knowledge graph  Iterate through all the nodes and edges of the csv in json format

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
    api_instance = structifyai.DatasetApi(api_client)

    try:
        # List knowledge graph
        api_instance.list()
    except Exception as e:
        print("Exception when calling DatasetApi->list: %s\n" % e)
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
**200** | Listed all nodes and edges |  -  |
**400** | Invalid document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> query()

Remove a kg from the database

Remove a kg from the database

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
    api_instance = structifyai.DatasetApi(api_client)

    try:
        # Remove a kg from the database
        api_instance.query()
    except Exception as e:
        print("Exception when calling DatasetApi->query: %s\n" % e)
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
**200** | Document deleted successfully |  -  |
**400** | Invalid document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

