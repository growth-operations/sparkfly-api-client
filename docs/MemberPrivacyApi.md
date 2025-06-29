# openapi_client.MemberPrivacyApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_privacy_member_export**](MemberPrivacyApi.md#get_privacy_member_export) | **GET** /privacy/member/export | Exports Data Associated with a Member
[**post_privacy_member_delete_request**](MemberPrivacyApi.md#post_privacy_member_delete_request) | **POST** /privacy/member/delete_request | Creates a Deletion Request for a Member


# **get_privacy_member_export**
> MemberPrivacy get_privacy_member_export(x_auth_token, content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)

Exports Data Associated with a Member

Looks up and exports data for the member associated with the provided member_identifier or credential_identifier query parameter.

### Example


```python
import openapi_client
from openapi_client.models.member_privacy import MemberPrivacy
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
    api_instance = openapi_client.MemberPrivacyApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    member_identifier = 'member_identifier_example' # str | the member identifier attached to a member (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)

    try:
        # Exports Data Associated with a Member
        api_response = api_instance.get_privacy_member_export(x_auth_token, content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)
        print("The response of MemberPrivacyApi->get_privacy_member_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPrivacyApi->get_privacy_member_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **member_identifier** | **str**| the member identifier attached to a member | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 

### Return type

[**MemberPrivacy**](MemberPrivacy.md)

### Authorization

No authorization required

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

# **post_privacy_member_delete_request**
> post_privacy_member_delete_request(x_auth_token, content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)

Creates a Deletion Request for a Member

Looks up and creates a deletion request for the member associated with the provided member_identifier or credential_identifier query parameter. For each deletion request, all member offers will first be voided, then after 7 days, or longer if specified in an Account's preferences, the member will be anonymized.

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
    api_instance = openapi_client.MemberPrivacyApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    member_identifier = 'member_identifier_example' # str | the member identifier attached to a member (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)

    try:
        # Creates a Deletion Request for a Member
        api_instance.post_privacy_member_delete_request(x_auth_token, content_type=content_type, member_identifier=member_identifier, credential_identifier=credential_identifier)
    except Exception as e:
        print("Exception when calling MemberPrivacyApi->post_privacy_member_delete_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **member_identifier** | **str**| the member identifier attached to a member | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 

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
**200** | Successfully created a member deletion request |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity (WebDAV) - Member could not be located from the member or credential identifiers |  -  |
**500** | Internal Server Error - Internal issue creating a member deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

