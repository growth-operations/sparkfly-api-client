# sparkfly.EligibleItemSetsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eligible_item_set**](EligibleItemSetsApi.md#create_eligible_item_set) | **POST** /offers/{offer_id}/eligible_item_sets | Create an Eligible Item Set
[**delete_offer_eligible_item_sets**](EligibleItemSetsApi.md#delete_offer_eligible_item_sets) | **DELETE** /offers/{offer_id}/eligible_item_sets/{id} | Remove an Eligible Item Set
[**get_eligible_item_set**](EligibleItemSetsApi.md#get_eligible_item_set) | **GET** /offers/{offer_id}/eligible_item_sets/{id} | Get an Eligible Item Set
[**list_eligible_item_sets**](EligibleItemSetsApi.md#list_eligible_item_sets) | **GET** /offers/{offer_id}/eligible_item_sets | List all Eligible Item Sets
[**update_offer_eligible_item_sets**](EligibleItemSetsApi.md#update_offer_eligible_item_sets) | **PUT** /offers/{offer_id}/eligible_item_sets/{id} | Update an Eligible Item Set


# **create_eligible_item_set**
> OfferEligibleItemSet create_eligible_item_set(offer_id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)

Create an Eligible Item Set

Creates an eligible item set on an offer.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_eligible_item_set import OfferEligibleItemSet
from sparkfly.models.offer_eligible_item_set_request import OfferEligibleItemSetRequest
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
    api_instance = sparkfly.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_eligible_item_set_request = sparkfly.OfferEligibleItemSetRequest() # OfferEligibleItemSetRequest |  (optional)

    try:
        # Create an Eligible Item Set
        api_response = await api_instance.create_eligible_item_set(offer_id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)
        print("The response of EligibleItemSetsApi->create_eligible_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->create_eligible_item_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_eligible_item_set_request** | [**OfferEligibleItemSetRequest**](OfferEligibleItemSetRequest.md)|  | [optional] 

### Return type

[**OfferEligibleItemSet**](OfferEligibleItemSet.md)

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
**401** | Unauthorized |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_offer_eligible_item_sets**
> delete_offer_eligible_item_sets(offer_id, id, content_type=content_type)

Remove an Eligible Item Set

Removes an eligible item set from an offer.

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
    api_instance = sparkfly.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the eligible item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove an Eligible Item Set
        await api_instance.delete_offer_eligible_item_sets(offer_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->delete_offer_eligible_item_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the eligible item set | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eligible_item_set**
> OfferEligibleItemSet get_eligible_item_set(offer_id, id, content_type=content_type)

Get an Eligible Item Set

Get an eligible item set by offer ID and ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_eligible_item_set import OfferEligibleItemSet
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
    api_instance = sparkfly.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the eligible item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get an Eligible Item Set
        api_response = await api_instance.get_eligible_item_set(offer_id, id, content_type=content_type)
        print("The response of EligibleItemSetsApi->get_eligible_item_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->get_eligible_item_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the eligible item set | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferEligibleItemSet**](OfferEligibleItemSet.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_eligible_item_sets**
> OfferEligibleItemsSetIndex list_eligible_item_sets(offer_id, content_type=content_type)

List all Eligible Item Sets

List all eligible item sets for an offer ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_eligible_items_set_index import OfferEligibleItemsSetIndex
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
    api_instance = sparkfly.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all Eligible Item Sets
        api_response = await api_instance.list_eligible_item_sets(offer_id, content_type=content_type)
        print("The response of EligibleItemSetsApi->list_eligible_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->list_eligible_item_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferEligibleItemsSetIndex**](OfferEligibleItemsSetIndex.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer_eligible_item_sets**
> OfferEligibleItemSet update_offer_eligible_item_sets(offer_id, id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)

Update an Eligible Item Set

Updates an eligible item set on an offer.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_eligible_item_set import OfferEligibleItemSet
from sparkfly.models.offer_eligible_item_set_request import OfferEligibleItemSetRequest
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
    api_instance = sparkfly.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the eligible item set
    content_type = 'content_type_example' # str | application/json (optional)
    offer_eligible_item_set_request = sparkfly.OfferEligibleItemSetRequest() # OfferEligibleItemSetRequest |  (optional)

    try:
        # Update an Eligible Item Set
        api_response = await api_instance.update_offer_eligible_item_sets(offer_id, id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)
        print("The response of EligibleItemSetsApi->update_offer_eligible_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->update_offer_eligible_item_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the eligible item set | 
 **content_type** | **str**| application/json | [optional] 
 **offer_eligible_item_set_request** | [**OfferEligibleItemSetRequest**](OfferEligibleItemSetRequest.md)|  | [optional] 

### Return type

[**OfferEligibleItemSet**](OfferEligibleItemSet.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

