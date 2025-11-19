# SubscriptionsIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**subscriptions** | [**List[SubscriptionResponse]**](SubscriptionResponse.md) |  | 

## Example

```python
from sparkfly.models.subscriptions_index_body import SubscriptionsIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsIndexBody from a JSON string
subscriptions_index_body_instance = SubscriptionsIndexBody.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsIndexBody.to_json())

# convert the object into a dict
subscriptions_index_body_dict = subscriptions_index_body_instance.to_dict()
# create an instance of SubscriptionsIndexBody from a dict
subscriptions_index_body_from_dict = SubscriptionsIndexBody.from_dict(subscriptions_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


