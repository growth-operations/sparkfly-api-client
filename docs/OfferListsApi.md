# openapi_client.OfferListsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offer_lists_offer_list_id**](OfferListsApi.md#delete_offer_lists_offer_list_id) | **DELETE** /offer_lists/{offer_list_id} | Remove an Offer List
[**get_offer_lists**](OfferListsApi.md#get_offer_lists) | **GET** /offer_lists | List all Offer Lists
[**get_offer_lists_offer_list_id**](OfferListsApi.md#get_offer_lists_offer_list_id) | **GET** /offer_lists/{offer_list_id} | Retrieve an Offer List
[**post_offer_lists**](OfferListsApi.md#post_offer_lists) | **POST** /offer_lists | Create an Offer List
[**put_offer_lists_offer_list_id**](OfferListsApi.md#put_offer_lists_offer_list_id) | **PUT** /offer_lists/{offer_list_id} | Update an Offer List


# **delete_offer_lists_offer_list_id**
> delete_offer_lists_offer_list_id(offer_list_id)

Remove an Offer List

Remove an offer list.

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
    api_instance = openapi_client.OfferListsApi(api_client)
    offer_list_id = 'offer_list_id_example' # str | primary id of the offer list

    try:
        # Remove an Offer List
        api_instance.delete_offer_lists_offer_list_id(offer_list_id)
    except Exception as e:
        print("Exception when calling OfferListsApi->delete_offer_lists_offer_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_list_id** | **str**| primary id of the offer list | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_lists**
> GetOfferLists200Response get_offer_lists(content_type=content_type, sort_by=sort_by, search_text=search_text, page=page, per_page=per_page, order=order)

List all Offer Lists

Fetch a list of offer lists. The list may be filtered according to the request's query parameters. If no filters are applied, the complete list of available offer lists will be returned.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.get_offer_lists200_response import GetOfferLists200Response
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
    api_instance = openapi_client.OfferListsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | Attempts to match by name or id (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # List all Offer Lists
        api_response = api_instance.get_offer_lists(content_type=content_type, sort_by=sort_by, search_text=search_text, page=page, per_page=per_page, order=order)
        print("The response of OfferListsApi->get_offer_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->get_offer_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **sort_by** | **str**| sort records by a field name | [optional] 
 **search_text** | **str**| Attempts to match by name or id | [optional] 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]

### Return type

[**GetOfferLists200Response**](GetOfferLists200Response.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_lists_offer_list_id**
> InlineObject get_offer_lists_offer_list_id(offer_list_id)

Retrieve an Offer List

Search for an offer list by ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.inline_object import InlineObject
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
    api_instance = openapi_client.OfferListsApi(api_client)
    offer_list_id = 'offer_list_id_example' # str | primary id of the offer list

    try:
        # Retrieve an Offer List
        api_response = api_instance.get_offer_lists_offer_list_id(offer_list_id)
        print("The response of OfferListsApi->get_offer_lists_offer_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->get_offer_lists_offer_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_list_id** | **str**| primary id of the offer list | 

### Return type

[**InlineObject**](InlineObject.md)

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
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_offer_lists**
> InlineObject post_offer_lists(content_type=content_type, post_offer_lists_request=post_offer_lists_request)

Create an Offer List

Create a new offer list containing the specified offer IDs.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.post_offer_lists_request import PostOfferListsRequest
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
    api_instance = openapi_client.OfferListsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    post_offer_lists_request = {offer_list={name=my offer list name, offer_ids=[1111, 2222, 3333, 4444]}} # PostOfferListsRequest |  (optional)

    try:
        # Create an Offer List
        api_response = api_instance.post_offer_lists(content_type=content_type, post_offer_lists_request=post_offer_lists_request)
        print("The response of OfferListsApi->post_offer_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->post_offer_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **post_offer_lists_request** | [**PostOfferListsRequest**](PostOfferListsRequest.md)|  | [optional] 

### Return type

[**InlineObject**](InlineObject.md)

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

# **put_offer_lists_offer_list_id**
> InlineObject put_offer_lists_offer_list_id(offer_list_id, content_type=content_type, post_offer_lists_request=post_offer_lists_request)

Update an Offer List

Update an offer list's contents.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.post_offer_lists_request import PostOfferListsRequest
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
    api_instance = openapi_client.OfferListsApi(api_client)
    offer_list_id = 'offer_list_id_example' # str | primary id of the offer list
    content_type = 'content_type_example' # str | application/json (optional)
    post_offer_lists_request = {offer_list={name=my offer list name, offer_ids=[1111, 2222, 3333, 4444]}} # PostOfferListsRequest |  (optional)

    try:
        # Update an Offer List
        api_response = api_instance.put_offer_lists_offer_list_id(offer_list_id, content_type=content_type, post_offer_lists_request=post_offer_lists_request)
        print("The response of OfferListsApi->put_offer_lists_offer_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->put_offer_lists_offer_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_list_id** | **str**| primary id of the offer list | 
 **content_type** | **str**| application/json | [optional] 
 **post_offer_lists_request** | [**PostOfferListsRequest**](PostOfferListsRequest.md)|  | [optional] 

### Return type

[**InlineObject**](InlineObject.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found.  Either the offer list with the specified ID does not exist or one of the provided offer IDs does not exist. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

