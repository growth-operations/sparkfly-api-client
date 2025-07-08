# OfferRequestOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**manufacturer_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_template_id** | **str** |  | [optional] 
**offer_type** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**offer_code** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**criteria** | **object** |  | [optional] 
**points_earning_value** | **int** |  | [optional] 
**points_required_value** | **int** |  | [optional] 
**reward_item_description** | **str** |  | [optional] 
**reward_item_value** | **int** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**terms_and_conditions_template_id** | **str** |  | [optional] 
**quest_only** | **bool** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**external_reward** | **str** |  | [optional] 
**is_reward** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**activates_at** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**stop_offering_at** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**max_amount** | **int** |  | [optional] 
**min_spend_amount** | **int** |  | [optional] 
**trigger_amount** | **int** |  | [optional] 
**max_redemptions** | **int** |  | [optional] 
**max_redemptions_per_member** | **int** |  | [optional] 
**max_redemptions_per_member_per_day** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**initial_value_mode** | **str** |  | [optional] 
**offer_value_text** | **str** |  | [optional] 
**offer_value_text_es** | **str** |  | [optional] 
**formatting** | [**OfferRequestOfferFormatting**](OfferRequestOfferFormatting.md) |  | [optional] 
**eligibility** | [**OfferRequestOfferEligibility**](OfferRequestOfferEligibility.md) |  | [optional] 
**redeem_until_depleted** | **bool** |  | [optional] 
**redemption_grace_period** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.offer_request_offer import OfferRequestOffer

# TODO update the JSON string below
json = "{}"
# create an instance of OfferRequestOffer from a JSON string
offer_request_offer_instance = OfferRequestOffer.from_json(json)
# print the JSON string representation of the object
print(OfferRequestOffer.to_json())

# convert the object into a dict
offer_request_offer_dict = offer_request_offer_instance.to_dict()
# create an instance of OfferRequestOffer from a dict
offer_request_offer_from_dict = OfferRequestOffer.from_dict(offer_request_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


