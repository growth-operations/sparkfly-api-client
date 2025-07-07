# sparkfly.StoresApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_merchants_merchant_id_stores_store_id**](StoresApi.md#delete_merchants_merchant_id_stores_store_id) | **DELETE** /merchants/{merchant_id}/stores/{store_id} | Remove a Store
[**get_merchants_merchant_id_stores**](StoresApi.md#get_merchants_merchant_id_stores) | **GET** /merchants/{merchant_id}/stores | List all Stores
[**get_merchants_merchant_id_stores_index**](StoresApi.md#get_merchants_merchant_id_stores_index) | **GET** /merchants/stores/index | List all Stores with Active Offers
[**get_merchants_merchant_id_stores_store_id**](StoresApi.md#get_merchants_merchant_id_stores_store_id) | **GET** /merchants/{merchant_id}/stores/{store_id} | Retrieve a Store
[**post_merchants_merchant_id_stores**](StoresApi.md#post_merchants_merchant_id_stores) | **POST** /merchants/{merchant_id}/stores | Create a Store
[**put_merchants_merchant_id_stores_store_id**](StoresApi.md#put_merchants_merchant_id_stores_store_id) | **PUT** /merchants/{merchant_id}/stores/{store_id} | Update a Store


# **delete_merchants_merchant_id_stores_store_id**
> delete_merchants_merchant_id_stores_store_id(store_id, merchant_id, content_type=content_type)

Remove a Store

Remove a store.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly.Configuration(
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
async with sparkfly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly.StoresApi(api_client)
    store_id = 'store_id_example' # str | the store's primary key
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store 
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove a Store
        await api_instance.delete_merchants_merchant_id_stores_store_id(store_id, merchant_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling StoresApi->delete_merchants_merchant_id_stores_store_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| the store&#39;s primary key | 
 **merchant_id** | **str**| merchant ID owning the store  | 
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
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants_merchant_id_stores**
> StoreIndexBody get_merchants_merchant_id_stores(merchant_id, search_text=search_text, sort_by=sort_by, page=page, per_page=per_page, order=order)

List all Stores

Search for stores by merchant ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.store_index_body import StoreIndexBody
from sparkfly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly.Configuration(
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
async with sparkfly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly.StoresApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the stores
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # List all Stores
        api_response = await api_instance.get_merchants_merchant_id_stores(merchant_id, search_text=search_text, sort_by=sort_by, page=page, per_page=per_page, order=order)
        print("The response of StoresApi->get_merchants_merchant_id_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->get_merchants_merchant_id_stores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the stores | 
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**StoreIndexBody**](StoreIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants_merchant_id_stores_index**
> StoreIndexBody get_merchants_merchant_id_stores_index(content_type=content_type, page=page, per_page=per_page, order=order, search_text=search_text, sort_by=sort_by)

List all Stores with Active Offers

Search stores with active offers.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.store_index_body import StoreIndexBody
from sparkfly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly.Configuration(
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
async with sparkfly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly.StoresApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | sort records by the specified field (optional) (default to id)

    try:
        # List all Stores with Active Offers
        api_response = await api_instance.get_merchants_merchant_id_stores_index(content_type=content_type, page=page, per_page=per_page, order=order, search_text=search_text, sort_by=sort_by)
        print("The response of StoresApi->get_merchants_merchant_id_stores_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->get_merchants_merchant_id_stores_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| sort records by the specified field | [optional] [default to id]

### Return type

[**StoreIndexBody**](StoreIndexBody.md)

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

# **get_merchants_merchant_id_stores_store_id**
> Store get_merchants_merchant_id_stores_store_id(store_id, merchant_id, content_type=content_type)

Retrieve a Store

Look a store up by it's ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.store import Store
from sparkfly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly.Configuration(
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
async with sparkfly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly.StoresApi(api_client)
    store_id = 'store_id_example' # str | the store's primary key
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store 
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Retrieve a Store
        api_response = await api_instance.get_merchants_merchant_id_stores_store_id(store_id, merchant_id, content_type=content_type)
        print("The response of StoresApi->get_merchants_merchant_id_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->get_merchants_merchant_id_stores_store_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| the store&#39;s primary key | 
 **merchant_id** | **str**| merchant ID owning the store  | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**Store**](Store.md)

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

# **post_merchants_merchant_id_stores**
> Store post_merchants_merchant_id_stores(merchant_id, content_type=content_type, store_request=store_request)

Create a Store

Add a new store for a merchant.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.store import Store
from sparkfly.models.store_request import StoreRequest
from sparkfly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly.Configuration(
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
async with sparkfly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly.StoresApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant ID owning the stores
    content_type = 'content_type_example' # str | application/json (optional)
    store_request = sparkfly.StoreRequest() # StoreRequest |  (optional)

    try:
        # Create a Store
        api_response = await api_instance.post_merchants_merchant_id_stores(merchant_id, content_type=content_type, store_request=store_request)
        print("The response of StoresApi->post_merchants_merchant_id_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->post_merchants_merchant_id_stores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant ID owning the stores | 
 **content_type** | **str**| application/json | [optional] 
 **store_request** | [**StoreRequest**](StoreRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_merchants_merchant_id_stores_store_id**
> Store put_merchants_merchant_id_stores_store_id(store_id, merchant_id, content_type=content_type, store_request=store_request)

Update a Store

Update an existing store.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.store import Store
from sparkfly.models.store_request import StoreRequest
from sparkfly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly.Configuration(
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
async with sparkfly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly.StoresApi(api_client)
    store_id = 'store_id_example' # str | the store's primary key
    merchant_id = 'merchant_id_example' # str | merchant ID owning the store 
    content_type = 'content_type_example' # str | application/json (optional)
    store_request = sparkfly.StoreRequest() # StoreRequest |  (optional)

    try:
        # Update a Store
        api_response = await api_instance.put_merchants_merchant_id_stores_store_id(store_id, merchant_id, content_type=content_type, store_request=store_request)
        print("The response of StoresApi->put_merchants_merchant_id_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoresApi->put_merchants_merchant_id_stores_store_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| the store&#39;s primary key | 
 **merchant_id** | **str**| merchant ID owning the store  | 
 **content_type** | **str**| application/json | [optional] 
 **store_request** | [**StoreRequest**](StoreRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

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

