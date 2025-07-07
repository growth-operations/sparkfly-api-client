# OfferStateUpdateOfferState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**offer_value_required** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**is_reward** | **bool** |  | [optional] 

## Example

```python
from sparkfly.models.offer_state_update_offer_state import OfferStateUpdateOfferState

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateUpdateOfferState from a JSON string
offer_state_update_offer_state_instance = OfferStateUpdateOfferState.from_json(json)
# print the JSON string representation of the object
print(OfferStateUpdateOfferState.to_json())

# convert the object into a dict
offer_state_update_offer_state_dict = offer_state_update_offer_state_instance.to_dict()
# create an instance of OfferStateUpdateOfferState from a dict
offer_state_update_offer_state_from_dict = OfferStateUpdateOfferState.from_dict(offer_state_update_offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


