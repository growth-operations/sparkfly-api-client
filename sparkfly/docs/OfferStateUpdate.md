# OfferStateUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state** | [**OfferStateUpdateOfferState**](OfferStateUpdateOfferState.md) |  | [optional] 

## Example

```python
from sparkfly.models.offer_state_update import OfferStateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateUpdate from a JSON string
offer_state_update_instance = OfferStateUpdate.from_json(json)
# print the JSON string representation of the object
print(OfferStateUpdate.to_json())

# convert the object into a dict
offer_state_update_dict = offer_state_update_instance.to_dict()
# create an instance of OfferStateUpdate from a dict
offer_state_update_from_dict = OfferStateUpdate.from_dict(offer_state_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


