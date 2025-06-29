# openapi_client.ImpressionsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_impressions_id**](ImpressionsApi.md#delete_impressions_id) | **DELETE** /impressions/{id} | Delete an Impression
[**get_impressions**](ImpressionsApi.md#get_impressions) | **GET** /impressions | List Impressions
[**post_impressions**](ImpressionsApi.md#post_impressions) | **POST** /impressions | Create an Impression


# **delete_impressions_id**
> delete_impressions_id(id, content_type=content_type)

Delete an Impression

Deletes an impression.

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
    api_instance = openapi_client.ImpressionsApi(api_client)
    id = 'id_example' # str | primary id for impressions
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Delete an Impression
        api_instance.delete_impressions_id(id, content_type=content_type)
    except Exception as e:
        print("Exception when calling ImpressionsApi->delete_impressions_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| primary id for impressions | 
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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_impressions**
> ImpressionIndexBody get_impressions(content_type=content_type)

List Impressions

List impressions.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.impression_index_body import ImpressionIndexBody
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
    api_instance = openapi_client.ImpressionsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List Impressions
        api_response = api_instance.get_impressions(content_type=content_type)
        print("The response of ImpressionsApi->get_impressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImpressionsApi->get_impressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 

### Return type

[**ImpressionIndexBody**](ImpressionIndexBody.md)

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
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_impressions**
> Impression post_impressions(content_type=content_type, impression_request=impression_request)

Create an Impression

Creates an impression.

### Example

* Api Key Authentication (XAuthToken):

```python
import openapi_client
from openapi_client.models.impression import Impression
from openapi_client.models.impression_request import ImpressionRequest
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
    api_instance = openapi_client.ImpressionsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    impression_request = openapi_client.ImpressionRequest() # ImpressionRequest |  (optional)

    try:
        # Create an Impression
        api_response = api_instance.post_impressions(content_type=content_type, impression_request=impression_request)
        print("The response of ImpressionsApi->post_impressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImpressionsApi->post_impressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **impression_request** | [**ImpressionRequest**](ImpressionRequest.md)|  | [optional] 

### Return type

[**Impression**](Impression.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

