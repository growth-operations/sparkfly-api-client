# openapi_client.ItemsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_item_sets_item_set_id**](ItemsApi.md#delete_item_sets_item_set_id) | **DELETE** /item_sets/{item_set_id} | Delete an Item Set
[**delete_item_sets_item_set_id_items_id**](ItemsApi.md#delete_item_sets_item_set_id_items_id) | **DELETE** /item_sets/{item_set_id}/items/{id} | Remove Item from Set
[**delete_items_id**](ItemsApi.md#delete_items_id) | **DELETE** /items/{id} | Delete Item
[**get_item_sets**](ItemsApi.md#get_item_sets) | **GET** /item_sets | Item Set Index
[**get_item_sets_item_set_id**](ItemsApi.md#get_item_sets_item_set_id) | **GET** /item_sets/{item_set_id} | Get an Item Set
[**get_item_sets_item_set_id_items**](ItemsApi.md#get_item_sets_item_set_id_items) | **GET** /item_sets/{item_set_id}/items | Item Set Item Index
[**get_items**](ItemsApi.md#get_items) | **GET** /items | Item Index
[**get_items_id**](ItemsApi.md#get_items_id) | **GET** /items/{id} | Get Item
[**post_item_sets**](ItemsApi.md#post_item_sets) | **POST** /item_sets | Item Set Create
[**post_item_sets_item_set_id_items_id**](ItemsApi.md#post_item_sets_item_set_id_items_id) | **POST** /item_sets/{item_set_id}/items/{id} | Add Item to Set
[**post_items**](ItemsApi.md#post_items) | **POST** /items | Create Item
[**put_item_sets_item_set_id**](ItemsApi.md#put_item_sets_item_set_id) | **PUT** /item_sets/{item_set_id} | Update an Item Set
[**put_items_id**](ItemsApi.md#put_items_id) | **PUT** /items/{id} | Update Item


# **delete_item_sets_item_set_id**
> delete_item_sets_item_set_id(x_auth_token, item_set_id, content_type=content_type)

Delete an Item Set

Deletes an item set.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Delete an Item Set
        api_instance.delete_item_sets_item_set_id(x_auth_token, item_set_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item_sets_item_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sets_item_set_id_items_id**
> delete_item_sets_item_set_id_items_id(x_auth_token, item_set_id, id, content_type=content_type)

Remove Item from Set

Removes an item from an item set.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    id = 'id_example' # str | The primary key of the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove Item from Set
        api_instance.delete_item_sets_item_set_id_items_id(x_auth_token, item_set_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item_sets_item_set_id_items_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **item_set_id** | **str**| The primary key of the item set | 
 **id** | **str**| The primary key of the item | 
 **content_type** | **str**| application/json | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **delete_items_id**
> delete_items_id(x_auth_token, id, content_type=content_type)

Delete Item

Deletes an item.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    id = 'id_example' # str | Primary key for the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Delete Item
        api_instance.delete_items_id(x_auth_token, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_items_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **id** | **str**| Primary key for the item | 
 **content_type** | **str**| application/json | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **get_item_sets**
> ItemSetIndexBody get_item_sets(x_auth_token, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Item Set Index

Get all item sets.

### Example


```python
import openapi_client
from openapi_client.models.item_set_index_body import ItemSetIndexBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # Item Set Index
        api_response = api_instance.get_item_sets(x_auth_token, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of ItemsApi->get_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**ItemSetIndexBody**](ItemSetIndexBody.md)

### Authorization

No authorization required

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

# **get_item_sets_item_set_id**
> ItemSet get_item_sets_item_set_id(x_auth_token, item_set_id, content_type=content_type)

Get an Item Set

Gets an item set.

### Example


```python
import openapi_client
from openapi_client.models.item_set import ItemSet
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get an Item Set
        api_response = api_instance.get_item_sets_item_set_id(x_auth_token, item_set_id, content_type=content_type)
        print("The response of ItemsApi->get_item_sets_item_set_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_sets_item_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**ItemSet**](ItemSet.md)

### Authorization

No authorization required

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

# **get_item_sets_item_set_id_items**
> ItemIndexBody get_item_sets_item_set_id_items(x_auth_token, item_set_id, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Item Set Item Index

Gets a list of items from the item set.

### Example


```python
import openapi_client
from openapi_client.models.item_index_body import ItemIndexBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # Item Set Item Index
        api_response = api_instance.get_item_sets_item_set_id_items(x_auth_token, item_set_id, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of ItemsApi->get_item_sets_item_set_id_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_sets_item_set_id_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **get_items**
> ItemIndexBody get_items(x_auth_token, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)

Item Index

Get all items.

### Example


```python
import openapi_client
from openapi_client.models.item_index_body import ItemIndexBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    sort_by = id # str | order the returned records by a specified field (optional) (default to id)
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # Item Index
        api_response = api_instance.get_items(x_auth_token, content_type=content_type, page=page, per_page=per_page, search_text=search_text, sort_by=sort_by, order=order)
        print("The response of ItemsApi->get_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **search_text** | **str**| search for records containing the text | [optional] 
 **sort_by** | **str**| order the returned records by a specified field | [optional] [default to id]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**ItemIndexBody**](ItemIndexBody.md)

### Authorization

No authorization required

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

# **get_items_id**
> Item get_items_id(x_auth_token, id, content_type=content_type)

Get Item

Gets an item.

### Example


```python
import openapi_client
from openapi_client.models.item import Item
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    id = 'id_example' # str | Primary key for the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get Item
        api_response = api_instance.get_items_id(x_auth_token, id, content_type=content_type)
        print("The response of ItemsApi->get_items_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **id** | **str**| Primary key for the item | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

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

# **post_item_sets**
> ItemSet post_item_sets(x_auth_token, content_type=content_type, item_set_request=item_set_request)

Item Set Create

Creates an item set.

### Example


```python
import openapi_client
from openapi_client.models.item_set import ItemSet
from openapi_client.models.item_set_request import ItemSetRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    item_set_request = openapi_client.ItemSetRequest() # ItemSetRequest |  (optional)

    try:
        # Item Set Create
        api_response = api_instance.post_item_sets(x_auth_token, content_type=content_type, item_set_request=item_set_request)
        print("The response of ItemsApi->post_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->post_item_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **item_set_request** | [**ItemSetRequest**](ItemSetRequest.md)|  | [optional] 

### Return type

[**ItemSet**](ItemSet.md)

### Authorization

No authorization required

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

# **post_item_sets_item_set_id_items_id**
> post_item_sets_item_set_id_items_id(x_auth_token, item_set_id, id, content_type=content_type)

Add Item to Set

Adds an item to the item set.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    id = 'id_example' # str | The primary key of the item
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Add Item to Set
        api_instance.post_item_sets_item_set_id_items_id(x_auth_token, item_set_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ItemsApi->post_item_sets_item_set_id_items_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **item_set_id** | **str**| The primary key of the item set | 
 **id** | **str**| The primary key of the item | 
 **content_type** | **str**| application/json | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **post_items**
> Item post_items(x_auth_token, content_type=content_type, item_request=item_request)

Create Item

Creates an item.

### Example


```python
import openapi_client
from openapi_client.models.item import Item
from openapi_client.models.item_request import ItemRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    item_request = openapi_client.ItemRequest() # ItemRequest |  (optional)

    try:
        # Create Item
        api_response = api_instance.post_items(x_auth_token, content_type=content_type, item_request=item_request)
        print("The response of ItemsApi->post_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->post_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **item_request** | [**ItemRequest**](ItemRequest.md)|  | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

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

# **put_item_sets_item_set_id**
> ItemSet put_item_sets_item_set_id(x_auth_token, item_set_id, content_type=content_type, item_set_request=item_set_request)

Update an Item Set

Updates an item set.

### Example


```python
import openapi_client
from openapi_client.models.item_set import ItemSet
from openapi_client.models.item_set_request import ItemSetRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    item_set_id = 'item_set_id_example' # str | The primary key of the item set
    content_type = 'content_type_example' # str | application/json (optional)
    item_set_request = openapi_client.ItemSetRequest() # ItemSetRequest |  (optional)

    try:
        # Update an Item Set
        api_response = api_instance.put_item_sets_item_set_id(x_auth_token, item_set_id, content_type=content_type, item_set_request=item_set_request)
        print("The response of ItemsApi->put_item_sets_item_set_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->put_item_sets_item_set_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **item_set_id** | **str**| The primary key of the item set | 
 **content_type** | **str**| application/json | [optional] 
 **item_set_request** | [**ItemSetRequest**](ItemSetRequest.md)|  | [optional] 

### Return type

[**ItemSet**](ItemSet.md)

### Authorization

No authorization required

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

# **put_items_id**
> Item put_items_id(x_auth_token, id, content_type=content_type, item_request=item_request)

Update Item

Updates an item.

### Example


```python
import openapi_client
from openapi_client.models.item import Item
from openapi_client.models.item_request import ItemRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    id = 'id_example' # str | Primary key for the item
    content_type = 'content_type_example' # str | application/json (optional)
    item_request = openapi_client.ItemRequest() # ItemRequest |  (optional)

    try:
        # Update Item
        api_response = api_instance.put_items_id(x_auth_token, id, content_type=content_type, item_request=item_request)
        print("The response of ItemsApi->put_items_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->put_items_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **id** | **str**| Primary key for the item | 
 **content_type** | **str**| application/json | [optional] 
 **item_request** | [**ItemRequest**](ItemRequest.md)|  | [optional] 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

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

