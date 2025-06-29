# openapi_client.POSOfferCodesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pos_offer_codes**](POSOfferCodesApi.md#get_pos_offer_codes) | **GET** /pos_offer_codes | List all POS Offer Codes
[**get_pos_offer_codes_id**](POSOfferCodesApi.md#get_pos_offer_codes_id) | **GET** /pos_offer_codes/{id} | Get a POS Offer Code


# **get_pos_offer_codes**
> PosOfferCodeIndexBody get_pos_offer_codes(content_type=content_type)

List all POS Offer Codes

List POS offer codes by account ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.pos_offer_code_index_body import PosOfferCodeIndexBody
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
    api_instance = openapi_client.POSOfferCodesApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all POS Offer Codes
        api_response = api_instance.get_pos_offer_codes(content_type=content_type)
        print("The response of POSOfferCodesApi->get_pos_offer_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POSOfferCodesApi->get_pos_offer_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 

### Return type

[**PosOfferCodeIndexBody**](PosOfferCodeIndexBody.md)

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

# **get_pos_offer_codes_id**
> PosOfferCode get_pos_offer_codes_id(id, content_type=content_type)

Get a POS Offer Code

Gets POS offer code by ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.pos_offer_code import PosOfferCode
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
    api_instance = openapi_client.POSOfferCodesApi(api_client)
    id = 56 # int | The pos offer code ID that represents the pos offer code.
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get a POS Offer Code
        api_response = api_instance.get_pos_offer_codes_id(id, content_type=content_type)
        print("The response of POSOfferCodesApi->get_pos_offer_codes_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling POSOfferCodesApi->get_pos_offer_codes_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The pos offer code ID that represents the pos offer code. | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**PosOfferCode**](PosOfferCode.md)

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
**404** | Not Found |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

