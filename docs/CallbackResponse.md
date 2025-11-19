# CallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**Callback**](Callback.md) |  | 

## Example

```python
from sparkfly.models.callback_response import CallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackResponse from a JSON string
callback_response_instance = CallbackResponse.from_json(json)
# print the JSON string representation of the object
print(CallbackResponse.to_json())

# convert the object into a dict
callback_response_dict = callback_response_instance.to_dict()
# create an instance of CallbackResponse from a dict
callback_response_from_dict = CallbackResponse.from_dict(callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


