# openapi_client.CtmApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ctm_custom_messages**](CtmApi.md#get_ctm_custom_messages) | **GET** /v2/ctm/customposmessages | CTM Custom Messages
[**get_ctm_store**](CtmApi.md#get_ctm_store) | **GET** /v2/ctm/stores | CTM Stores
[**get_show_ctm**](CtmApi.md#get_show_ctm) | **GET** /ctm/members/{site_id}/{credential} | CTM Show Response
[**post_allocate_ctm**](CtmApi.md#post_allocate_ctm) | **POST** /ctm/allocate/{site_id}/{credential} | CTM Allocate
[**post_deallocate_ctm**](CtmApi.md#post_deallocate_ctm) | **POST** /ctm/deallocate/{site_id} | CTM Dealocate
[**post_qitems_ctm**](CtmApi.md#post_qitems_ctm) | **POST** /ctm/qitems/{site_id}/{credential} | CTM Qitems
[**post_update_ctm**](CtmApi.md#post_update_ctm) | **POST** /v2/ctm/members/{site_id}/{credential} | CTM Update Response
[**post_update_ctm_siteid**](CtmApi.md#post_update_ctm_siteid) | **POST** /v2/ctm/members/{site_id} | CTM Update Response
[**put_show_ctm**](CtmApi.md#put_show_ctm) | **PUT** /v2/ctm/members/{site_id}/{credential} | CTM Show Response
[**put_transaction_update_ctm**](CtmApi.md#put_transaction_update_ctm) | **PUT** /ctm/members/{site_id} | CTM Transaction Update
[**put_update_ctm**](CtmApi.md#put_update_ctm) | **PUT** /ctm/members/{site_id}/{credential} | CTM Update Response


# **get_ctm_custom_messages**
> object get_ctm_custom_messages(x_auth_token, content_type=content_type)

CTM Custom Messages

ctm custom messages

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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # CTM Custom Messages
        api_response = api_instance.get_ctm_custom_messages(x_auth_token, content_type=content_type)
        print("The response of CtmApi->get_ctm_custom_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->get_ctm_custom_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ctm_store**
> object get_ctm_store(x_auth_token, content_type=content_type)

CTM Stores

ctm stores

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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # CTM Stores
        api_response = api_instance.get_ctm_store(x_auth_token, content_type=content_type)
        print("The response of CtmApi->get_ctm_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->get_ctm_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_show_ctm**
> CtmTransactionShowResponse get_show_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)

CTM Show Response

ctm show response

### Example


```python
import openapi_client
from openapi_client.models.ctm_redemption_job_request import CtmRedemptionJobRequest
from openapi_client.models.ctm_transaction_show_response import CtmTransactionShowResponse
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    x_sparkfly_metadata = 'x_sparkfly_metadata_example' # str | Metadata (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    pos_version = 'pos_version_example' # str | search for records with a pos version (optional)
    pos_vendor = 'pos_vendor_example' # str | search for records with a pos vendor (optional)
    ctm_redemption_job_request = openapi_client.CtmRedemptionJobRequest() # CtmRedemptionJobRequest |  (optional)

    try:
        # CTM Show Response
        api_response = api_instance.get_show_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)
        print("The response of CtmApi->get_show_ctm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->get_show_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **post_allocate_ctm**
> post_allocate_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, offer_id=offer_id)

CTM Allocate

ctm allocate

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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)

    try:
        # CTM Allocate
        api_instance.post_allocate_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, offer_id=offer_id)
    except Exception as e:
        print("Exception when calling CtmApi->post_allocate_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **post_deallocate_ctm**
> post_deallocate_ctm(x_auth_token, tran_id, term_id, site_id, content_type=content_type, token=token, offer_id=offer_id, credential_identifier=credential_identifier, pos_vendor=pos_vendor)

CTM Dealocate

ctm dealocate

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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
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
        api_instance.post_deallocate_ctm(x_auth_token, tran_id, term_id, site_id, content_type=content_type, token=token, offer_id=offer_id, credential_identifier=credential_identifier, pos_vendor=pos_vendor)
    except Exception as e:
        print("Exception when calling CtmApi->post_deallocate_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **post_qitems_ctm**
> post_qitems_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_qitems_request=ctm_qitems_request)

CTM Qitems

ctm qitems

### Example


```python
import openapi_client
from openapi_client.models.ctm_qitems_request import CtmQitemsRequest
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_qitems_request = openapi_client.CtmQitemsRequest() # CtmQitemsRequest |  (optional)

    try:
        # CTM Qitems
        api_instance.post_qitems_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_qitems_request=ctm_qitems_request)
    except Exception as e:
        print("Exception when calling CtmApi->post_qitems_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **post_update_ctm**
> post_update_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Update Response

ctm update response

### Example


```python
import openapi_client
from openapi_client.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = openapi_client.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Update Response
        api_instance.post_update_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->post_update_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **post_update_ctm_siteid**
> post_update_ctm_siteid(x_auth_token, tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Update Response

ctm update response

### Example


```python
import openapi_client
from openapi_client.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = openapi_client.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Update Response
        api_instance.post_update_ctm_siteid(x_auth_token, tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->post_update_ctm_siteid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_transaction_job_request** | [**CtmTransactionJobRequest**](CtmTransactionJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **put_show_ctm**
> CtmTransactionShowResponse put_show_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)

CTM Show Response

ctm show response

### Example


```python
import openapi_client
from openapi_client.models.ctm_redemption_job_request import CtmRedemptionJobRequest
from openapi_client.models.ctm_transaction_show_response import CtmTransactionShowResponse
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    x_sparkfly_metadata = 'x_sparkfly_metadata_example' # str | Metadata (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    pos_version = 'pos_version_example' # str | search for records with a pos version (optional)
    pos_vendor = 'pos_vendor_example' # str | search for records with a pos vendor (optional)
    ctm_redemption_job_request = openapi_client.CtmRedemptionJobRequest() # CtmRedemptionJobRequest |  (optional)

    try:
        # CTM Show Response
        api_response = api_instance.put_show_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, x_sparkfly_metadata=x_sparkfly_metadata, token=token, pos_version=pos_version, pos_vendor=pos_vendor, ctm_redemption_job_request=ctm_redemption_job_request)
        print("The response of CtmApi->put_show_ctm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtmApi->put_show_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

# **put_transaction_update_ctm**
> put_transaction_update_ctm(x_auth_token, tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Transaction Update

ctm transaction update

### Example


```python
import openapi_client
from openapi_client.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = openapi_client.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Transaction Update
        api_instance.put_transaction_update_ctm(x_auth_token, tran_id, term_id, site_id, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->put_transaction_update_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **tran_id** | **str**| Required transaction identifier | 
 **term_id** | **str**| Required term identifier | 
 **site_id** | **str**| search for records with a matching site id | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| search for records with a matching token | [optional] 
 **ctm_transaction_job_request** | [**CtmTransactionJobRequest**](CtmTransactionJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

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

# **put_update_ctm**
> put_update_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)

CTM Update Response

ctm update response

### Example


```python
import openapi_client
from openapi_client.models.ctm_transaction_job_request import CtmTransactionJobRequest
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
    api_instance = openapi_client.CtmApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    tran_id = 'tran_id_example' # str | Required transaction identifier
    term_id = 'term_id_example' # str | Required term identifier
    site_id = 'site_id_example' # str | search for records with a matching site id
    credential = 'credential_example' # str | search for records with a matching credential
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | search for records with a matching token (optional)
    ctm_transaction_job_request = openapi_client.CtmTransactionJobRequest() # CtmTransactionJobRequest |  (optional)

    try:
        # CTM Update Response
        api_instance.put_update_ctm(x_auth_token, tran_id, term_id, site_id, credential, content_type=content_type, token=token, ctm_transaction_job_request=ctm_transaction_job_request)
    except Exception as e:
        print("Exception when calling CtmApi->put_update_ctm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
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

No authorization required

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

