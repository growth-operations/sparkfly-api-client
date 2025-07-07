# sparkfly_api_client.AudiencesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_audiences_id**](AudiencesApi.md#delete_audiences_id) | **DELETE** /audiences/{audience_id} | Remove an Audience
[**delete_audiences_id_sub_audiences_sub_audience_id**](AudiencesApi.md#delete_audiences_id_sub_audiences_sub_audience_id) | **DELETE** /audiences/{audience_id}/sub_audiences/{sub_audience_id} | Remove a Sub-Audience
[**get_audiences**](AudiencesApi.md#get_audiences) | **GET** /audiences | List all Audiences
[**get_audiences_id**](AudiencesApi.md#get_audiences_id) | **GET** /audiences/{audience_id} | Retrieve an Audience
[**get_audiences_id_sub_audiences**](AudiencesApi.md#get_audiences_id_sub_audiences) | **GET** /audiences/{audience_id}/sub_audiences | List all Sub-Audiences
[**get_audiences_id_sub_audiences_sub_audience_id**](AudiencesApi.md#get_audiences_id_sub_audiences_sub_audience_id) | **GET** /audiences/{audience_id}/sub_audiences/{sub_audience_id} | Retrieve a Sub-Audience
[**post_audiences**](AudiencesApi.md#post_audiences) | **POST** /audiences | Create an Audience
[**post_audiences_id_sub_audiences**](AudiencesApi.md#post_audiences_id_sub_audiences) | **POST** /audiences/{audience_id}/sub_audiences | Create a Sub-Audience
[**put_audiences_id**](AudiencesApi.md#put_audiences_id) | **PUT** /audiences/{audience_id} | Update an Audience
[**put_audiences_id_sub_audiences_sub_audience_id**](AudiencesApi.md#put_audiences_id_sub_audiences_sub_audience_id) | **PUT** /audiences/{audience_id}/sub_audiences/{sub_audience_id} | Update a Sub-Audience


# **delete_audiences_id**
> delete_audiences_id(audience_id)

Remove an Audience

Removes an existing audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | audience to find or modify

    try:
        # Remove an Audience
        await api_instance.delete_audiences_id(audience_id)
    except Exception as e:
        print("Exception when calling AudiencesApi->delete_audiences_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| audience to find or modify | 

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
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Could not be deleted -- may be in use. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audiences_id_sub_audiences_sub_audience_id**
> delete_audiences_id_sub_audiences_sub_audience_id(sub_audience_id, audience_id)

Remove a Sub-Audience

Removes an existing sub-audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    sub_audience_id = 'sub_audience_id_example' # str | sub-audience to find or modify
    audience_id = 'audience_id_example' # str | parent audience

    try:
        # Remove a Sub-Audience
        await api_instance.delete_audiences_id_sub_audiences_sub_audience_id(sub_audience_id, audience_id)
    except Exception as e:
        print("Exception when calling AudiencesApi->delete_audiences_id_sub_audiences_sub_audience_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_audience_id** | **str**| sub-audience to find or modify | 
 **audience_id** | **str**| parent audience | 

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
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**404** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences**
> InlineObject2 get_audiences(page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)

List all Audiences

Retrieve all audiences associated with your account.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object2 import InlineObject2
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | search for records containing the text (optional)

    try:
        # List all Audiences
        api_response = await api_instance.get_audiences(page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)
        print("The response of AudiencesApi->get_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audiences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]
 **sort_by** | **str**| sort records by a field name | [optional] 
 **search_text** | **str**| search for records containing the text | [optional] 

### Return type

[**InlineObject2**](InlineObject2.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences_id**
> InlineObject1 get_audiences_id(audience_id)

Retrieve an Audience

Find an audience by its primary identifier.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object1 import InlineObject1
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | audience to find or modify

    try:
        # Retrieve an Audience
        api_response = await api_instance.get_audiences_id(audience_id)
        print("The response of AudiencesApi->get_audiences_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audiences_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| audience to find or modify | 

### Return type

[**InlineObject1**](InlineObject1.md)

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
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences_id_sub_audiences**
> InlineObject4 get_audiences_id_sub_audiences(audience_id, page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)

List all Sub-Audiences

Search within all sub-audiences.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object4 import InlineObject4
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | parent audience
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | search for records containing the text (optional)

    try:
        # List all Sub-Audiences
        api_response = await api_instance.get_audiences_id_sub_audiences(audience_id, page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)
        print("The response of AudiencesApi->get_audiences_id_sub_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audiences_id_sub_audiences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| parent audience | 
 **page** | **str**| page offset to display a range of records from | [optional] [default to &#39;1&#39;]
 **per_page** | **str**| maximum number of records to return in the search | [optional] [default to &#39;5000&#39;]
 **order** | **str**| sort the records in either ascending (asc) or descending (desc) order | [optional] [default to asc]
 **sort_by** | **str**| sort records by a field name | [optional] 
 **search_text** | **str**| search for records containing the text | [optional] 

### Return type

[**InlineObject4**](InlineObject4.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences_id_sub_audiences_sub_audience_id**
> InlineObject3 get_audiences_id_sub_audiences_sub_audience_id(sub_audience_id, audience_id)

Retrieve a Sub-Audience

Get a sub-audience by it's primary identifier.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object3 import InlineObject3
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    sub_audience_id = 'sub_audience_id_example' # str | sub-audience to find or modify
    audience_id = 'audience_id_example' # str | parent audience

    try:
        # Retrieve a Sub-Audience
        api_response = await api_instance.get_audiences_id_sub_audiences_sub_audience_id(sub_audience_id, audience_id)
        print("The response of AudiencesApi->get_audiences_id_sub_audiences_sub_audience_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audiences_id_sub_audiences_sub_audience_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_audience_id** | **str**| sub-audience to find or modify | 
 **audience_id** | **str**| parent audience | 

### Return type

[**InlineObject3**](InlineObject3.md)

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

# **post_audiences**
> InlineObject1 post_audiences(content_type=content_type, post_audiences_request=post_audiences_request)

Create an Audience

Creates a new audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object1 import InlineObject1
from sparkfly_api_client.models.post_audiences_request import PostAudiencesRequest
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    post_audiences_request = sparkfly_api_client.PostAudiencesRequest() # PostAudiencesRequest |  (optional)

    try:
        # Create an Audience
        api_response = await api_instance.post_audiences(content_type=content_type, post_audiences_request=post_audiences_request)
        print("The response of AudiencesApi->post_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->post_audiences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **post_audiences_request** | [**PostAudiencesRequest**](PostAudiencesRequest.md)|  | [optional] 

### Return type

[**InlineObject1**](InlineObject1.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**400** | Your request was malformed |  -  |
**422** | Your request was parseable, but a validation error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_audiences_id_sub_audiences**
> InlineObject3 post_audiences_id_sub_audiences(audience_id, content_type=content_type, post_audiences_id_sub_audiences_request=post_audiences_id_sub_audiences_request)

Create a Sub-Audience

Creates a sub-audience within this audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object3 import InlineObject3
from sparkfly_api_client.models.post_audiences_id_sub_audiences_request import PostAudiencesIdSubAudiencesRequest
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | parent audience
    content_type = 'content_type_example' # str | application/json (optional)
    post_audiences_id_sub_audiences_request = sparkfly_api_client.PostAudiencesIdSubAudiencesRequest() # PostAudiencesIdSubAudiencesRequest |  (optional)

    try:
        # Create a Sub-Audience
        api_response = await api_instance.post_audiences_id_sub_audiences(audience_id, content_type=content_type, post_audiences_id_sub_audiences_request=post_audiences_id_sub_audiences_request)
        print("The response of AudiencesApi->post_audiences_id_sub_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->post_audiences_id_sub_audiences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| parent audience | 
 **content_type** | **str**| application/json | [optional] 
 **post_audiences_id_sub_audiences_request** | [**PostAudiencesIdSubAudiencesRequest**](PostAudiencesIdSubAudiencesRequest.md)|  | [optional] 

### Return type

[**InlineObject3**](InlineObject3.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Example response |  -  |
**400** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_audiences_id**
> InlineObject1 put_audiences_id(audience_id, content_type=content_type, post_audiences_request=post_audiences_request)

Update an Audience

Updates an existing audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object1 import InlineObject1
from sparkfly_api_client.models.post_audiences_request import PostAudiencesRequest
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | audience to find or modify
    content_type = 'content_type_example' # str | application/json (optional)
    post_audiences_request = sparkfly_api_client.PostAudiencesRequest() # PostAudiencesRequest |  (optional)

    try:
        # Update an Audience
        api_response = await api_instance.put_audiences_id(audience_id, content_type=content_type, post_audiences_request=post_audiences_request)
        print("The response of AudiencesApi->put_audiences_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->put_audiences_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| audience to find or modify | 
 **content_type** | **str**| application/json | [optional] 
 **post_audiences_request** | [**PostAudiencesRequest**](PostAudiencesRequest.md)|  | [optional] 

### Return type

[**InlineObject1**](InlineObject1.md)

### Authorization

[XAuthToken](../README.md#XAuthToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_audiences_id_sub_audiences_sub_audience_id**
> InlineObject3 put_audiences_id_sub_audiences_sub_audience_id(sub_audience_id, audience_id, content_type=content_type, post_audiences_id_sub_audiences_request=post_audiences_id_sub_audiences_request)

Update a Sub-Audience

Updates an existing sub-audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly_api_client
from sparkfly_api_client.models.inline_object3 import InlineObject3
from sparkfly_api_client.models.post_audiences_id_sub_audiences_request import PostAudiencesIdSubAudiencesRequest
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
    api_instance = sparkfly_api_client.AudiencesApi(api_client)
    sub_audience_id = 'sub_audience_id_example' # str | sub-audience to find or modify
    audience_id = 'audience_id_example' # str | parent audience
    content_type = 'content_type_example' # str | application/json (optional)
    post_audiences_id_sub_audiences_request = sparkfly_api_client.PostAudiencesIdSubAudiencesRequest() # PostAudiencesIdSubAudiencesRequest |  (optional)

    try:
        # Update a Sub-Audience
        api_response = await api_instance.put_audiences_id_sub_audiences_sub_audience_id(sub_audience_id, audience_id, content_type=content_type, post_audiences_id_sub_audiences_request=post_audiences_id_sub_audiences_request)
        print("The response of AudiencesApi->put_audiences_id_sub_audiences_sub_audience_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->put_audiences_id_sub_audiences_sub_audience_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_audience_id** | **str**| sub-audience to find or modify | 
 **audience_id** | **str**| parent audience | 
 **content_type** | **str**| application/json | [optional] 
 **post_audiences_id_sub_audiences_request** | [**PostAudiencesIdSubAudiencesRequest**](PostAudiencesIdSubAudiencesRequest.md)|  | [optional] 

### Return type

[**InlineObject3**](InlineObject3.md)

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
**422** | An API error contains both a user friendly message as well as a trace id, which is a unique identifier for the request.  |  -  |
**500** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

