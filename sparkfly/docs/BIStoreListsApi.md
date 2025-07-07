# sparkfly.BIStoreListsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_bi_store_lists**](BIStoreListsApi.md#get_merchants_bi_store_lists) | **GET** /merchants/bi_store_lists | List all BI Store Lists


# **get_merchants_bi_store_lists**
> BiStoreList get_merchants_bi_store_lists(content_type=content_type)

List all BI Store Lists

List all BI Store Lists by Account ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.bi_store_list import BiStoreList
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
    api_instance = sparkfly.BIStoreListsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all BI Store Lists
        api_response = await api_instance.get_merchants_bi_store_lists(content_type=content_type)
        print("The response of BIStoreListsApi->get_merchants_bi_store_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BIStoreListsApi->get_merchants_bi_store_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 

### Return type

[**BiStoreList**](BiStoreList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

