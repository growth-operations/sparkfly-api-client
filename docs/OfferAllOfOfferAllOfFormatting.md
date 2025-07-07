# OfferAllOfOfferAllOfFormatting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bg_image** | **str** |  | [optional] 
**custom_offer_group** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**eligible_store_map** | [**OfferAllOfOfferAllOfFormattingEligibleStoreMap**](OfferAllOfOfferAllOfFormattingEligibleStoreMap.md) |  | [optional] 
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
from sparkfly_api_client.models.offer_all_of_offer_all_of_formatting import OfferAllOfOfferAllOfFormatting

# TODO update the JSON string below
json = "{}"
# create an instance of OfferAllOfOfferAllOfFormatting from a JSON string
offer_all_of_offer_all_of_formatting_instance = OfferAllOfOfferAllOfFormatting.from_json(json)
# print the JSON string representation of the object
print(OfferAllOfOfferAllOfFormatting.to_json())

# convert the object into a dict
offer_all_of_offer_all_of_formatting_dict = offer_all_of_offer_all_of_formatting_instance.to_dict()
# create an instance of OfferAllOfOfferAllOfFormatting from a dict
offer_all_of_offer_all_of_formatting_from_dict = OfferAllOfOfferAllOfFormatting.from_dict(offer_all_of_offer_all_of_formatting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


