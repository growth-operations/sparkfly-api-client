# sparkfly.CtmApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ctm_allocate**](CtmApi.md#ctm_allocate) | **POST** /ctm/allocate/{site_id}/{credential} | CTM Allocate
[**ctm_create_member**](CtmApi.md#ctm_create_member) | **POST** /v2/ctm/members/{site_id}/{credential} | CTM Update Response
[**ctm_create_member_by_site**](CtmApi.md#ctm_create_member_by_site) | **POST** /v2/ctm/members/{site_id} | CTM Update Response
[**ctm_deallocate**](CtmApi.md#ctm_deallocate) | **POST** /ctm/deallocate/{site_id} | CTM Dealocate
[**ctm_get_custom_messages**](CtmApi.md#ctm_get_custom_messages) | **GET** /v2/ctm/customposmessages | CTM Custom Messages
[**ctm_get_member**](CtmApi.md#ctm_get_member) | **GET** /ctm/members/{site_id}/{credential} | CTM Show Response
[**ctm_get_qitems**](CtmApi.md#ctm_get_qitems) | **POST** /ctm/qitems/{site_id}/{credential} | CTM Qitems
[**ctm_get_store**](CtmApi.md#ctm_get_store) | **GET** /v2/ctm/stores | CTM Stores
[**ctm_update_member**](CtmApi.md#ctm_update_member) | **PUT** /ctm/members/{site_id}/{credential} | CTM Update Response
[**ctm_update_member_v2**](CtmApi.md#ctm_update_member_v2) | **PUT** /v2/ctm/members/{site_id}/{credential} | CTM Show Response
[**ctm_update_transaction**](CtmApi.md#ctm_update_transaction) | **PUT** /ctm/members/{site_id} | CTM Transaction Update


# **ctm_allocate**
> ctm_allocate(tran_id, term_id, site_id, credential, content_type=content_type, token=token, offer_id=offer_id)

CTM Allocate

ctm allocate

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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)

    try:
        # CTM Allocate
        await api_instance.ctm_allocate(tran_id, term_id, site_id, credential, content_type=content_type, token=token, offer_id=offer_id)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **credential** | **str**| search for records with a matching credential | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_create_member**
> ctm_create_member(tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Update Response

ctm update response

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = sparkfly.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Update Response
        await api_instance.ctm_create_member(tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_create_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **credential** | **str**| search for records with a matching credential | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_transaction_job_request** | [**CtmTransactionJobRequest**](CtmTransactionJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_create_member_by_site**
> ctm_create_member_by_site(tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Update Response

ctm update response

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = sparkfly.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Update Response
        await api_instance.ctm_create_member_by_site(tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_create_member_by_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_transaction_job_request** | [**CtmTransactionJobRequest**](CtmTransactionJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_deallocate**
> ctm_deallocate(tran_id, term_id, site_id, content_type=content_type, token=token, offer_id=offer_id, credential_identifier=credential_identifier, pos_vendor=pos_vendor)

CTM Dealocate

ctm dealocate

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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)
    pos_vendor = 'pos_vendor_example' # str | search for records with a pos vendor (optional)

    try:
        # CTM Dealocate
        await api_instance.ctm_deallocate(tran_id, term_id, site_id, content_type=content_type, token=token, offer_id=offer_id, credential_identifier=credential_identifier, pos_vendor=pos_vendor)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_deallocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 
 **pos_vendor** | **str**| search for records with a pos vendor | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_get_custom_messages**
> object ctm_get_custom_messages(content_type=content_type)

CTM Custom Messages

ctm custom messages

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
    api_instance = sparkfly.CtmApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # CTM Custom Messages
        api_response = await api_instance.ctm_get_custom_messages(content_type=content_type)
        print("The response of CtmApi->ctm_get_custom_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_get_custom_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 

### Return type

**object**

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_get_member**
> CtmTransactionShowResponse ctm_get_member(tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)

CTM Show Response

ctm show response

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_redemption_job_request import CtmRedemptionJobRequest
from sparkfly.models.ctm_transaction_show_response import CtmTransactionShowResponse
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    x_sparkfly_metadata = 'x_sparkfly_metadata_example' # str | Metadata (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    pos_version = 'pos_version_example' # str | search for records with a pos version (optional)
    pos_vendor = 'pos_vendor_example' # str | search for records with a pos vendor (optional)
    ctm_redemption_job_request = sparkfly.CtmRedemptionJobRequest() # CtmRedemptionJobRequest |  (optional)

    try:
        # CTM Show Response
        api_response = await api_instance.ctm_get_member(tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)
        print("The response of CtmApi->ctm_get_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_get_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **credential** | **str**| search for records with a matching credential | 
 **content_type** | **str**| application/json | [optional] 
 **x_sparkfly_metadata** | **str**| Metadata | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **pos_version** | **str**| search for records with a pos version | [optional] 
 **pos_vendor** | **str**| search for records with a pos vendor | [optional] 
 **ctm_redemption_job_request** | [**CtmRedemptionJobRequest**](CtmRedemptionJobRequest.md)|  | [optional] 

### Return type

[**CtmTransactionShowResponse**](CtmTransactionShowResponse.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_get_qitems**
> ctm_get_qitems(tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_qitems_request=ctm_qitems_request)

CTM Qitems

ctm qitems

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_qitems_request import CtmQitemsRequest
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_qitems_request = sparkfly.CtmQitemsRequest() # CtmQitemsRequest |  (optional)

    try:
        # CTM Qitems
        await api_instance.ctm_get_qitems(tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_qitems_request=ctm_qitems_request)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_get_qitems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **credential** | **str**| search for records with a matching credential | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_qitems_request** | [**CtmQitemsRequest**](CtmQitemsRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_get_store**
> object ctm_get_store(content_type=content_type)

CTM Stores

ctm stores

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
    api_instance = sparkfly.CtmApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # CTM Stores
        api_response = await api_instance.ctm_get_store(content_type=content_type)
        print("The response of CtmApi->ctm_get_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_get_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 

### Return type

**object**

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_update_member**
> ctm_update_member(tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Update Response

ctm update response

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = sparkfly.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Update Response
        await api_instance.ctm_update_member(tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_update_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **credential** | **str**| search for records with a matching credential | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_transaction_job_request** | [**CtmTransactionJobRequest**](CtmTransactionJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_update_member_v2**
> CtmTransactionShowResponse ctm_update_member_v2(tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)

CTM Show Response

ctm show response

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_redemption_job_request import CtmRedemptionJobRequest
from sparkfly.models.ctm_transaction_show_response import CtmTransactionShowResponse
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    x_sparkfly_metadata = 'x_sparkfly_metadata_example' # str | Metadata (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    pos_version = 'pos_version_example' # str | search for records with a pos version (optional)
    pos_vendor = 'pos_vendor_example' # str | search for records with a pos vendor (optional)
    ctm_redemption_job_request = sparkfly.CtmRedemptionJobRequest() # CtmRedemptionJobRequest |  (optional)

    try:
        # CTM Show Response
        api_response = await api_instance.ctm_update_member_v2(tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)
        print("The response of CtmApi->ctm_update_member_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_update_member_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **credential** | **str**| search for records with a matching credential | 
 **content_type** | **str**| application/json | [optional] 
 **x_sparkfly_metadata** | **str**| Metadata | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **pos_version** | **str**| search for records with a pos version | [optional] 
 **pos_vendor** | **str**| search for records with a pos vendor | [optional] 
 **ctm_redemption_job_request** | [**CtmRedemptionJobRequest**](CtmRedemptionJobRequest.md)|  | [optional] 

### Return type

[**CtmTransactionShowResponse**](CtmTransactionShowResponse.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ctm_update_transaction**
> ctm_update_transaction(tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Transaction Update

ctm transaction update

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = sparkfly.CtmApi(api_client)
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = sparkfly.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Transaction Update
        await api_instance.ctm_update_transaction(tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->ctm_update_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_transaction_job_request** | [**CtmTransactionJobRequest**](CtmTransactionJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

