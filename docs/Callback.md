# Callback

A callback URL configuration for receiving event notifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the callback | [optional] [readonly] 
**external_id** | **str** | External identifier for the callback | [optional] 
**enabled** | **bool** | Whether the callback is enabled | [optional] 
**url** | **str** | The URL to send event notifications to | [optional] 
**last_verified_at** | **datetime** | Timestamp when the callback was last verified | [optional] [readonly] 
**signing_key** | **str** | Key used to sign webhook payloads for verification | [optional] [readonly] 
**subscriptions** | [**List[Subscription]**](Subscription.md) | List of event subscriptions associated with this callback | [optional] 

## Example

```python
from sparkfly.models.callback import Callback

# TODO update the JSON string below
json = "{}"
# create an instance of Callback from a JSON string
callback_instance = Callback.from_json(json)
# print the JSON string representation of the object
print(Callback.to_json())

# convert the object into a dict
callback_dict = callback_instance.to_dict()
# create an instance of Callback from a dict
callback_from_dict = Callback.from_dict(callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


