# sparkfly_api_client.AuthenticationApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_auth**](AuthenticationApi.md#post_auth) | **POST** /auth | Request an Authentication Token


# **post_auth**
> post_auth(x_auth_scope=x_auth_scope, x_forwarded_for=x_forwarded_for)

Request an Authentication Token

Request an authentication token that is required for most Sparkfly core API requests. An authentication token is good for 24 hours before expiring.

### Example

* Api Key Authentication (XAuthKey):
* Api Key Authentication (XAuthIdentity):

```python
import sparkfly_api_client
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
    host = "https://api-staging.sparkfly.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: XAuthKey
configuration.api_key['XAuthKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthKey'] = 'Bearer'

# Configure API key authorization: XAuthIdentity
configuration.api_key['XAuthIdentity'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['XAuthIdentity'] = 'Bearer'

# Enter a context with an instance of the API client
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.AuthenticationApi(api_client)
    x_auth_scope = 'x_auth_scope_example' # str | API scope availability for an auth token (optional)
    x_forwarded_for = 'x_forwarded_for_example' # str | Available IP address for an auth token (optional)

    try:
        # Request an Authentication Token
        await api_instance.post_auth(x_auth_scope=x_auth_scope, x_forwarded_for=x_forwarded_for)
    except Exception as e:
        print("Exception when calling AuthenticationApi->post_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_scope** | **str**| API scope availability for an auth token | [optional] 
 **x_forwarded_for** | **str**| Available IP address for an auth token | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthKey](../README.md#XAuthKey), [XAuthIdentity](../README.md#XAuthIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Authentication successful |  * X-Auth-Token - Authentication token <br>  * Cache-Control - Cache control header <br>  * Date - RFC3339 timestamp <br>  * X-Ua-Compatible - Browser compatibility <br>  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

