# openapi_client.StoreListsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_merchants_merchant_id_store_lists_store_list_id**](StoreListsApi.md#delete_merchants_merchant_id_store_lists_store_list_id) | **DELETE** /merchants/{merchant_id}/store_lists/{store_list_id} | Remove a Store List
[**get_merchants_merchant_id_store_lists**](StoreListsApi.md#get_merchants_merchant_id_store_lists) | **GET** /merchants/{merchant_id}/store_lists | List all Store Lists
[**get_merchants_merchant_id_store_lists_store_list_id**](StoreListsApi.md#get_merchants_merchant_id_store_lists_store_list_id) | **GET** /merchants/{merchant_id}/store_lists/{store_list_id} | Retrieve a Store List
[**post_merchants_merchant_id_store_lists**](StoreListsApi.md#post_merchants_merchant_id_store_lists) | **POST** /merchants/{merchant_id}/store_lists | Create a Store List
[**put_merchants_merchant_id_store_lists_store_list_id**](StoreListsApi.md#put_merchants_merchant_id_store_lists_store_list_id) | **PUT** /merchants/{merchant_id}/store_lists/{store_list_id} | Update a Store List


# **delete_merchants_merchant_id_store_lists_store_list_id**
> delete_merchants_merchant_id_store_lists_store_list_id(merchant_id, store_list_id, content_type=content_type)

Remove a Store List

Remove a store list.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAuthToken
configuration.api_key['XAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StoreListsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store lists
    store_list_id = 'store_list_id_example' # str | the store list to search for
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove a Store List
        api_instance.delete_merchants_merchant_id_store_lists_store_list_id(merchant_id, store_list_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling StoreListsApi->delete_merchants_merchant_id_store_lists_store_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the store lists | 
 **store_list_id** | **str**| the store list to search for | 
 **content_type** | **str**| application/json | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants_merchant_id_store_lists**
> StoreListIndexBody get_merchants_merchant_id_store_lists(merchant_id, content_type=content_type, page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)

List all Store Lists

Search for store lists by merchant ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.store_list_index_body import StoreListIndexBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAuthToken
configuration.api_key['XAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StoreListsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store lists
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    search_text = 'search_text_example' # str | search for records containing the text (optional)

    try:
        # List all Store Lists
        api_response = api_instance.get_merchants_merchant_id_store_lists(merchant_id, content_type=content_type, page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)
        print("The response of StoreListsApi->get_merchants_merchant_id_store_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreListsApi->get_merchants_merchant_id_store_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the store lists | 
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **search_text** | **str**| search for records containing the text | [optional] 

### Return type

[**StoreListIndexBody**](StoreListIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants_merchant_id_store_lists_store_list_id**
> StoreList get_merchants_merchant_id_store_lists_store_list_id(merchant_id, store_list_id, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Retrieve a Store List

Look up a store list by ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.store_list import StoreList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAuthToken
configuration.api_key['XAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StoreListsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store lists
    store_list_id = 'store_list_id_example' # str | the store list to search for
    content_type = 'content_type_example' # str | application/json (optional)
    page = 56 # int | page offset (optional)
    per_page = 56 # int | number of items per page (optional)
    search_text = 'search_text_example' # str | search for matching text (optional)
    sort_by = 'sort_by_example' # str | id or name (optional)
    order = 'order_example' # str | asc or desc for ascending or descending, respectively (optional)

    try:
        # Retrieve a Store List
        api_response = api_instance.get_merchants_merchant_id_store_lists_store_list_id(merchant_id, store_list_id, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of StoreListsApi->get_merchants_merchant_id_store_lists_store_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreListsApi->get_merchants_merchant_id_store_lists_store_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the store lists | 
 **store_list_id** | **str**| the store list to search for | 
 **content_type** | **str**| application/json | [optional] 
 **page** | **int**| page offset | [optional] 
 **per_page** | **int**| number of items per page | [optional] 
 **search_text** | **str**| search for matching text | [optional] 
 **sort_by** | **str**| id or name | [optional] 
 **order** | **str**| asc or desc for ascending or descending, respectively | [optional] 

### Return type

[**StoreList**](StoreList.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_merchants_merchant_id_store_lists**
> StoreList post_merchants_merchant_id_store_lists(merchant_id, content_type=content_type, store_list_request=store_list_request)

Create a Store List

Add a new store list for a merchant.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.store_list import StoreList
from openapi_client.models.store_list_request import StoreListRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAuthToken
configuration.api_key['XAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StoreListsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store lists
    content_type = 'content_type_example' # str | application/json (optional)
    store_list_request = openapi_client.StoreListRequest() # StoreListRequest |  (optional)

    try:
        # Create a Store List
        api_response = api_instance.post_merchants_merchant_id_store_lists(merchant_id, content_type=content_type, store_list_request=store_list_request)
        print("The response of StoreListsApi->post_merchants_merchant_id_store_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreListsApi->post_merchants_merchant_id_store_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the store lists | 
 **content_type** | **str**| application/json | [optional] 
 **store_list_request** | [**StoreListRequest**](StoreListRequest.md)|  | [optional] 

### Return type

[**StoreList**](StoreList.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_merchants_merchant_id_store_lists_store_list_id**
> StoreList put_merchants_merchant_id_store_lists_store_list_id(merchant_id, store_list_id, content_type=content_type, store_list_request=store_list_request)

Update a Store List

Update an existing store list.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.store_list import StoreList
from openapi_client.models.store_list_request import StoreListRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAuthToken
configuration.api_key['XAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthToken'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StoreListsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store lists
    store_list_id = 'store_list_id_example' # str | the store list to search for
    content_type = 'content_type_example' # str | application/json (optional)
    store_list_request = openapi_client.StoreListRequest() # StoreListRequest |  (optional)

    try:
        # Update a Store List
        api_response = api_instance.put_merchants_merchant_id_store_lists_store_list_id(merchant_id, store_list_id, content_type=content_type, store_list_request=store_list_request)
        print("The response of StoreListsApi->put_merchants_merchant_id_store_lists_store_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreListsApi->put_merchants_merchant_id_store_lists_store_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the store lists | 
 **store_list_id** | **str**| the store list to search for | 
 **content_type** | **str**| application/json | [optional] 
 **store_list_request** | [**StoreListRequest**](StoreListRequest.md)|  | [optional] 

### Return type

[**StoreList**](StoreList.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

