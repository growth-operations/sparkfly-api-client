# sparkfly.AudiencesApi

All URIs are relative to *https://api-staging.sparkfly.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audience**](AudiencesApi.md#create_audience) | **POST** /audiences | Create an Audience
[**create_sub_audience**](AudiencesApi.md#create_sub_audience) | **POST** /audiences/{audience_id}/sub_audiences | Create a Sub-Audience
[**delete_audience**](AudiencesApi.md#delete_audience) | **DELETE** /audiences/{audience_id} | Remove an Audience
[**delete_sub_audience**](AudiencesApi.md#delete_sub_audience) | **DELETE** /audiences/{audience_id}/sub_audiences/{sub_audience_id} | Remove a Sub-Audience
[**get_audience**](AudiencesApi.md#get_audience) | **GET** /audiences/{audience_id} | Retrieve an Audience
[**get_sub_audience**](AudiencesApi.md#get_sub_audience) | **GET** /audiences/{audience_id}/sub_audiences/{sub_audience_id} | Retrieve a Sub-Audience
[**list_audiences**](AudiencesApi.md#list_audiences) | **GET** /audiences | List all Audiences
[**list_sub_audiences**](AudiencesApi.md#list_sub_audiences) | **GET** /audiences/{audience_id}/sub_audiences | List all Sub-Audiences
[**update_audience**](AudiencesApi.md#update_audience) | **PUT** /audiences/{audience_id} | Update an Audience
[**update_sub_audience**](AudiencesApi.md#update_sub_audience) | **PUT** /audiences/{audience_id}/sub_audiences/{sub_audience_id} | Update a Sub-Audience


# **create_audience**
> AudienceData create_audience(content_type=content_type, create_audience_request=create_audience_request)

Create an Audience

Creates a new audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.audience_data import AudienceData
from sparkfly.models.create_audience_request import CreateAudienceRequest
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
    api_instance = sparkfly.AudiencesApi(api_client)
    content_type = 'content_type_example' # str | application/json (optional)
    create_audience_request = sparkfly.CreateAudienceRequest() # CreateAudienceRequest |  (optional)

    try:
        # Create an Audience
        api_response = await api_instance.create_audience(content_type=content_type, create_audience_request=create_audience_request)
        print("The response of AudiencesApi->create_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->create_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| application/json | [optional] 
 **create_audience_request** | [**CreateAudienceRequest**](CreateAudienceRequest.md)|  | [optional] 

### Return type

[**AudienceData**](AudienceData.md)

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

# **create_sub_audience**
> SubAudienceData create_sub_audience(audience_id, content_type=content_type, create_sub_audience_request=create_sub_audience_request)

Create a Sub-Audience

Creates a sub-audience within this audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.create_sub_audience_request import CreateSubAudienceRequest
from sparkfly.models.sub_audience_data import SubAudienceData
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
    api_instance = sparkfly.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | parent audience
    content_type = 'content_type_example' # str | application/json (optional)
    create_sub_audience_request = sparkfly.CreateSubAudienceRequest() # CreateSubAudienceRequest |  (optional)

    try:
        # Create a Sub-Audience
        api_response = await api_instance.create_sub_audience(audience_id, content_type=content_type, create_sub_audience_request=create_sub_audience_request)
        print("The response of AudiencesApi->create_sub_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->create_sub_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| parent audience | 
 **content_type** | **str**| application/json | [optional] 
 **create_sub_audience_request** | [**CreateSubAudienceRequest**](CreateSubAudienceRequest.md)|  | [optional] 

### Return type

[**SubAudienceData**](SubAudienceData.md)

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

# **delete_audience**
> delete_audience(audience_id)

Remove an Audience

Removes an existing audience.

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
    api_instance = sparkfly.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | audience to find or modify

    try:
        # Remove an Audience
        await api_instance.delete_audience(audience_id)
    except Exception as e:
        print("Exception when calling AudiencesApi->delete_audience: %s\n" % e)
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

# **delete_sub_audience**
> delete_sub_audience(sub_audience_id, audience_id)

Remove a Sub-Audience

Removes an existing sub-audience.

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
    api_instance = sparkfly.AudiencesApi(api_client)
    sub_audience_id = 'sub_audience_id_example' # str | sub-audience to find or modify
    audience_id = 'audience_id_example' # str | parent audience

    try:
        # Remove a Sub-Audience
        await api_instance.delete_sub_audience(sub_audience_id, audience_id)
    except Exception as e:
        print("Exception when calling AudiencesApi->delete_sub_audience: %s\n" % e)
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

# **get_audience**
> AudienceData get_audience(audience_id)

Retrieve an Audience

Find an audience by its primary identifier.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.audience_data import AudienceData
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
    api_instance = sparkfly.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | audience to find or modify

    try:
        # Retrieve an Audience
        api_response = await api_instance.get_audience(audience_id)
        print("The response of AudiencesApi->get_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| audience to find or modify | 

### Return type

[**AudienceData**](AudienceData.md)

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

# **get_sub_audience**
> SubAudienceData get_sub_audience(sub_audience_id, audience_id)

Retrieve a Sub-Audience

Get a sub-audience by it's primary identifier.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.sub_audience_data import SubAudienceData
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
    api_instance = sparkfly.AudiencesApi(api_client)
    sub_audience_id = 'sub_audience_id_example' # str | sub-audience to find or modify
    audience_id = 'audience_id_example' # str | parent audience

    try:
        # Retrieve a Sub-Audience
        api_response = await api_instance.get_sub_audience(sub_audience_id, audience_id)
        print("The response of AudiencesApi->get_sub_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_sub_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_audience_id** | **str**| sub-audience to find or modify | 
 **audience_id** | **str**| parent audience | 

### Return type

[**SubAudienceData**](SubAudienceData.md)

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

# **list_audiences**
> AudienceIndexBody list_audiences(page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)

List all Audiences

Retrieve all audiences associated with your account.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.audience_index_body import AudienceIndexBody
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
    api_instance = sparkfly.AudiencesApi(api_client)
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | search for records containing the text (optional)

    try:
        # List all Audiences
        api_response = await api_instance.list_audiences(page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)
        print("The response of AudiencesApi->list_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_audiences: %s\n" % e)
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

[**AudienceIndexBody**](AudienceIndexBody.md)

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

# **list_sub_audiences**
> SubAudienceIndexBody list_sub_audiences(audience_id, page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)

List all Sub-Audiences

Search within all sub-audiences.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.sub_audience_index_body import SubAudienceIndexBody
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
    api_instance = sparkfly.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | parent audience
    page = '1' # str | page offset to display a range of records from (optional) (default to '1')
    per_page = '5000' # str | maximum number of records to return in the search (optional) (default to '5000')
    order = asc # str | sort the records in either ascending (asc) or descending (desc) order (optional) (default to asc)
    sort_by = 'sort_by_example' # str | sort records by a field name (optional)
    search_text = 'search_text_example' # str | search for records containing the text (optional)

    try:
        # List all Sub-Audiences
        api_response = await api_instance.list_sub_audiences(audience_id, page=page, per_page=per_page, order=order, sort_by=sort_by, search_text=search_text)
        print("The response of AudiencesApi->list_sub_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_sub_audiences: %s\n" % e)
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

[**SubAudienceIndexBody**](SubAudienceIndexBody.md)

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

# **update_audience**
> AudienceData update_audience(audience_id, content_type=content_type, create_audience_request=create_audience_request)

Update an Audience

Updates an existing audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.audience_data import AudienceData
from sparkfly.models.create_audience_request import CreateAudienceRequest
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
    api_instance = sparkfly.AudiencesApi(api_client)
    audience_id = 'audience_id_example' # str | audience to find or modify
    content_type = 'content_type_example' # str | application/json (optional)
    create_audience_request = sparkfly.CreateAudienceRequest() # CreateAudienceRequest |  (optional)

    try:
        # Update an Audience
        api_response = await api_instance.update_audience(audience_id, content_type=content_type, create_audience_request=create_audience_request)
        print("The response of AudiencesApi->update_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->update_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| audience to find or modify | 
 **content_type** | **str**| application/json | [optional] 
 **create_audience_request** | [**CreateAudienceRequest**](CreateAudienceRequest.md)|  | [optional] 

### Return type

[**AudienceData**](AudienceData.md)

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

# **update_sub_audience**
> SubAudienceData update_sub_audience(sub_audience_id, audience_id, content_type=content_type, create_sub_audience_request=create_sub_audience_request)

Update a Sub-Audience

Updates an existing sub-audience.

### Example

* Api Key Authentication (XAuthToken):

```python
import sparkfly
from sparkfly.models.create_sub_audience_request import CreateSubAudienceRequest
from sparkfly.models.sub_audience_data import SubAudienceData
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
    api_instance = sparkfly.AudiencesApi(api_client)
    sub_audience_id = 'sub_audience_id_example' # str | sub-audience to find or modify
    audience_id = 'audience_id_example' # str | parent audience
    content_type = 'content_type_example' # str | application/json (optional)
    create_sub_audience_request = sparkfly.CreateSubAudienceRequest() # CreateSubAudienceRequest |  (optional)

    try:
        # Update a Sub-Audience
        api_response = await api_instance.update_sub_audience(sub_audience_id, audience_id, content_type=content_type, create_sub_audience_request=create_sub_audience_request)
        print("The response of AudiencesApi->update_sub_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->update_sub_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_audience_id** | **str**| sub-audience to find or modify | 
 **audience_id** | **str**| parent audience | 
 **content_type** | **str**| application/json | [optional] 
 **create_sub_audience_request** | [**CreateSubAudienceRequest**](CreateSubAudienceRequest.md)|  | [optional] 

### Return type

[**SubAudienceData**](SubAudienceData.md)

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

