# openapi_client.MembersApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_members_member_id**](MembersApi.md#delete_members_member_id) | **DELETE** /members/{member_id} | Remove a Member
[**get_members_member_id**](MembersApi.md#get_members_member_id) | **GET** /members/{member_id} | Find a Member
[**get_members_profile**](MembersApi.md#get_members_profile) | **GET** /members/{id}/profile | Retrieve a Member Profile
[**get_members_search**](MembersApi.md#get_members_search) | **GET** /members/search | Search for a Member
[**post_members**](MembersApi.md#post_members) | **POST** /members | Create a Member
[**post_members_profile**](MembersApi.md#post_members_profile) | **POST** /members/{id}/profile | Create/Update a Member Profile
[**put_members_member_id**](MembersApi.md#put_members_member_id) | **PUT** /members/{member_id} | Update a Member


# **delete_members_member_id**
> delete_members_member_id(x_auth_token, member_id)

Remove a Member

Attempts to delete a member.

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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    member_id = 56 # int | unique ID

    try:
        # Remove a Member
        api_instance.delete_members_member_id(x_auth_token, member_id)
    except Exception as e:
        print("Exception when calling MembersApi->delete_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **member_id** | **int**| unique ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**401** | Unauthorized |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_member_id**
> Member get_members_member_id(x_auth_token, member_id)

Find a Member

Find a particular member by its' Sparkfly ID.

### Example


```python
import openapi_client
from openapi_client.models.member import Member
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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    member_id = 56 # int | unique ID

    try:
        # Find a Member
        api_response = api_instance.get_members_member_id(x_auth_token, member_id)
        print("The response of MembersApi->get_members_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->get_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **member_id** | **int**| unique ID | 

### Return type

[**Member**](Member.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_profile**
> InlineObject5 get_members_profile(x_auth_token, id)

Retrieve a Member Profile

Get a member's profile data. If the caller's Sparkfly account is configured to store profile data on a remote platform, this call may communicate with that platform to service the request. If no member profile provider is configured within Sparkfly, an error will be returned.

### Example


```python
import openapi_client
from openapi_client.models.inline_object5 import InlineObject5
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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    id = 56 # int | The member ID that represents the member.

    try:
        # Retrieve a Member Profile
        api_response = api_instance.get_members_profile(x_auth_token, id)
        print("The response of MembersApi->get_members_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->get_members_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **id** | **int**| The member ID that represents the member. | 

### Return type

[**InlineObject5**](InlineObject5.md)

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
**403** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_search**
> Member get_members_search(x_auth_token, identifier)

Search for a Member

Performs a search of an already existing member using the identifier.

### Example


```python
import openapi_client
from openapi_client.models.member import Member
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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    identifier = 'identifier_example' # str | unique member identifier

    try:
        # Search for a Member
        api_response = api_instance.get_members_search(x_auth_token, identifier)
        print("The response of MembersApi->get_members_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->get_members_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **identifier** | **str**| unique member identifier | 

### Return type

[**Member**](Member.md)

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
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members**
> Member post_members(x_auth_token, content_type=content_type, member_request=member_request)

Create a Member

Create a new member.

### Example


```python
import openapi_client
from openapi_client.models.member import Member
from openapi_client.models.member_request import MemberRequest
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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    member_request = openapi_client.MemberRequest() # MemberRequest |  (optional)

    try:
        # Create a Member
        api_response = api_instance.post_members(x_auth_token, content_type=content_type, member_request=member_request)
        print("The response of MembersApi->post_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->post_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **member_request** | [**MemberRequest**](MemberRequest.md)|  | [optional] 

### Return type

[**Member**](Member.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**400** | Example response |  -  |
**401** | Unauthorized |  -  |
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_profile**
> post_members_profile(x_auth_token, id, content_type=content_type, post_members_profile_request=post_members_profile_request)

Create/Update a Member Profile

Creates or updates a member's profile. If Sparkfly account is configured to store profile data on a remote platform, this call may communicate with that platform to service the request. If no member profile provider is configured within Sparkfly, an error will be returned.

### Example


```python
import openapi_client
from openapi_client.models.post_members_profile_request import PostMembersProfileRequest
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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    id = 56 # int | The member ID that represents the member.
    content_type = 'content_type_example' # str | application/json (optional)
    post_members_profile_request = openapi_client.PostMembersProfileRequest() # PostMembersProfileRequest |  (optional)

    try:
        # Create/Update a Member Profile
        api_instance.post_members_profile(x_auth_token, id, content_type=content_type, post_members_profile_request=post_members_profile_request)
    except Exception as e:
        print("Exception when calling MembersApi->post_members_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **id** | **int**| The member ID that represents the member. | 
 **content_type** | **str**| application/json | [optional] 
 **post_members_profile_request** | [**PostMembersProfileRequest**](PostMembersProfileRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**403** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_member_id**
> Member put_members_member_id(x_auth_token, member_id, content_type=content_type)

Update a Member

Update a member's data.

### Example


```python
import openapi_client
from openapi_client.models.member import Member
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
    api_instance = openapi_client.MembersApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    member_id = 56 # int | unique ID
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Update a Member
        api_response = api_instance.put_members_member_id(x_auth_token, member_id, content_type=content_type)
        print("The response of MembersApi->put_members_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->put_members_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **member_id** | **int**| unique ID | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**Member**](Member.md)

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
**422** | Example response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

