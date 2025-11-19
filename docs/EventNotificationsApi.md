# sparkfly.EventNotificationsApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_callback**](EventNotificationsApi.md#create_callback) | **POST** /event_notifications/callbacks | Create Callback
[**create_subscription**](EventNotificationsApi.md#create_subscription) | **POST** /event_notifications/subscriptions | Create Subscription
[**delete_callback**](EventNotificationsApi.md#delete_callback) | **DELETE** /event_notifications/callbacks/{callback_id} | Delete Callback
[**delete_subscription**](EventNotificationsApi.md#delete_subscription) | **DELETE** /event_notifications/subscriptions/{subscription_id} | Delete Subscription
[**get_callback**](EventNotificationsApi.md#get_callback) | **GET** /event_notifications/callbacks/{callback_id} | Get Callback by ID
[**get_subscription**](EventNotificationsApi.md#get_subscription) | **GET** /event_notifications/subscriptions/{subscription_id} | Get Subscription by ID
[**list_callbacks**](EventNotificationsApi.md#list_callbacks) | **GET** /event_notifications/callbacks | List Callbacks
[**list_subscriptions**](EventNotificationsApi.md#list_subscriptions) | **GET** /event_notifications/subscriptions | List Subscriptions


# **create_callback**
> CallbackResponse create_callback(callback_request, content_type=content_type)

Create Callback

Create a new callback URL configuration for receiving event notifications

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.callback_request import CallbackRequest
from sparkfly.models.callback_response import CallbackResponse
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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    callback_request = sparkfly.CallbackRequest() # CallbackRequest | 
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Create Callback
        api_response = await api_instance.create_callback(callback_request, content_type=content_type)
        print("The response of EventNotificationsApi->create_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->create_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_request** | [**CallbackRequest**](CallbackRequest.md)|  | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**CallbackResponse**](CallbackResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Callback created successfully |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> SubscriptionResponse create_subscription(subscription_request, content_type=content_type)

Create Subscription

Create a new event subscription that links a callback to a specific event type

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.subscription_request import SubscriptionRequest
from sparkfly.models.subscription_response import SubscriptionResponse
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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    subscription_request = sparkfly.SubscriptionRequest() # SubscriptionRequest | 
    content_type = 'content_type_example' # str | application/json (optional)

    try:
        # Create Subscription
        api_response = await api_instance.create_subscription(subscription_request, content_type=content_type)
        print("The response of EventNotificationsApi->create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 
 **content_type** | **str**| application/json | [optional] 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription created successfully |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_callback**
> delete_callback(callback_id)

Delete Callback

Delete a callback configuration and all associated subscriptions

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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    callback_id = 56 # int | The unique identifier of the callback

    try:
        # Delete Callback
        await api_instance.delete_callback(callback_id)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->delete_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_id** | **int**| The unique identifier of the callback | 

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
**200** | Callback deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Callback not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id)

Delete Subscription

Delete an event subscription

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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    subscription_id = 56 # int | The unique identifier of the subscription

    try:
        # Delete Subscription
        await api_instance.delete_subscription(subscription_id)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique identifier of the subscription | 

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
**200** | Subscription deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Subscription not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback**
> CallbackResponse get_callback(callback_id)

Get Callback by ID

Retrieve a specific callback configuration by its ID

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.callback_response import CallbackResponse
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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    callback_id = 56 # int | The unique identifier of the callback

    try:
        # Get Callback by ID
        api_response = await api_instance.get_callback(callback_id)
        print("The response of EventNotificationsApi->get_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->get_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_id** | **int**| The unique identifier of the callback | 

### Return type

[**CallbackResponse**](CallbackResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**404** | Callback not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> SubscriptionResponse get_subscription(subscription_id)

Get Subscription by ID

Retrieve a specific event subscription by its ID

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.subscription_response import SubscriptionResponse
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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    subscription_id = 56 # int | The unique identifier of the subscription

    try:
        # Get Subscription by ID
        api_response = await api_instance.get_subscription(subscription_id)
        print("The response of EventNotificationsApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique identifier of the subscription | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**404** | Subscription not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_callbacks**
> CallbacksIndexBody list_callbacks(page=page, per_page=per_page)

List Callbacks

Retrieve a paginated list of all callback configurations

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.callbacks_index_body import CallbacksIndexBody
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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')

    try:
        # List Callbacks
        api_response = await api_instance.list_callbacks(page=page, per_page=per_page)
        print("The response of EventNotificationsApi->list_callbacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->list_callbacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]

### Return type

[**CallbacksIndexBody**](CallbacksIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> SubscriptionsIndexBody list_subscriptions(page=page, per_page=per_page)

List Subscriptions

Retrieve a paginated list of all event subscriptions

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.subscriptions_index_body import SubscriptionsIndexBody
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
    api_instance = sparkfly.EventNotificationsApi(api_client)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')

    try:
        # List Subscriptions
        api_response = await api_instance.list_subscriptions(page=page, per_page=per_page)
        print("The response of EventNotificationsApi->list_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventNotificationsApi->list_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]

### Return type

[**SubscriptionsIndexBody**](SubscriptionsIndexBody.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

