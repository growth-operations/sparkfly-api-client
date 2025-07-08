# OfferRequestOfferFormatting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bg_image** | **str** |  | [optional] 
**custom_offer_group** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**eligible_store_map** | [**OfferRequestOfferFormattingEligibleStoreMap**](OfferRequestOfferFormattingEligibleStoreMap.md) |  | [optional] 
**mobile_thumb_url** | **str** |  | [optional] 
**mobile_url** | **str** |  | [optional] 
**no_printable** | **bool** |  | [optional] 
**offer_store_highlight_text_template** | **str** |  | [optional] 
**offer_storelist_highlight_text_template** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**web_thumb_url** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.offer_request_offer_formatting import OfferRequestOfferFormatting

# TODO update the JSON string below
json = "{}"
# create an instance of OfferRequestOfferFormatting from a JSON string
offer_request_offer_formatting_instance = OfferRequestOfferFormatting.from_json(json)
# print the JSON string representation of the object
print(OfferRequestOfferFormatting.to_json())

# convert the object into a dict
offer_request_offer_formatting_dict = offer_request_offer_formatting_instance.to_dict()
# create an instance of OfferRequestOfferFormatting from a dict
offer_request_offer_formatting_from_dict = OfferRequestOfferFormatting.from_dict(offer_request_offer_formatting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


