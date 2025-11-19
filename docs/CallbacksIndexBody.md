# CallbacksIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**callbacks** | [**List[CallbackResponse]**](CallbackResponse.md) |  | [optional] 

## Example

```python
from sparkfly.models.callbacks_index_body import CallbacksIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of CallbacksIndexBody from a JSON string
callbacks_index_body_instance = CallbacksIndexBody.from_json(json)
# print the JSON string representation of the object
print(CallbacksIndexBody.to_json())

# convert the object into a dict
callbacks_index_body_dict = callbacks_index_body_instance.to_dict()
# create an instance of CallbacksIndexBody from a dict
callbacks_index_body_from_dict = CallbacksIndexBody.from_dict(callbacks_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


