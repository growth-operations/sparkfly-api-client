# openapi_client.OfferPOSOfferCodesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offers_offer_id_pos_offer_codes_id**](OfferPOSOfferCodesApi.md#delete_offers_offer_id_pos_offer_codes_id) | **DELETE** /offers/{offer_id}/pos_offer_codes/{id} | Remove an Offer POS Offer Code
[**get_offers_offer_id_pos_offer_codes**](OfferPOSOfferCodesApi.md#get_offers_offer_id_pos_offer_codes) | **GET** /offers/{offer_id}/pos_offer_codes | List all Offer POS Offer Codes
[**get_offers_offer_id_pos_offer_codes_id**](OfferPOSOfferCodesApi.md#get_offers_offer_id_pos_offer_codes_id) | **GET** /offers/{offer_id}/pos_offer_codes/{id} | Get an Offer POS Offer Code
[**post_offers_offer_id_pos_offer_codes**](OfferPOSOfferCodesApi.md#post_offers_offer_id_pos_offer_codes) | **POST** /offers/{offer_id}/pos_offer_codes | Create an Offer POS Offer Code
[**put_offers_offer_id_pos_offer_codes_id**](OfferPOSOfferCodesApi.md#put_offers_offer_id_pos_offer_codes_id) | **PUT** /offers/{offer_id}/pos_offer_codes/{id} | Update an Offer POS Offer Code


# **delete_offers_offer_id_pos_offer_codes_id**
> delete_offers_offer_id_pos_offer_codes_id(x_auth_token, offer_id, id, content_type=content_type)

Remove an Offer POS Offer Code

Removes an offer POS offer Code by from it's ID.

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
    api_instance = openapi_client.OfferPOSOfferCodesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the offer code offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove an Offer POS Offer Code
        api_instance.delete_offers_offer_id_pos_offer_codes_id(x_auth_token, offer_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->delete_offers_offer_id_pos_offer_codes_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the offer code offer | 
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

# **get_offers_offer_id_pos_offer_codes**
> OfferPosOfferCodeIndex get_offers_offer_id_pos_offer_codes(x_auth_token, offer_id, content_type=content_type)

List all Offer POS Offer Codes

List offer POS offer codes for an offer ID.

### Example


```python
import openapi_client
from openapi_client.models.offer_pos_offer_code_index import OfferPosOfferCodeIndex
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
    api_instance = openapi_client.OfferPOSOfferCodesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all Offer POS Offer Codes
        api_response = api_instance.get_offers_offer_id_pos_offer_codes(x_auth_token, offer_id, content_type=content_type)
        print("The response of OfferPOSOfferCodesApi->get_offers_offer_id_pos_offer_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->get_offers_offer_id_pos_offer_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferPosOfferCodeIndex**](OfferPosOfferCodeIndex.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers_offer_id_pos_offer_codes_id**
> OfferPosOfferCode get_offers_offer_id_pos_offer_codes_id(x_auth_token, offer_id, id, content_type=content_type)

Get an Offer POS Offer Code

Gets an offer POS offer code from it's ID.

### Example


```python
import openapi_client
from openapi_client.models.offer_pos_offer_code import OfferPosOfferCode
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
    api_instance = openapi_client.OfferPOSOfferCodesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the offer code offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get an Offer POS Offer Code
        api_response = api_instance.get_offers_offer_id_pos_offer_codes_id(x_auth_token, offer_id, id, content_type=content_type)
        print("The response of OfferPOSOfferCodesApi->get_offers_offer_id_pos_offer_codes_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->get_offers_offer_id_pos_offer_codes_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the offer code offer | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferPosOfferCode**](OfferPosOfferCode.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_offers_offer_id_pos_offer_codes**
> OfferPosOfferCode post_offers_offer_id_pos_offer_codes(x_auth_token, offer_id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)

Create an Offer POS Offer Code

Creates an offer POS offer code.

### Example


```python
import openapi_client
from openapi_client.models.offer_pos_offer_code import OfferPosOfferCode
from openapi_client.models.offer_pos_offer_code_request import OfferPosOfferCodeRequest
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
    api_instance = openapi_client.OfferPOSOfferCodesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_pos_offer_code_request = openapi_client.OfferPosOfferCodeRequest() # OfferPosOfferCodeRequest |  (optional)

    try:
        # Create an Offer POS Offer Code
        api_response = api_instance.post_offers_offer_id_pos_offer_codes(x_auth_token, offer_id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)
        print("The response of OfferPOSOfferCodesApi->post_offers_offer_id_pos_offer_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->post_offers_offer_id_pos_offer_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_pos_offer_code_request** | [**OfferPosOfferCodeRequest**](OfferPosOfferCodeRequest.md)|  | [optional] 

### Return type

[**OfferPosOfferCode**](OfferPosOfferCode.md)

### Authorization

No authorization required

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

# **put_offers_offer_id_pos_offer_codes_id**
> OfferPosOfferCode put_offers_offer_id_pos_offer_codes_id(x_auth_token, offer_id, id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)

Update an Offer POS Offer Code

Updates an offer POS offer code by it's ID.

### Example


```python
import openapi_client
from openapi_client.models.offer_pos_offer_code import OfferPosOfferCode
from openapi_client.models.offer_pos_offer_code_request import OfferPosOfferCodeRequest
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
    api_instance = openapi_client.OfferPOSOfferCodesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the offer code offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_pos_offer_code_request = openapi_client.OfferPosOfferCodeRequest() # OfferPosOfferCodeRequest |  (optional)

    try:
        # Update an Offer POS Offer Code
        api_response = api_instance.put_offers_offer_id_pos_offer_codes_id(x_auth_token, offer_id, id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)
        print("The response of OfferPOSOfferCodesApi->put_offers_offer_id_pos_offer_codes_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->put_offers_offer_id_pos_offer_codes_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the offer code offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_pos_offer_code_request** | [**OfferPosOfferCodeRequest**](OfferPosOfferCodeRequest.md)|  | [optional] 

### Return type

[**OfferPosOfferCode**](OfferPosOfferCode.md)

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

