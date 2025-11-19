# CallbackRequestCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to send event notifications to | 
**external_id** | **str** | External identifier for the callback | 
**enabled** | **bool** | Whether the callback is enabled | [optional] [default to True]

## Example

```python
from sparkfly.models.callback_request_callback import CallbackRequestCallback

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackRequestCallback from a JSON string
callback_request_callback_instance = CallbackRequestCallback.from_json(json)
# print the JSON string representation of the object
print(CallbackRequestCallback.to_json())

# convert the object into a dict
callback_request_callback_dict = callback_request_callback_instance.to_dict()
# create an instance of CallbackRequestCallback from a dict
callback_request_callback_from_dict = CallbackRequestCallback.from_dict(callback_request_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


