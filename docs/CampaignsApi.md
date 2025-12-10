# sparkfly.CampaignsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_campaign**](CampaignsApi.md#approve_campaign) | **PUT** /campaigns/{campaign_id}/actions/{action} | Set a Campaign&#39;s Status
[**create_campaign**](CampaignsApi.md#create_campaign) | **POST** /campaigns | Create a Campaign
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /campaigns/{campaign_id} | Retrieve a Campaign by Campaign ID
[**list_campaign_tags**](CampaignsApi.md#list_campaign_tags) | **GET** /campaigns/tags | Retrieve Campaign Tags
[**list_campaigns**](CampaignsApi.md#list_campaigns) | **GET** /campaigns | List all Campaigns
[**update_campaign**](CampaignsApi.md#update_campaign) | **PUT** /campaigns/{campaign_id} | Update a Campaign by Campaign ID


# **approve_campaign**
> CampaignResponse approve_campaign(campaign_id, action)

Set a Campaign's Status

Set the status of a currently pending or suspended campaign to active.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.campaign_response import CampaignResponse
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
    api_instance = sparkfly.CampaignsApi(api_client)
    campaign_id = 56 # int | primary identifier of the campaign
    action = 'action_example' # str | desired status of the campaign

    try:
        # Set a Campaign's Status
        api_response = await api_instance.approve_campaign(campaign_id, action)
        print("The response of CampaignsApi->approve_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->approve_campaign: %s\n" % e)
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

# **create_campaign**
> CampaignResponse create_campaign(campaign_request=campaign_request)

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
import sparkfly
from sparkfly.models.campaign_request import CampaignRequest
from sparkfly.models.campaign_response import CampaignResponse
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
    api_instance = sparkfly.CampaignsApi(api_client)
    campaign_request = sparkfly.CampaignRequest() # CampaignRequest |  (optional)

    try:
        # Create a Campaign
        api_response = await api_instance.create_campaign(campaign_request=campaign_request)
        print("The response of CampaignsApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign: %s\n" % e)
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

# **get_campaign**
> CampaignResponse get_campaign(campaign_id)

Retrieve a Campaign by Campaign ID

Retrieves a campaign.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.campaign_response import CampaignResponse
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
    api_instance = sparkfly.CampaignsApi(api_client)
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

# **list_campaign_tags**
> CampaignTagsResponse list_campaign_tags()

Retrieve Campaign Tags

Retrieve campaign tags.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.campaign_tags_response import CampaignTagsResponse
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
    api_instance = sparkfly.CampaignsApi(api_client)

    try:
        # Retrieve Campaign Tags
        api_response = await api_instance.list_campaign_tags()
        print("The response of CampaignsApi->list_campaign_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->list_campaign_tags: %s\n" % e)
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

# **list_campaigns**
> CampaignIndexBody list_campaigns(page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text, status=status, offer_id=offer_id, external_id=external_id)

List all Campaigns

Retrieve all campaigns associated with your account.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.campaign_index_body import CampaignIndexBody
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
    api_instance = sparkfly.CampaignsApi(api_client)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | search for records containing the text (optional)
    status = 'status_example' # str | search for records matching the desired status (optional)
    offer_id = 'offer_id_example' # str | search for records with a matching offer id (optional)
    external_id = 'external_id_example' # str | search for records with a matching external ID (optional)

    try:
        # List all Campaigns
        api_response = await api_instance.list_campaigns(page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text, status=status, offer_id=offer_id, external_id=external_id)
        print("The response of CampaignsApi->list_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->list_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]
 **sort_by** | **str**| sort records by a field name | [optional] 
 **search_text** | **str**| search for records containing the text | [optional] 
 **status** | **str**| search for records matching the desired status | [optional] 
 **offer_id** | **str**| search for records with a matching offer id | [optional] 
 **external_id** | **str**| search for records with a matching external ID | [optional] 

### Return type

[**CampaignIndexBody**](CampaignIndexBody.md)

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
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign**
> CampaignResponse update_campaign(campaign_id, campaign_request=campaign_request)

Update a Campaign by Campaign ID

Updates a campaign.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.campaign_request import CampaignRequest
from sparkfly.models.campaign_response import CampaignResponse
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
    api_instance = sparkfly.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | search for records with a matching campaign ID
    campaign_request = sparkfly.CampaignRequest() # CampaignRequest |  (optional)

    try:
        # Update a Campaign by Campaign ID
        api_response = await api_instance.update_campaign(campaign_id, campaign_request=campaign_request)
        print("The response of CampaignsApi->update_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaign: %s\n" % e)
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

