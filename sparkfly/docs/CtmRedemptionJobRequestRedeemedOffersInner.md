# CtmRedemptionJobRequestRedeemedOffersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**override_ammount** | **int** |  | [optional] 
**credential** | **str** |  | [optional] 
**rpe_auth_code** | **str** |  | [optional] 
**pos_offer_code_type** | **str** |  | [optional] 
**linked_item_entry_id** | **str** |  | [optional] 
**qualifying_items** | [**List[CtmRedemptionJobRequestRedeemedOffersInnerQualifyingItemsInner]**](CtmRedemptionJobRequestRedeemedOffersInnerQualifyingItemsInner.md) |  | [optional] 

## Example

```python
from sparkfly.models.ctm_redemption_job_request_redeemed_offers_inner import CtmRedemptionJobRequestRedeemedOffersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmRedemptionJobRequestRedeemedOffersInner from a JSON string
ctm_redemption_job_request_redeemed_offers_inner_instance = CtmRedemptionJobRequestRedeemedOffersInner.from_json(json)
# print the JSON string representation of the object
print(CtmRedemptionJobRequestRedeemedOffersInner.to_json())

# convert the object into a dict
ctm_redemption_job_request_redeemed_offers_inner_dict = ctm_redemption_job_request_redeemed_offers_inner_instance.to_dict()
# create an instance of CtmRedemptionJobRequestRedeemedOffersInner from a dict
ctm_redemption_job_request_redeemed_offers_inner_from_dict = CtmRedemptionJobRequestRedeemedOffersInner.from_dict(ctm_redemption_job_request_redeemed_offers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


