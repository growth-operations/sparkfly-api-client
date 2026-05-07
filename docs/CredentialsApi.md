# sparkfly.CredentialsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](CredentialsApi.md#create_credential) | **POST** /credentials | Create a Credential
[**search_credentials**](CredentialsApi.md#search_credentials) | **GET** /credentials | Search Credentials


# **create_credential**
> CredentialCreateResponse create_credential(content_type=content_type, credential_create_request=credential_create_request)

Create a Credential

Creates a new credential for a member, which can be used to redeem offers or participate in loyalty programs.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.credential_create_request import CredentialCreateRequest
from sparkfly.models.credential_create_response import CredentialCreateResponse
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
    api_instance = sparkfly.CredentialsApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    credential_create_request = sparkfly.CredentialCreateRequest() # CredentialCreateRequest |  (optional)

    try:
        # Create a Credential
        api_response = await api_instance.create_credential(content_type=content_type, credential_create_request=credential_create_request)
        print("The response of CredentialsApi->create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **credential_create_request** | [**CredentialCreateRequest**](CredentialCreateRequest.md)|  | [optional] 

### Return type

[**CredentialCreateResponse**](CredentialCreateResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_credentials**
> CredentialIndexBody search_credentials(identifier)

Search Credentials

Search for credentials by identifier. Returns all credentials matching the given identifier across members.
A single identifier may match multiple credentials over time (e.g., when a credential is voided and reissued
to another member). Callers should treat any credential with a non-null `voided_at` as inactive.


### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.credential_index_body import CredentialIndexBody
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
    api_instance = sparkfly.CredentialsApi(api_client)
    identifier = 'identifier_example' # str | The credential identifier to search for (e.g., a phone number, email, or external ID).

    try:
        # Search Credentials
        api_response = await api_instance.search_credentials(identifier)
        print("The response of CredentialsApi->search_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->search_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The credential identifier to search for (e.g., a phone number, email, or external ID). | 

### Return type

[**CredentialIndexBody**](CredentialIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of credentials matching the searched identifier. |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

