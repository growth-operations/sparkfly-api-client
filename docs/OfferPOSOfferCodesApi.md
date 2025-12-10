# sparkfly.OfferPOSOfferCodesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pos_code**](OfferPOSOfferCodesApi.md#create_pos_code) | **POST** /offers/{offer_id}/pos_offer_codes | Create an Offer POS Offer Code
[**delete_offer_pos_offer_codes**](OfferPOSOfferCodesApi.md#delete_offer_pos_offer_codes) | **DELETE** /offers/{offer_id}/pos_offer_codes/{id} | Remove an Offer POS Offer Code
[**get_offer_pos_code**](OfferPOSOfferCodesApi.md#get_offer_pos_code) | **GET** /offers/{offer_id}/pos_offer_codes/{id} | Get an Offer POS Offer Code
[**list_pos_codes**](OfferPOSOfferCodesApi.md#list_pos_codes) | **GET** /offers/{offer_id}/pos_offer_codes | List all Offer POS Offer Codes
[**update_offer_pos_offer_codes**](OfferPOSOfferCodesApi.md#update_offer_pos_offer_codes) | **PUT** /offers/{offer_id}/pos_offer_codes/{id} | Update an Offer POS Offer Code


# **create_pos_code**
> OfferPosOfferCode create_pos_code(offer_id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)

Create an Offer POS Offer Code

Creates an offer POS offer code.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_pos_offer_code import OfferPosOfferCode
from sparkfly.models.offer_pos_offer_code_request import OfferPosOfferCodeRequest
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
    api_instance = sparkfly.OfferPOSOfferCodesApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_pos_offer_code_request = sparkfly.OfferPosOfferCodeRequest() # OfferPosOfferCodeRequest |  (optional)

    try:
        # Create an Offer POS Offer Code
        api_response = await api_instance.create_pos_code(offer_id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)
        print("The response of OfferPOSOfferCodesApi->create_pos_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->create_pos_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_pos_offer_code_request** | [**OfferPosOfferCodeRequest**](OfferPosOfferCodeRequest.md)|  | [optional] 

### Return type

[**OfferPosOfferCode**](OfferPosOfferCode.md)

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

# **delete_offer_pos_offer_codes**
> delete_offer_pos_offer_codes(offer_id, id, content_type=content_type)

Remove an Offer POS Offer Code

Removes an offer POS offer Code by from it's ID.

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
    api_instance = sparkfly.OfferPOSOfferCodesApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the offer code offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Remove an Offer POS Offer Code
        await api_instance.delete_offer_pos_offer_codes(offer_id, id, content_type=content_type)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->delete_offer_pos_offer_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the offer code offer | 
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

# **get_offer_pos_code**
> OfferPosOfferCode get_offer_pos_code(offer_id, id, content_type=content_type)

Get an Offer POS Offer Code

Gets an offer POS offer code from it's ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_pos_offer_code import OfferPosOfferCode
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
    api_instance = sparkfly.OfferPOSOfferCodesApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the offer code offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get an Offer POS Offer Code
        api_response = await api_instance.get_offer_pos_code(offer_id, id, content_type=content_type)
        print("The response of OfferPOSOfferCodesApi->get_offer_pos_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->get_offer_pos_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the offer code offer | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferPosOfferCode**](OfferPosOfferCode.md)

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

# **list_pos_codes**
> OfferPosOfferCodeIndex list_pos_codes(offer_id, content_type=content_type)

List all Offer POS Offer Codes

List offer POS offer codes for an offer ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_pos_offer_code_index import OfferPosOfferCodeIndex
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
    api_instance = sparkfly.OfferPOSOfferCodesApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all Offer POS Offer Codes
        api_response = await api_instance.list_pos_codes(offer_id, content_type=content_type)
        print("The response of OfferPOSOfferCodesApi->list_pos_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->list_pos_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferPosOfferCodeIndex**](OfferPosOfferCodeIndex.md)

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

# **update_offer_pos_offer_codes**
> OfferPosOfferCode update_offer_pos_offer_codes(offer_id, id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)

Update an Offer POS Offer Code

Updates an offer POS offer code by it's ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_pos_offer_code import OfferPosOfferCode
from sparkfly.models.offer_pos_offer_code_request import OfferPosOfferCodeRequest
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
    api_instance = sparkfly.OfferPOSOfferCodesApi(api_client)
    offer_id = 'offer_id_example' # str | Primary ID of the offer
    id = 'id_example' # str | Primary ID of the offer code offer
    content_type = 'content_type_example' # str | application/json (optional)
    offer_pos_offer_code_request = sparkfly.OfferPosOfferCodeRequest() # OfferPosOfferCodeRequest |  (optional)

    try:
        # Update an Offer POS Offer Code
        api_response = await api_instance.update_offer_pos_offer_codes(offer_id, id, content_type=content_type, offer_pos_offer_code_request=offer_pos_offer_code_request)
        print("The response of OfferPOSOfferCodesApi->update_offer_pos_offer_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPOSOfferCodesApi->update_offer_pos_offer_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Primary ID of the offer | 
 **id** | **str**| Primary ID of the offer code offer | 
 **content_type** | **str**| application/json | [optional] 
 **offer_pos_offer_code_request** | [**OfferPosOfferCodeRequest**](OfferPosOfferCodeRequest.md)|  | [optional] 

### Return type

[**OfferPosOfferCode**](OfferPosOfferCode.md)

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

