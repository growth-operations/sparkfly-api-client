# OfferStateAllOfOfferState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**locked** | **bool** |  | [optional] 
**activates_at** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 
**custom_data** | **str** |  | [optional] 
**credential_custom_data** | **str** |  | [optional] 
**offer_activities** | **List[object]** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**offer_short_name** | **str** |  | [optional] 
**offer_campaign_name** | **str** |  | [optional] 
**offer_group** | **str** |  | [optional] 
**offer_description** | **str** |  | [optional] 
**offer_value_required** | **int** |  | [optional] 
**offer_terms_and_conditions** | **str** |  | [optional] 
**offer_web_image_url** | **str** |  | [optional] 
**offer_web_thumb_url** | **str** |  | [optional] 
**offer_mobile_image_url** | **str** |  | [optional] 
**offer_mobile_thumb_url** | **str** |  | [optional] 
**is_reward** | **bool** |  | [optional] 
**credential_identifier** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**transferable** | **bool** |  | [optional] 
**reusable** | **bool** |  | [optional] 
**offer_tags** | **List[object]** |  | [optional] 
**offer_campaign_tags** | **List[object]** |  | [optional] 
**campaign_external_id** | **str** |  | [optional] 
**campaign_xid** | **str** |  | [optional] 
**campaign_id** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.offer_state_all_of_offer_state import OfferStateAllOfOfferState

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateAllOfOfferState from a JSON string
offer_state_all_of_offer_state_instance = OfferStateAllOfOfferState.from_json(json)
# print the JSON string representation of the object
print(OfferStateAllOfOfferState.to_json())

# convert the object into a dict
offer_state_all_of_offer_state_dict = offer_state_all_of_offer_state_instance.to_dict()
# create an instance of OfferStateAllOfOfferState from a dict
offer_state_all_of_offer_state_from_dict = OfferStateAllOfOfferState.from_dict(offer_state_all_of_offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


