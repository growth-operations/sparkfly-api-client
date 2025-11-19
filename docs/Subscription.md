# Subscription

An event subscription that links a callback to a specific event type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the subscription | [readonly] 
**callback_id** | **int** | ID of the callback this subscription is associated with | [optional] 
**external_id** | **str** | External identifier for the subscription | 
**enabled** | **bool** | Whether the subscription is enabled | 
**event** | **str** | The event type to subscribe to | 

## Example

```python
from sparkfly.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


