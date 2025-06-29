# OfferPosOfferCodeIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offer_pose_codes** | [**List[OfferPosOfferCode]**](OfferPosOfferCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_pos_offer_code_index import OfferPosOfferCodeIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OfferPosOfferCodeIndex from a JSON string
offer_pos_offer_code_index_instance = OfferPosOfferCodeIndex.from_json(json)
# print the JSON string representation of the object
print(OfferPosOfferCodeIndex.to_json())

# convert the object into a dict
offer_pos_offer_code_index_dict = offer_pos_offer_code_index_instance.to_dict()
# create an instance of OfferPosOfferCodeIndex from a dict
offer_pos_offer_code_index_from_dict = OfferPosOfferCodeIndex.from_dict(offer_pos_offer_code_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


