# openapi_client.EligibleItemSetsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offers_offer_id_eligible_item_sets_id**](EligibleItemSetsApi.md#delete_offers_offer_id_eligible_item_sets_id) | **DELETE** /offers/{offer_id}/eligible_item_sets/{id} | Remove an Eligible Item Set
[**get_offers_offer_id_eligible_item_sets**](EligibleItemSetsApi.md#get_offers_offer_id_eligible_item_sets) | **GET** /offers/{offer_id}/eligible_item_sets | List all Eligible Item Sets
[**get_offers_offer_id_eligible_item_sets_id**](EligibleItemSetsApi.md#get_offers_offer_id_eligible_item_sets_id) | **GET** /offers/{offer_id}/eligible_item_sets/{id} | Get an Eligible Item Set
[**post_offers_offer_id_eligible_item_sets**](EligibleItemSetsApi.md#post_offers_offer_id_eligible_item_sets) | **POST** /offers/{offer_id}/eligible_item_sets | Create an Eligible Item Set
[**put_offers_offer_id_eligible_item_sets_id**](EligibleItemSetsApi.md#put_offers_offer_id_eligible_item_sets_id) | **PUT** /offers/{offer_id}/eligible_item_sets/{id} | Update an Eligible Item Set


# **delete_offers_offer_id_eligible_item_sets_id**
> delete_offers_offer_id_eligible_item_sets_id(offer_id, id, content_type=content_type)

Remove an Eligible Item Set

Removes an eligible item set from an offer.

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
    api_instance = openapi_client.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the eligible item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove an Eligible Item Set
        api_instance.delete_offers_offer_id_eligible_item_sets_id(offer_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->delete_offers_offer_id_eligible_item_sets_id: %s\n" % e)
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

# **get_offers_offer_id_eligible_item_sets**
> OfferEligibleItemsSetIndex get_offers_offer_id_eligible_item_sets(offer_id, content_type=content_type)

List all Eligible Item Sets

List all eligible item sets for an offer ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.offer_eligible_items_set_index import OfferEligibleItemsSetIndex
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
    api_instance = openapi_client.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all Eligible Item Sets
        api_response = api_instance.get_offers_offer_id_eligible_item_sets(offer_id, content_type=content_type)
        print("The response of EligibleItemSetsApi->get_offers_offer_id_eligible_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->get_offers_offer_id_eligible_item_sets: %s\n" % e)
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

# **get_offers_offer_id_eligible_item_sets_id**
> OfferEligibleItemSet get_offers_offer_id_eligible_item_sets_id(offer_id, id, content_type=content_type)

Get an Eligible Item Set

Get an eligible item set by offer ID and ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.offer_eligible_item_set import OfferEligibleItemSet
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
    api_instance = openapi_client.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the eligible item set
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get an Eligible Item Set
        api_response = api_instance.get_offers_offer_id_eligible_item_sets_id(offer_id, id, content_type=content_type)
        print("The response of EligibleItemSetsApi->get_offers_offer_id_eligible_item_sets_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->get_offers_offer_id_eligible_item_sets_id: %s\n" % e)
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

# **post_offers_offer_id_eligible_item_sets**
> OfferEligibleItemSet post_offers_offer_id_eligible_item_sets(offer_id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)

Create an Eligible Item Set

Creates an eligible item set on an offer.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.offer_eligible_item_set import OfferEligibleItemSet
from openapi_client.models.offer_eligible_item_set_request import OfferEligibleItemSetRequest
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
    api_instance = openapi_client.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_eligible_item_set_request = openapi_client.OfferEligibleItemSetRequest() # OfferEligibleItemSetRequest |  (optional)

    try:
        # Create an Eligible Item Set
        api_response = api_instance.post_offers_offer_id_eligible_item_sets(offer_id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)
        print("The response of EligibleItemSetsApi->post_offers_offer_id_eligible_item_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->post_offers_offer_id_eligible_item_sets: %s\n" % e)
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

# **put_offers_offer_id_eligible_item_sets_id**
> OfferEligibleItemSet put_offers_offer_id_eligible_item_sets_id(offer_id, id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)

Update an Eligible Item Set

Updates an eligible item set on an offer.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.offer_eligible_item_set import OfferEligibleItemSet
from openapi_client.models.offer_eligible_item_set_request import OfferEligibleItemSetRequest
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
    api_instance = openapi_client.EligibleItemSetsApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the eligible item set
    content_type = 'content_type_example' # str | application/json (optional)
    offer_eligible_item_set_request = openapi_client.OfferEligibleItemSetRequest() # OfferEligibleItemSetRequest |  (optional)

    try:
        # Update an Eligible Item Set
        api_response = api_instance.put_offers_offer_id_eligible_item_sets_id(offer_id, id, content_type=content_type, offer_eligible_item_set_request=offer_eligible_item_set_request)
        print("The response of EligibleItemSetsApi->put_offers_offer_id_eligible_item_sets_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EligibleItemSetsApi->put_offers_offer_id_eligible_item_sets_id: %s\n" % e)
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

