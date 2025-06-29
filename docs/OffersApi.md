# openapi_client.OffersApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offers_offer_id**](OffersApi.md#delete_offers_offer_id) | **DELETE** /offers/{offer_id} | Delete an Offer
[**get_offers**](OffersApi.md#get_offers) | **GET** /offers | List all Offers
[**get_offers_offer_id**](OffersApi.md#get_offers_offer_id) | **GET** /offers/{offer_id} | Find an Offer
[**post_offers**](OffersApi.md#post_offers) | **POST** /offers | Create an Offer
[**put_offers_offer_id**](OffersApi.md#put_offers_offer_id) | **PUT** /offers/{offer_id} | Update an Offer


# **delete_offers_offer_id**
> delete_offers_offer_id(x_auth_token, offer_id, content_type=content_type)

Delete an Offer

Deletes an offer by ID.

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
    api_instance = openapi_client.OffersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Delete an Offer
        api_instance.delete_offers_offer_id(x_auth_token, offer_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling OffersApi->delete_offers_offer_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers**
> OfferIndexBody get_offers(x_auth_token, page=page, per_page=per_page, order=order, search_text=search_text, sort_by=sort_by, status=status, merchant_id=merchant_id, manufacturer_id=manufacturer_id, store_id=store_id, offer_list_id=offer_list_id)

List all Offers

Search for offers.

### Example


```python
import openapi_client
from openapi_client.models.offer_index_body import OfferIndexBody
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
    api_instance = openapi_client.OffersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    search_text = 'search_text_example' # str | Attempts to match by name or id (optional)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    status = 'status_example' # str | search for records matching the desired status (optional)
    merchant_id = 56 # int | search for records with a matching merchant ID (optional)
    manufacturer_id = 56 # int | search for records with a matching manufacturer ID (optional)
    store_id = 56 # int | search for records with a matching store ID (optional)
    offer_list_id = None # List[object] | search for records with a matching offer list ID (optional)

    try:
        # List all Offers
        api_response = api_instance.get_offers(x_auth_token, page=page, per_page=per_page, order=order, search_text=search_text, sort_by=sort_by, status=status, merchant_id=merchant_id, manufacturer_id=manufacturer_id, store_id=store_id, offer_list_id=offer_list_id)
        print("The response of OffersApi->get_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->get_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]
 **search_text** | **str**| Attempts to match by name or id | [optional] 
 **sort_by** | **str**| sort records by a field name | [optional] 
 **status** | **str**| search for records matching the desired status | [optional] 
 **merchant_id** | **int**| search for records with a matching merchant ID | [optional] 
 **manufacturer_id** | **int**| search for records with a matching manufacturer ID | [optional] 
 **store_id** | **int**| search for records with a matching store ID | [optional] 
 **offer_list_id** | [**List[object]**](object.md)| search for records with a matching offer list ID | [optional] 

### Return type

[**OfferIndexBody**](OfferIndexBody.md)

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

# **get_offers_offer_id**
> Offer get_offers_offer_id(x_auth_token, offer_id, content_type=content_type, offer_request=offer_request)

Find an Offer

Finds an offer by the ID.

### Example


```python
import openapi_client
from openapi_client.models.offer import Offer
from openapi_client.models.offer_request import OfferRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_request = openapi_client.OfferRequest() # OfferRequest |  (optional)

    try:
        # Find an Offer
        api_response = api_instance.get_offers_offer_id(x_auth_token, offer_id, content_type=content_type, offer_request=offer_request)
        print("The response of OffersApi->get_offers_offer_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->get_offers_offer_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_request** | [**OfferRequest**](OfferRequest.md)|  | [optional] 

### Return type

[**Offer**](Offer.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_offers**
> Offer post_offers(x_auth_token, content_type=content_type, offer_request=offer_request)

Create an Offer

Creates an offer.
redemption_grace_period is the grace period provided for generating and redeeming codes. 
If not provided. The default will be the related Campaign's End Date.
If not provided however a grace period exists on the Campaign. The grace period will be the Campaign End Date + Campaign Grace Period Days.

In all cases, the Campaign End Date or Offer End Date - which ever occurs first - plus any applicable grace period days.

(ex: You cannot set a campaign end date beyond the offer expiration date. In this case it will follow the offer expiration date)

### Example


```python
import openapi_client
from openapi_client.models.offer import Offer
from openapi_client.models.offer_request import OfferRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    offer_request = openapi_client.OfferRequest() # OfferRequest |  (optional)

    try:
        # Create an Offer
        api_response = api_instance.post_offers(x_auth_token, content_type=content_type, offer_request=offer_request)
        print("The response of OffersApi->post_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->post_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **offer_request** | [**OfferRequest**](OfferRequest.md)|  | [optional] 

### Return type

[**Offer**](Offer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**400** | Example response |  -  |
**401** | Unauthorized |  -  |
**422** | Example response |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_offers_offer_id**
> Offer put_offers_offer_id(x_auth_token, offer_id, content_type=content_type, offer_request=offer_request)

Update an Offer

Updates an offer by ID.

### Example


```python
import openapi_client
from openapi_client.models.offer import Offer
from openapi_client.models.offer_request import OfferRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_request = openapi_client.OfferRequest() # OfferRequest |  (optional)

    try:
        # Update an Offer
        api_response = api_instance.put_offers_offer_id(x_auth_token, offer_id, content_type=content_type, offer_request=offer_request)
        print("The response of OffersApi->put_offers_offer_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->put_offers_offer_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_request** | [**OfferRequest**](OfferRequest.md)|  | [optional] 

### Return type

[**Offer**](Offer.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

