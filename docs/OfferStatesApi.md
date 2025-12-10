# sparkfly.OfferStatesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_member_offer_states_issue**](OfferStatesApi.md#create_member_offer_states_issue) | **POST** /members/offer_states/issue | Issue an Offer to a member (high throughput)
[**create_member_offer_states_void**](OfferStatesApi.md#create_member_offer_states_void) | **POST** /members/{member_id}/offer_states/{offerstate_id}/void | Void Offer State
[**create_member_offer_states_voidmember_identifierentifier**](OfferStatesApi.md#create_member_offer_states_voidmember_identifierentifier) | **POST** /members/offer_states/{offerstate_id}/void | Void Offer State by Member Identifier
[**create_offer_state**](OfferStatesApi.md#create_offer_state) | **POST** /members/offer_states | Create Offer State from Query Parameters
[**get_offer_state**](OfferStatesApi.md#get_offer_state) | **GET** /members/{member_id}/offer_states/{offerstate_id} | Get Offer State by Offer State ID
[**issue_offer_state**](OfferStatesApi.md#issue_offer_state) | **POST** /members/{member_id}/offer_states | Create Offer State
[**list_members_offers**](OfferStatesApi.md#list_members_offers) | **GET** /members/{member_id}/offers/{offer_id} | Get Offer State by Offer ID
[**list_offer_states**](OfferStatesApi.md#list_offer_states) | **GET** /members/{member_id}/offer_states | Get all Offer States
[**query_offer_states**](OfferStatesApi.md#query_offer_states) | **GET** /members/offer_states | Get Offer State from Query Parameters
[**redeem_offer_state**](OfferStatesApi.md#redeem_offer_state) | **POST** /members/{member_id}/offer_states/{offerstate_id} | Update Offer State - Post
[**update_offer_state**](OfferStatesApi.md#update_offer_state) | **PUT** /members/{member_id}/offer_states/{offerstate_id} | Update Offer State


# **create_member_offer_states_issue**
> CreateMemberOfferStatesIssue201Response create_member_offer_states_issue(create_member_offer_states_issue_request=create_member_offer_states_issue_request)

Issue an Offer to a member (high throughput)

Issues an offer to a member using an active Sparkfly campaign, optionally allowing attachment of external data, activation and expiration dates. An issued offer is referred to as an offer_state.

This endpoint provides a limited feature set aimed at high throughput offer issuance. This endpoint should be preferred when issuing offer_states to a large number of members.


### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.create_member_offer_states_issue201_response import CreateMemberOfferStatesIssue201Response
from sparkfly.models.create_member_offer_states_issue_request import CreateMemberOfferStatesIssueRequest
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    create_member_offer_states_issue_request = sparkfly.CreateMemberOfferStatesIssueRequest() # CreateMemberOfferStatesIssueRequest |  (optional)

    try:
        # Issue an Offer to a member (high throughput)
        api_response = await api_instance.create_member_offer_states_issue(create_member_offer_states_issue_request=create_member_offer_states_issue_request)
        print("The response of OfferStatesApi->create_member_offer_states_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->create_member_offer_states_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_member_offer_states_issue_request** | [**CreateMemberOfferStatesIssueRequest**](CreateMemberOfferStatesIssueRequest.md)|  | [optional] 

### Return type

[**CreateMemberOfferStatesIssue201Response**](CreateMemberOfferStatesIssue201Response.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_member_offer_states_void**
> create_member_offer_states_void(member_id, offerstate_id)

Void Offer State

Voids an offer state from an offer state ID.

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
    api_instance = sparkfly.OfferStatesApi(api_client)
    member_id = 'member_id_example' # str | The member's primary key
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key

    try:
        # Void Offer State
        await api_instance.create_member_offer_states_void(member_id, offerstate_id)
    except Exception as e:
        print("Exception when calling OfferStatesApi->create_member_offer_states_void: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member&#39;s primary key | 
 **offerstate_id** | **str**| The offer state&#39;s primary key | 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

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

# **create_member_offer_states_voidmember_identifierentifier**
> create_member_offer_states_voidmember_identifierentifier(offerstate_id, member_identifier=member_identifier)

Void Offer State by Member Identifier

Voids an offer state by the member identifier.

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
    api_instance = sparkfly.OfferStatesApi(api_client)
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_identifier = 'member_identifier_example' # str | the member identifier attached to a member (optional)

    try:
        # Void Offer State by Member Identifier
        await api_instance.create_member_offer_states_voidmember_identifierentifier(offerstate_id, member_identifier=member_identifier)
    except Exception as e:
        print("Exception when calling OfferStatesApi->create_member_offer_states_voidmember_identifierentifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_identifier** | **str**| the member identifier attached to a member | [optional] 

### Return type

void (empty response body)

### Authorization

[XAuthToken](../README.md#XAuthToken)

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

# **create_offer_state**
> OfferState create_offer_state(content_type=content_type, token=token, offer_id=offer_id, channel_id=channel_id, offer_state_request=offer_state_request)

Create Offer State from Query Parameters

Creates an offer state using the osid, offer_id or channel_id.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state import OfferState
from sparkfly.models.offer_state_request import OfferStateRequest
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | An offer state's osid (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)
    channel_id = 'channel_id_example' # str | The channel's primary key (optional)
    offer_state_request = sparkfly.OfferStateRequest() # OfferStateRequest |  (optional)

    try:
        # Create Offer State from Query Parameters
        api_response = await api_instance.create_offer_state(content_type=content_type, token=token, offer_id=offer_id, channel_id=channel_id, offer_state_request=offer_state_request)
        print("The response of OfferStatesApi->create_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->create_offer_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| An offer state&#39;s osid | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 
 **channel_id** | **str**| The channel&#39;s primary key | [optional] 
 **offer_state_request** | [**OfferStateRequest**](OfferStateRequest.md)|  | [optional] 

### Return type

[**OfferState**](OfferState.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

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

# **get_offer_state**
> OfferStateIndexBody get_offer_state(offerstate_id, member_id, content_type=content_type)

Get Offer State by Offer State ID

Gets the offer state by the offer state ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state_index_body import OfferStateIndexBody
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get Offer State by Offer State ID
        api_response = await api_instance.get_offer_state(offerstate_id, member_id, content_type=content_type)
        print("The response of OfferStatesApi->get_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->get_offer_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferStateIndexBody**](OfferStateIndexBody.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_offer_state**
> OfferState issue_offer_state(member_id, content_type=content_type, channel_id=channel_id, offer_id=offer_id, offer_state_request=offer_state_request)

Create Offer State

Creates an offer state from member, offer, and channel IDs.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state import OfferState
from sparkfly.models.offer_state_request import OfferStateRequest
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)
    channel_id = 'channel_id_example' # str | The channel's primary key (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)
    offer_state_request = sparkfly.OfferStateRequest() # OfferStateRequest |  (optional)

    try:
        # Create Offer State
        api_response = await api_instance.issue_offer_state(member_id, content_type=content_type, channel_id=channel_id, offer_id=offer_id, offer_state_request=offer_state_request)
        print("The response of OfferStatesApi->issue_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->issue_offer_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 
 **channel_id** | **str**| The channel&#39;s primary key | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 
 **offer_state_request** | [**OfferStateRequest**](OfferStateRequest.md)|  | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**403** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members_offers**
> OfferState list_members_offers(member_id, offer_id, content_type=content_type)

Get Offer State by Offer ID

Gets the offer state by the offer ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state import OfferState
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    member_id = 'member_id_example' # str | The member's primary key
    offer_id = 'offer_id_example' # str | The offer's primary key
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get Offer State by Offer ID
        api_response = await api_instance.list_members_offers(member_id, offer_id, content_type=content_type)
        print("The response of OfferStatesApi->list_members_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->list_members_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member&#39;s primary key | 
 **offer_id** | **str**| The offer&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_offer_states**
> OfferStateIndexBody list_offer_states(member_id, content_type=content_type)

Get all Offer States

Gets all offer states.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state_index_body import OfferStateIndexBody
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Get all Offer States
        api_response = await api_instance.list_offer_states(member_id, content_type=content_type)
        print("The response of OfferStatesApi->list_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->list_offer_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**OfferStateIndexBody**](OfferStateIndexBody.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offer_states**
> OfferState query_offer_states(content_type=content_type, token=token, credential_identifier=credential_identifier, external_ref_id=external_ref_id)

Get Offer State from Query Parameters

Gets an offer state from a token, credential_identifier, and/or an external_ref_id.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state import OfferState
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    token = 'token_example' # str | An offer state's osid (optional)
    credential_identifier = 'credential_identifier_example' # str | The identifier of the credential (optional)
    external_ref_id = 'external_ref_id_example' # str | An external reference id (optional)

    try:
        # Get Offer State from Query Parameters
        api_response = await api_instance.query_offer_states(content_type=content_type, token=token, credential_identifier=credential_identifier, external_ref_id=external_ref_id)
        print("The response of OfferStatesApi->query_offer_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->query_offer_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **token** | **str**| An offer state&#39;s osid | [optional] 
 **credential_identifier** | **str**| The identifier of the credential | [optional] 
 **external_ref_id** | **str**| An external reference id | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_offer_state**
> OfferState redeem_offer_state(offerstate_id, member_id, offer_state_update=offer_state_update)

Update Offer State - Post

Updates the offer state by offer state ID through a post.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state import OfferState
from sparkfly.models.offer_state_update import OfferStateUpdate
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_id = 'member_id_example' # str | The member's primary key
    offer_state_update = sparkfly.OfferStateUpdate() # OfferStateUpdate |  (optional)

    try:
        # Update Offer State - Post
        api_response = await api_instance.redeem_offer_state(offerstate_id, member_id, offer_state_update=offer_state_update)
        print("The response of OfferStatesApi->redeem_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->redeem_offer_state: %s\n" % e)
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

[XAuthToken](../README.md#XAuthToken)

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

# **update_offer_state**
> OfferState update_offer_state(offerstate_id, member_id, content_type=content_type, offer_state_update=offer_state_update)

Update Offer State

Updates an offer state by offer state ID.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.offer_state import OfferState
from sparkfly.models.offer_state_update import OfferStateUpdate
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
    api_instance = sparkfly.OfferStatesApi(api_client)
    offerstate_id = 'offerstate_id_example' # str | The offer state's primary key
    member_id = 'member_id_example' # str | The member's primary key
    content_type = 'content_type_example' # str | application/json (optional)
    offer_state_update = sparkfly.OfferStateUpdate() # OfferStateUpdate |  (optional)

    try:
        # Update Offer State
        api_response = await api_instance.update_offer_state(offerstate_id, member_id, content_type=content_type, offer_state_update=offer_state_update)
        print("The response of OfferStatesApi->update_offer_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferStatesApi->update_offer_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offerstate_id** | **str**| The offer state&#39;s primary key | 
 **member_id** | **str**| The member&#39;s primary key | 
 **content_type** | **str**| application/json | [optional] 
 **offer_state_update** | [**OfferStateUpdate**](OfferStateUpdate.md)|  | [optional] 

### Return type

[**OfferState**](OfferState.md)

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
**404** | Example response |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

