# sparkfly.EmailOptInApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_optins**](EmailOptInApi.md#post_optins) | **POST** /optins | Email Opt In


# **post_optins**
> EmailOptIn post_optins(address, xid, content_type=content_type, code=code)

Email Opt In

Email opt in with an address, xid, and code.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.email_opt_in import EmailOptIn
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
    api_instance = sparkfly.EmailOptInApi(api_client)
    address = 'address_example' # str | email address for email opt in
    xid = 'xid_example' # str | xid for email opt in
    content_type = 'content_type_example' # str | application/json (optional)
    code = 'code_example' # str | code for email opt in (optional)

    try:
        # Email Opt In
        api_response = await api_instance.post_optins(address, xid, content_type=content_type, code=code)
        print("The response of EmailOptInApi->post_optins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailOptInApi->post_optins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| email address for email opt in | 
 **xid** | **str**| xid for email opt in | 
 **content_type** | **str**| application/json | [optional] 
 **code** | **str**| code for email opt in | [optional] 

### Return type

[**EmailOptIn**](EmailOptIn.md)

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
**422** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

