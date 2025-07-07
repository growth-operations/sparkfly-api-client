# OfferEligibleItemsSetIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offer_eligible_item_sets** | [**List[OfferEligibleItemSet]**](OfferEligibleItemSet.md) |  | [optional] 

## Example

```python
from sparkfly.models.offer_eligible_items_set_index import OfferEligibleItemsSetIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibleItemsSetIndex from a JSON string
offer_eligible_items_set_index_instance = OfferEligibleItemsSetIndex.from_json(json)
# print the JSON string representation of the object
print(OfferEligibleItemsSetIndex.to_json())

# convert the object into a dict
offer_eligible_items_set_index_dict = offer_eligible_items_set_index_instance.to_dict()
# create an instance of OfferEligibleItemsSetIndex from a dict
offer_eligible_items_set_index_from_dict = OfferEligibleItemsSetIndex.from_dict(offer_eligible_items_set_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


