# openapi_client.BIStoreListsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_bi_store_lists**](BIStoreListsApi.md#get_merchants_bi_store_lists) | **GET** /merchants/bi_store_lists | List all BI Store Lists


# **get_merchants_bi_store_lists**
> BiStoreList get_merchants_bi_store_lists(x_auth_token, content_type=content_type)

List all BI Store Lists

List all BI Store Lists by Account ID.

### Example


```python
import openapi_client
from openapi_client.models.bi_store_list import BiStoreList
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
    api_instance = openapi_client.BIStoreListsApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # List all BI Store Lists
        api_response = api_instance.get_merchants_bi_store_lists(x_auth_token, content_type=content_type)
        print("The response of BIStoreListsApi->get_merchants_bi_store_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BIStoreListsApi->get_merchants_bi_store_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**BiStoreList**](BiStoreList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

