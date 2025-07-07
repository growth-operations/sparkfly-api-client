# PageResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.page_response_body import PageResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponseBody from a JSON string
page_response_body_instance = PageResponseBody.from_json(json)
# print the JSON string representation of the object
print(PageResponseBody.to_json())

# convert the object into a dict
page_response_body_dict = page_response_body_instance.to_dict()
# create an instance of PageResponseBody from a dict
page_response_body_from_dict = PageResponseBody.from_dict(page_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


