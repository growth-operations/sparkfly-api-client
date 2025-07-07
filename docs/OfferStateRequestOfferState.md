# OfferStateRequestOfferState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activates_at** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.offer_state_request_offer_state import OfferStateRequestOfferState

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateRequestOfferState from a JSON string
offer_state_request_offer_state_instance = OfferStateRequestOfferState.from_json(json)
# print the JSON string representation of the object
print(OfferStateRequestOfferState.to_json())

# convert the object into a dict
offer_state_request_offer_state_dict = offer_state_request_offer_state_instance.to_dict()
# create an instance of OfferStateRequestOfferState from a dict
offer_state_request_offer_state_from_dict = OfferStateRequestOfferState.from_dict(offer_state_request_offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


