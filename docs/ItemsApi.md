# sparkfly.ItemsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_set**](ItemsApi.md#add_item_to_set) | **POST** /item_sets/{item_set_id}/items/{id} | Add Item to Set
[**create_item**](ItemsApi.md#create_item) | **POST** /items | Create Item
[**create_item_set**](ItemsApi.md#create_item_set) | **POST** /item_sets | Item Set Create
[**delete_item**](ItemsApi.md#delete_item) | **DELETE** /items/{id} | Delete Item
[**delete_item_set**](ItemsApi.md#delete_item_set) | **DELETE** /item_sets/{item_set_id} | Delete an Item Set
[**delete_item_set_items**](ItemsApi.md#delete_item_set_items) | **DELETE** /item_sets/{item_set_id}/items/{id} | Remove Item from Set
[**get_item**](ItemsApi.md#get_item) | **GET** /items/{id} | Get Item
[**get_item_set**](ItemsApi.md#get_item_set) | **GET** /item_sets/{item_set_id} | Get an Item Set
[**list_item_sets**](ItemsApi.md#list_item_sets) | **GET** /item_sets | Item Set Index
[**list_items**](ItemsApi.md#list_items) | **GET** /items | Item Index
[**list_set_items**](ItemsApi.md#list_set_items) | **GET** /item_sets/{item_set_id}/items | Item Set Item Index
[**update_item**](ItemsApi.md#update_item) | **PUT** /items/{id} | Update Item
[**update_item_set**](ItemsApi.md#update_item_set) | **PUT** /item_sets/{item_set_id} | Update an Item Set


# **add_item_to_set**
> add_item_to_set(item_set_id, id, content_type=content_type)

Add Item to Set

Adds an item to the item set.

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
    api_instance = sparkfly.ItemsApi(api_client)
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    id = 'id_example' # str | The primary key of the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Add Item to Set
        await api_instance.add_item_to_set(item_set_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->add_item_to_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_set_id** | **str**| The primary key of the item set | 
 **id** | **str**| The primary key of the item | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item**
> Item create_item(content_type=content_type, item_request=item_request)

Create Item

Creates an item.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item import Item
from sparkfly.models.item_request import ItemRequest
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
    api_instance = sparkfly.ItemsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    item_request = sparkfly.ItemRequest() # ItemRequest |  (optional)

    try:
        # Create Item
        api_response = await api_instance.create_item(content_type=content_type, item_request=item_request)
        print("The response of ItemsApi->create_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **item_request** | [**ItemRequest**](ItemRequest.md)|  | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**401** | Unauthorized |  -  |
**422** | Example response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_set**
> ItemSet create_item_set(content_type=content_type, item_set_request=item_set_request)

Item Set Create

Creates an item set.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item_set import ItemSet
from sparkfly.models.item_set_request import ItemSetRequest
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
    api_instance = sparkfly.ItemsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    item_set_request = sparkfly.ItemSetRequest() # ItemSetRequest |  (optional)

    try:
        # Item Set Create
        api_response = await api_instance.create_item_set(content_type=content_type, item_set_request=item_set_request)
        print("The response of ItemsApi->create_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_item_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **item_set_request** | [**ItemSetRequest**](ItemSetRequest.md)|  | [optional] 

### Return type

[**ItemSet**](ItemSet.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**401** | Unauthorized |  -  |
**422** | Example response |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(id, content_type=content_type)

Delete Item

Deletes an item.

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
    api_instance = sparkfly.ItemsApi(api_client)
    id = 'id_example' # str | Primary key for the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Delete Item
        await api_instance.delete_item(id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Primary key for the item | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_set**
> delete_item_set(item_set_id, content_type=content_type)

Delete an Item Set

Deletes an item set.

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
    api_instance = sparkfly.ItemsApi(api_client)
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Delete an Item Set
        await api_instance.delete_item_set(item_set_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_set_items**
> delete_item_set_items(item_set_id, id, content_type=content_type)

Remove Item from Set

Removes an item from an item set.

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
    api_instance = sparkfly.ItemsApi(api_client)
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    id = 'id_example' # str | The primary key of the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove Item from Set
        await api_instance.delete_item_set_items(item_set_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item_set_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_set_id** | **str**| The primary key of the item set | 
 **id** | **str**| The primary key of the item | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> Item get_item(id, content_type=content_type)

Get Item

Gets an item.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item import Item
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
    api_instance = sparkfly.ItemsApi(api_client)
    id = 'id_example' # str | Primary key for the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get Item
        api_response = await api_instance.get_item(id, content_type=content_type)
        print("The response of ItemsApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Primary key for the item | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_set**
> ItemSet get_item_set(item_set_id, content_type=content_type)

Get an Item Set

Gets an item set.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item_set import ItemSet
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
    api_instance = sparkfly.ItemsApi(api_client)
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get an Item Set
        api_response = await api_instance.get_item_set(item_set_id, content_type=content_type)
        print("The response of ItemsApi->get_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**ItemSet**](ItemSet.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_sets**
> ItemSetIndexBody list_item_sets(content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Item Set Index

Get all item sets.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item_set_index_body import ItemSetIndexBody
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
    api_instance = sparkfly.ItemsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # Item Set Index
        api_response = await api_instance.list_item_sets(content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of ItemsApi->list_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_item_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**ItemSetIndexBody**](ItemSetIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> ItemIndexBody list_items(content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Item Index

Get all items.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item_index_body import ItemIndexBody
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
    api_instance = sparkfly.ItemsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # Item Index
        api_response = await api_instance.list_items(content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of ItemsApi->list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**ItemIndexBody**](ItemIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_set_items**
> ItemIndexBody list_set_items(item_set_id, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Item Set Item Index

Gets a list of items from the item set.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item_index_body import ItemIndexBody
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
    api_instance = sparkfly.ItemsApi(api_client)
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # Item Set Item Index
        api_response = await api_instance.list_set_items(item_set_id, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of ItemsApi->list_set_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_set_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**ItemIndexBody**](ItemIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Example response |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> Item update_item(id, content_type=content_type, item_request=item_request)

Update Item

Updates an item.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item import Item
from sparkfly.models.item_request import ItemRequest
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
    api_instance = sparkfly.ItemsApi(api_client)
    id = 'id_example' # str | Primary key for the item
    content_type = 'content_type_example' # str | application/json (optional)
    item_request = sparkfly.ItemRequest() # ItemRequest |  (optional)

    try:
        # Update Item
        api_response = await api_instance.update_item(id, content_type=content_type, item_request=item_request)
        print("The response of ItemsApi->update_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->update_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Primary key for the item | 
 **content_type** | **str**| application/json | [optional] 
 **item_request** | [**ItemRequest**](ItemRequest.md)|  | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_set**
> ItemSet update_item_set(item_set_id, content_type=content_type, item_set_request=item_set_request)

Update an Item Set

Updates an item set.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.item_set import ItemSet
from sparkfly.models.item_set_request import ItemSetRequest
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
    api_instance = sparkfly.ItemsApi(api_client)
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)
    item_set_request = sparkfly.ItemSetRequest() # ItemSetRequest |  (optional)

    try:
        # Update an Item Set
        api_response = await api_instance.update_item_set(item_set_id, content_type=content_type, item_set_request=item_set_request)
        print("The response of ItemsApi->update_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->update_item_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 
 **item_set_request** | [**ItemSetRequest**](ItemSetRequest.md)|  | [optional] 

### Return type

[**ItemSet**](ItemSet.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

