# OfferEligibleItemSetAllOfEligibleItemSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | [optional] 
**item_set_id** | **int** |  | [optional] 
**list_type** | **int** |  | [optional] 
**type_name** | **str** |  | [optional] 
**req_qty** | **int** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.offer_eligible_item_set_all_of_eligible_item_set import OfferEligibleItemSetAllOfEligibleItemSet

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibleItemSetAllOfEligibleItemSet from a JSON string
offer_eligible_item_set_all_of_eligible_item_set_instance = OfferEligibleItemSetAllOfEligibleItemSet.from_json(json)
# print the JSON string representation of the object
print(OfferEligibleItemSetAllOfEligibleItemSet.to_json())

# convert the object into a dict
offer_eligible_item_set_all_of_eligible_item_set_dict = offer_eligible_item_set_all_of_eligible_item_set_instance.to_dict()
# create an instance of OfferEligibleItemSetAllOfEligibleItemSet from a dict
offer_eligible_item_set_all_of_eligible_item_set_from_dict = OfferEligibleItemSetAllOfEligibleItemSet.from_dict(offer_eligible_item_set_all_of_eligible_item_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


