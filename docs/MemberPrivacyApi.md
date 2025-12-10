# sparkfly.MemberPrivacyApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_member_privacy**](MemberPrivacyApi.md#export_member_privacy) | **GET** /privacy/member/export | Exports Data Associated with a Member
[**request_member_deletion**](MemberPrivacyApi.md#request_member_deletion) | **POST** /privacy/member/delete_request | Creates a Deletion Request for a Member


# **export_member_privacy**
> MemberPrivacy export_member_privacy(content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)

Exports Data Associated with a Member

Looks up and exports data for the member associated with the provided member_identifier or credential_identifier query parameter.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.member_privacy import MemberPrivacy
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
    api_instance = sparkfly.MemberPrivacyApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    member_identifier = 'member_identifier_example' # str | the member identifier attached to a member (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)

    try:
        # Exports Data Associated with a Member
        api_response = await api_instance.export_member_privacy(content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)
        print("The response of MemberPrivacyApi->export_member_privacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPrivacyApi->export_member_privacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **member_identifier** | **str**| the member identifier attached to a member | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 

### Return type

[**MemberPrivacy**](MemberPrivacy.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**401** | Unauthorized |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_member_deletion**
> request_member_deletion(content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)

Creates a Deletion Request for a Member

Looks up and creates a deletion request for the member associated with the provided member_identifier or credential_identifier query parameter. For each deletion request, all member offers will first be voided, then after 7 days, or longer if specified in an Account's preferences, the member will be anonymized.

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
    api_instance = sparkfly.MemberPrivacyApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    member_identifier = 'member_identifier_example' # str | the member identifier attached to a member (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)

    try:
        # Creates a Deletion Request for a Member
        await api_instance.request_member_deletion(content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)
    except Exception as e:
        print("Exception when calling MemberPrivacyApi->request_member_deletion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **member_identifier** | **str**| the member identifier attached to a member | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 

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
**200** | Successfully created a member deletion request |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity (WebDAV) - Member could not be located from the member or credential identifiers |  -  |
**500** | Internal Server Error - Internal issue creating a member deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

