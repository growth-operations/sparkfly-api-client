# sparkfly.OfferListsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer_list**](OfferListsApi.md#create_offer_list) | **POST** /offer_lists | Create an Offer List
[**delete_offer_list**](OfferListsApi.md#delete_offer_list) | **DELETE** /offer_lists/{offer_list_id} | Remove an Offer List
[**get_offer_list**](OfferListsApi.md#get_offer_list) | **GET** /offer_lists/{offer_list_id} | Retrieve an Offer List
[**list_offer_lists**](OfferListsApi.md#list_offer_lists) | **GET** /offer_lists | List all Offer Lists
[**update_offer_list**](OfferListsApi.md#update_offer_list) | **PUT** /offer_lists/{offer_list_id} | Update an Offer List


# **create_offer_list**
> OfferListData create_offer_list(content_type=content_type, create_offer_list_request=create_offer_list_request)

Create an Offer List

Create a new offer list containing the specified offer IDs.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.create_offer_list_request import CreateOfferListRequest
from sparkfly.models.offer_list_data import OfferListData
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
    api_instance = sparkfly.OfferListsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    create_offer_list_request = {offer_list={name=my offer list name, offer_ids=[1111, 2222, 3333, 4444]}} # CreateOfferListRequest |  (optional)

    try:
        # Create an Offer List
        api_response = await api_instance.create_offer_list(content_type=content_type, create_offer_list_request=create_offer_list_request)
        print("The response of OfferListsApi->create_offer_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->create_offer_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **create_offer_list_request** | [**CreateOfferListRequest**](CreateOfferListRequest.md)|  | [optional] 

### Return type

[**OfferListData**](OfferListData.md)

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

# **delete_offer_list**
> delete_offer_list(offer_list_id)

Remove an Offer List

Remove an offer list.

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
    api_instance = sparkfly.OfferListsApi(api_client)
    offer_list_id = 'offer_list_id_example' # str | primary id of the offer list

    try:
        # Remove an Offer List
        await api_instance.delete_offer_list(offer_list_id)
    except Exception as e:
        print("Exception when calling OfferListsApi->delete_offer_list: %s\n" % e)
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

# **get_offer_list**
> OfferListData get_offer_list(offer_list_id)

Retrieve an Offer List

Search for an offer list by ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_list_data import OfferListData
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
    api_instance = sparkfly.OfferListsApi(api_client)
    offer_list_id = 'offer_list_id_example' # str | primary id of the offer list

    try:
        # Retrieve an Offer List
        api_response = await api_instance.get_offer_list(offer_list_id)
        print("The response of OfferListsApi->get_offer_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->get_offer_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_list_id** | **str**| primary id of the offer list | 

### Return type

[**OfferListData**](OfferListData.md)

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

# **list_offer_lists**
> OfferListsIndexBody list_offer_lists(content_type=content_type, sort_by=sort_by, search_text=search_text, page=page, per_page=per_page, order=order)

List all Offer Lists

Fetch a list of offer lists. The list may be filtered according to the request's query parameters. If no filters are applied, the complete list of available offer lists will be returned.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_lists_index_body import OfferListsIndexBody
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
    api_instance = sparkfly.OfferListsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | Attempts to match by name or id (optional)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)

    try:
        # List all Offer Lists
        api_response = await api_instance.list_offer_lists(content_type=content_type, sort_by=sort_by, search_text=search_text, page=page, per_page=per_page, order=order)
        print("The response of OfferListsApi->list_offer_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->list_offer_lists: %s\n" % e)
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

[**OfferListsIndexBody**](OfferListsIndexBody.md)

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

# **update_offer_list**
> OfferListData update_offer_list(offer_list_id, content_type=content_type, create_offer_list_request=create_offer_list_request)

Update an Offer List

Update an offer list's contents.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.create_offer_list_request import CreateOfferListRequest
from sparkfly.models.offer_list_data import OfferListData
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
    api_instance = sparkfly.OfferListsApi(api_client)
    offer_list_id = 'offer_list_id_example' # str | primary id of the offer list
    content_type = 'content_type_example' # str | application/json (optional)
    create_offer_list_request = {offer_list={name=my offer list name, offer_ids=[1111, 2222, 3333, 4444]}} # CreateOfferListRequest |  (optional)

    try:
        # Update an Offer List
        api_response = await api_instance.update_offer_list(offer_list_id, content_type=content_type, create_offer_list_request=create_offer_list_request)
        print("The response of OfferListsApi->update_offer_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferListsApi->update_offer_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_list_id** | **str**| primary id of the offer list | 
 **content_type** | **str**| application/json | [optional] 
 **create_offer_list_request** | [**CreateOfferListRequest**](CreateOfferListRequest.md)|  | [optional] 

### Return type

[**OfferListData**](OfferListData.md)

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

