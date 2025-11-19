# SubscriptionRequestSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_id** | **int** | ID of the callback this subscription is associated with | 
**external_id** | **str** | External identifier for the subscription | 
**enabled** | **bool** | Whether the subscription is enabled | [optional] [default to True]
**event** | **str** | The event type to subscribe to | 

## Example

```python
from sparkfly.models.subscription_request_subscription import SubscriptionRequestSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequestSubscription from a JSON string
subscription_request_subscription_instance = SubscriptionRequestSubscription.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequestSubscription.to_json())

# convert the object into a dict
subscription_request_subscription_dict = subscription_request_subscription_instance.to_dict()
# create an instance of SubscriptionRequestSubscription from a dict
subscription_request_subscription_from_dict = SubscriptionRequestSubscription.from_dict(subscription_request_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


