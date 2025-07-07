# sparkfly_api_client.CampaignsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /campaigns/{campaign_id} | Retrieve a Campaign by Campaign ID
[**get_campaign_external_id**](CampaignsApi.md#get_campaign_external_id) | **GET** /campaigns | Retrieve a Campaign by External ID and Offer ID
[**get_campaign_tags**](CampaignsApi.md#get_campaign_tags) | **GET** /campaigns/tags | Retrieve Campaign Tags
[**post_campaign**](CampaignsApi.md#post_campaign) | **POST** /campaigns | Create a Campaign
[**put_campaign**](CampaignsApi.md#put_campaign) | **PUT** /campaigns/{campaign_id} | Update a Campaign by Campaign ID
[**put_campaigns_campaign_id_actions_approve**](CampaignsApi.md#put_campaigns_campaign_id_actions_approve) | **PUT** /campaigns/{campaign_id}/actions/{action} | Set a Campaign&#39;s Status


# **get_campaign**
> CampaignResponse get_campaign(campaign_id)

Retrieve a Campaign by Campaign ID

Retrieves a campaign.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.campaign_response import CampaignResponse
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
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
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | search for records with a matching campaign ID

    try:
        # Retrieve a Campaign by Campaign ID
        api_response = await api_instance.get_campaign(campaign_id)
        print("The response of CampaignsApi->get_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| search for records with a matching campaign ID | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

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
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_external_id**
> CampaignResponse get_campaign_external_id(external_id=external_id, offer_id=offer_id)

Retrieve a Campaign by External ID and Offer ID

Retrieve a campaign.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.campaign_response import CampaignResponse
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
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
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.CampaignsApi(api_client)
    external_id = 'external_id_example' # str | search for records with a matching external ID (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)

    try:
        # Retrieve a Campaign by External ID and Offer ID
        api_response = await api_instance.get_campaign_external_id(external_id=external_id, offer_id=offer_id)
        print("The response of CampaignsApi->get_campaign_external_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign_external_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| search for records with a matching external ID | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 

### Return type

[**CampaignResponse**](CampaignResponse.md)

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
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_tags**
> CampaignTagsResponse get_campaign_tags()

Retrieve Campaign Tags

Retrieve campaign tags.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.campaign_tags_response import CampaignTagsResponse
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
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
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.CampaignsApi(api_client)

    try:
        # Retrieve Campaign Tags
        api_response = await api_instance.get_campaign_tags()
        print("The response of CampaignsApi->get_campaign_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CampaignTagsResponse**](CampaignTagsResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_campaign**
> CampaignResponse post_campaign(campaign_request=campaign_request)

Create a Campaign

Creates a campaign.

redemption_grace_period is the grace period provided for generating and redeeming codes. 
If not provided. The default will be the related Campaign's End Date.
If not provided however a grace period exists on the Campaign. The grace period will be the Campaign End Date + Campaign Grace Period Days.

If the grace period exists on the Offer but is not defined in the campaign. The grace period will be the Campaign End Date + Offer Grace Period Days = Code Redemption Expiration Date.
IF the grace period exists on the Offer and IS defined in the campaign, then the grace period will be Campaign End Date + Campaign Grace Period Days = Code Redemption Expiration Date.

In all cases, the Campaign End Date or Offer End Date - which ever occurs first - plus any applicable grace period days.

(ex: You cannot set a campaign end date beyond the offer expiration date. In this case it will follow the offer expiration date)

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.campaign_request import CampaignRequest
from sparkfly_api_client.models.campaign_response import CampaignResponse
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
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
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.CampaignsApi(api_client)
    campaign_request = sparkfly_api_client.CampaignRequest() # CampaignRequest |  (optional)

    try:
        # Create a Campaign
        api_response = await api_instance.post_campaign(campaign_request=campaign_request)
        print("The response of CampaignsApi->post_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->post_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)|  | [optional] 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_campaign**
> CampaignResponse put_campaign(campaign_id, campaign_request=campaign_request)

Update a Campaign by Campaign ID

Updates a campaign.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.campaign_request import CampaignRequest
from sparkfly_api_client.models.campaign_response import CampaignResponse
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
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
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | search for records with a matching campaign ID
    campaign_request = sparkfly_api_client.CampaignRequest() # CampaignRequest |  (optional)

    try:
        # Update a Campaign by Campaign ID
        api_response = await api_instance.put_campaign(campaign_id, campaign_request=campaign_request)
        print("The response of CampaignsApi->put_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->put_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| search for records with a matching campaign ID | 
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)|  | [optional] 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_campaigns_campaign_id_actions_approve**
> CampaignResponse put_campaigns_campaign_id_actions_approve(campaign_id, action)

Set a Campaign's Status

Set the status of a currently pending or suspended campaign to active.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.campaign_response import CampaignResponse
from sparkfly_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-staging.sparkfly.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = sparkfly_api_client.Configuration(
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
async with sparkfly_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparkfly_api_client.CampaignsApi(api_client)
    campaign_id = 56 # int | primary identifier of the campaign
    action = 'action_example' # str | desired status of the campaign

    try:
        # Set a Campaign's Status
        api_response = await api_instance.put_campaigns_campaign_id_actions_approve(campaign_id, action)
        print("The response of CampaignsApi->put_campaigns_campaign_id_actions_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->put_campaigns_campaign_id_actions_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| primary identifier of the campaign | 
 **action** | **str**| desired status of the campaign | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

