# openapi_client.OfferStatesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_members_member_id_offer_states**](OfferStatesApi.md#get_members_member_id_offer_states) | **GET** /members/{member_id}/offer_states | Get all Offer States
[**get_members_member_id_offer_states_offer_state_id**](OfferStatesApi.md#get_members_member_id_offer_states_offer_state_id) | **GET** /members/{member_id}/offer_states/{offerstate_id} | Get Offer State by Offer State ID
[**get_members_member_id_offers_offer_id**](OfferStatesApi.md#get_members_member_id_offers_offer_id) | **GET** /members/{member_id}/offers/{offer_id} | Get Offer State by Offer ID
[**get_members_offer_states**](OfferStatesApi.md#get_members_offer_states) | **GET** /members/offer_states | Get Offer State from Query Parameters
[**post_members_id_offer_states_issue**](OfferStatesApi.md#post_members_id_offer_states_issue) | **POST** /members/offer_states/issue | Issue an Offer to a member (high throughput)
[**post_members_member_id_offer_states**](OfferStatesApi.md#post_members_member_id_offer_states) | **POST** /members/{member_id}/offer_states | Create Offer State
[**post_members_member_id_offer_states_offerstate_id**](OfferStatesApi.md#post_members_member_id_offer_states_offerstate_id) | **POST** /members/{member_id}/offer_states/{offerstate_id} | Update Offer State - Post
[**post_members_member_id_offer_states_offerstate_id_void**](OfferStatesApi.md#post_members_member_id_offer_states_offerstate_id_void) | **POST** /members/{member_id}/offer_states/{offerstate_id}/void | Void Offer State
[**post_members_member_id_offer_states_offerstate_id_voidmember_identifier_member_identifier**](OfferStatesApi.md#post_members_member_id_offer_states_offerstate_id_voidmember_identifier_member_identifier) | **POST** /members/offer_states/{offerstate_id}/void | Void Offer State by Member Identifier
[**post_members_offer_states**](OfferStatesApi.md#post_members_offer_states) | **POST** /members/offer_states | Create Offer State from Query Parameters
[**put_members_member_id_offer_states_offer_state_id**](OfferStatesApi.md#put_members_member_id_offer_states_offer_state_id) | **PUT** /members/{member_id}/offer_states/{offerstate_id} | Update Offer State


# **get_members_member_id_offer_states**
> OfferStateIndexBody get_members_member_id_offer_states(x_auth_token, member_id, content_type=content_type)

Get all Offer States

Gets all offer states.

### Example


```python
import openapi_client
from openapi_client.models.offer_state_index_body import OfferStateIndexBody
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get all Offer States
        api_response = api_instance.get_members_member_id_offer_states(x_auth_token, member_id, content_type=content_type)
        print("The response of OfferStatesApi->get_members_member_id_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->get_members_member_id_offer_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferStateIndexBody**](OfferStateIndexBody.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_member_id_offer_states_offer_state_id**
> OfferStateIndexBody get_members_member_id_offer_states_offer_state_id(x_auth_token, offerstate_id, member_id, content_type=content_type)

Get Offer State by Offer State ID

Gets the offer state by the offer state ID.

### Example


```python
import openapi_client
from openapi_client.models.offer_state_index_body import OfferStateIndexBody
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get Offer State by Offer State ID
        api_response = api_instance.get_members_member_id_offer_states_offer_state_id(x_auth_token, offerstate_id, member_id, content_type=content_type)
        print("The response of OfferStatesApi->get_members_member_id_offer_states_offer_state_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->get_members_member_id_offer_states_offer_state_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferStateIndexBody**](OfferStateIndexBody.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_member_id_offers_offer_id**
> OfferState get_members_member_id_offers_offer_id(x_auth_token, member_id, offer_id, content_type=content_type)

Get Offer State by Offer ID

Gets the offer state by the offer ID.

### Example


```python
import openapi_client
from openapi_client.models.offer_state import OfferState
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    member_id = 'member_id_example' # str | The member's primary key
    offer_id = 'offer_id_example' # str | The offer's primary key
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get Offer State by Offer ID
        api_response = api_instance.get_members_member_id_offers_offer_id(x_auth_token, member_id, offer_id, content_type=content_type)
        print("The response of OfferStatesApi->get_members_member_id_offers_offer_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->get_members_member_id_offers_offer_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **member_id** | **str**| The member&#39;s primary key | 
 **offer_id** | **str**| The offer&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_offer_states**
> OfferState get_members_offer_states(x_auth_token, content_type=content_type, token=token, credential_identifier=credential_identifier, external_ref_id=external_ref_id)

Get Offer State from Query Parameters

Gets an offer state from a token, credential_identifier, and/or an external_ref_id.

### Example


```python
import openapi_client
from openapi_client.models.offer_state import OfferState
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | An offer state's osid (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)
    external_ref_id = 'external_ref_id_example' # str | An external reference id (optional)

    try:
        # Get Offer State from Query Parameters
        api_response = api_instance.get_members_offer_states(x_auth_token, content_type=content_type, token=token, credential_identifier=credential_identifier, external_ref_id=external_ref_id)
        print("The response of OfferStatesApi->get_members_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->get_members_offer_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| An offer state&#39;s osid | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 
 **external_ref_id** | **str**| An external reference id | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_offer_states_issue**
> PostMembersIdOfferStatesIssue201Response post_members_id_offer_states_issue(x_auth_token, post_members_id_offer_states_issue_request=post_members_id_offer_states_issue_request)

Issue an Offer to a member (high throughput)

Issues an offer to a member using an active Sparkfly campaign, optionally allowing attachment of external data, activation and expiration dates. An issued offer is referred to as an offer_state.

This endpoint provides a limited feature set aimed at high throughput offer issuance. This endpoint should be preferred when issuing offer_states to a large number of members.


### Example


```python
import openapi_client
from openapi_client.models.post_members_id_offer_states_issue201_response import PostMembersIdOfferStatesIssue201Response
from openapi_client.models.post_members_id_offer_states_issue_request import PostMembersIdOfferStatesIssueRequest
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    post_members_id_offer_states_issue_request = openapi_client.PostMembersIdOfferStatesIssueRequest() # PostMembersIdOfferStatesIssueRequest |  (optional)

    try:
        # Issue an Offer to a member (high throughput)
        api_response = api_instance.post_members_id_offer_states_issue(x_auth_token, post_members_id_offer_states_issue_request=post_members_id_offer_states_issue_request)
        print("The response of OfferStatesApi->post_members_id_offer_states_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->post_members_id_offer_states_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **post_members_id_offer_states_issue_request** | [**PostMembersIdOfferStatesIssueRequest**](PostMembersIdOfferStatesIssueRequest.md)|  | [optional] 

### Return type

[**PostMembersIdOfferStatesIssue201Response**](PostMembersIdOfferStatesIssue201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_member_id_offer_states**
> OfferState post_members_member_id_offer_states(x_auth_token, member_id, content_type=content_type, channel_id=channel_id, offer_id=offer_id)

Create Offer State

Creates an offer state from member, offer, and channel IDs.

### Example


```python
import openapi_client
from openapi_client.models.offer_state import OfferState
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)
    channel_id = 'channel_id_example' # str | The channel's primary key (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)

    try:
        # Create Offer State
        api_response = api_instance.post_members_member_id_offer_states(x_auth_token, member_id, content_type=content_type, channel_id=channel_id, offer_id=offer_id)
        print("The response of OfferStatesApi->post_members_member_id_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->post_members_member_id_offer_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 
 **channel_id** | **str**| The channel&#39;s primary key | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 

### Return type

[**OfferState**](OfferState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**401** | Unauthorized |  -  |
**403** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_member_id_offer_states_offerstate_id**
> OfferState post_members_member_id_offer_states_offerstate_id(offerstate_id, member_id, offer_state_update=offer_state_update)

Update Offer State - Post

Updates the offer state by offer state ID through a post.

### Example


```python
import openapi_client
from openapi_client.models.offer_state import OfferState
from openapi_client.models.offer_state_update import OfferStateUpdate
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_id = 'member_id_example' # str | The member's primary key
    offer_state_update = openapi_client.OfferStateUpdate() # OfferStateUpdate |  (optional)

    try:
        # Update Offer State - Post
        api_response = api_instance.post_members_member_id_offer_states_offerstate_id(offerstate_id, member_id, offer_state_update=offer_state_update)
        print("The response of OfferStatesApi->post_members_member_id_offer_states_offerstate_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->post_members_member_id_offer_states_offerstate_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_id** | **str**| The member&#39;s primary key | 
 **offer_state_update** | [**OfferStateUpdate**](OfferStateUpdate.md)|  | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_member_id_offer_states_offerstate_id_void**
> post_members_member_id_offer_states_offerstate_id_void(member_id, offerstate_id)

Void Offer State

Voids an offer state from an offer state ID.

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
    api_instance = openapi_client.OfferStatesApi(api_client)
    member_id = 'member_id_example' # str | The member's primary key
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key

    try:
        # Void Offer State
        api_instance.post_members_member_id_offer_states_offerstate_id_void(member_id, offerstate_id)
    except Exception as e:
        print("Exception when calling OfferStatesApi->post_members_member_id_offer_states_offerstate_id_void: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member&#39;s primary key | 
 **offerstate_id** | **str**| The offer state&#39;s primary key | 

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
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_member_id_offer_states_offerstate_id_voidmember_identifier_member_identifier**
> post_members_member_id_offer_states_offerstate_id_voidmember_identifier_member_identifier(offerstate_id, member_identifier=member_identifier)

Void Offer State by Member Identifier

Voids an offer state by the member identifier.

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
    api_instance = openapi_client.OfferStatesApi(api_client)
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_identifier = 'member_identifier_example' # str | the member identifier attached to a member (optional)

    try:
        # Void Offer State by Member Identifier
        api_instance.post_members_member_id_offer_states_offerstate_id_voidmember_identifier_member_identifier(offerstate_id, member_identifier=member_identifier)
    except Exception as e:
        print("Exception when calling OfferStatesApi->post_members_member_id_offer_states_offerstate_id_voidmember_identifier_member_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_identifier** | **str**| the member identifier attached to a member | [optional] 

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
**401** | Unauthorized |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_offer_states**
> OfferState post_members_offer_states(x_auth_token, content_type=content_type, token=token, offer_id=offer_id, channel_id=channel_id, offer_state_request=offer_state_request)

Create Offer State from Query Parameters

Creates an offer state using the osid, offer_id or channel_id.

### Example


```python
import openapi_client
from openapi_client.models.offer_state import OfferState
from openapi_client.models.offer_state_request import OfferStateRequest
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | An offer state's osid (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)
    channel_id = 'channel_id_example' # str | The channel's primary key (optional)
    offer_state_request = openapi_client.OfferStateRequest() # OfferStateRequest |  (optional)

    try:
        # Create Offer State from Query Parameters
        api_response = api_instance.post_members_offer_states(x_auth_token, content_type=content_type, token=token, offer_id=offer_id, channel_id=channel_id, offer_state_request=offer_state_request)
        print("The response of OfferStatesApi->post_members_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->post_members_offer_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| An offer state&#39;s osid | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 
 **channel_id** | **str**| The channel&#39;s primary key | [optional] 
 **offer_state_request** | [**OfferStateRequest**](OfferStateRequest.md)|  | [optional] 

### Return type

[**OfferState**](OfferState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_member_id_offer_states_offer_state_id**
> OfferState put_members_member_id_offer_states_offer_state_id(x_auth_token, offerstate_id, member_id, content_type=content_type, offer_state_update=offer_state_update)

Update Offer State

Updates an offer state by offer state ID.

### Example


```python
import openapi_client
from openapi_client.models.offer_state import OfferState
from openapi_client.models.offer_state_update import OfferStateUpdate
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
    api_instance = openapi_client.OfferStatesApi(api_client)
    x_auth_token = 'x_auth_token_example' # str | Required authentication token
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)
    offer_state_update = openapi_client.OfferStateUpdate() # OfferStateUpdate |  (optional)

    try:
        # Update Offer State
        api_response = api_instance.put_members_member_id_offer_states_offer_state_id(x_auth_token, offerstate_id, member_id, content_type=content_type, offer_state_update=offer_state_update)
        print("The response of OfferStatesApi->put_members_member_id_offer_states_offer_state_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->put_members_member_id_offer_states_offer_state_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_auth_token** | **str**| Required authentication token | 
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 
 **offer_state_update** | [**OfferStateUpdate**](OfferStateUpdate.md)|  | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

