# OfferEligibleItemSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**eligible_item_set** | [**OfferEligibleItemSetAllOfEligibleItemSet**](OfferEligibleItemSetAllOfEligibleItemSet.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.offer_eligible_item_set import OfferEligibleItemSet

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibleItemSet from a JSON string
offer_eligible_item_set_instance = OfferEligibleItemSet.from_json(json)
# print the JSON string representation of the object
print(OfferEligibleItemSet.to_json())

# convert the object into a dict
offer_eligible_item_set_dict = offer_eligible_item_set_instance.to_dict()
# create an instance of OfferEligibleItemSet from a dict
offer_eligible_item_set_from_dict = OfferEligibleItemSet.from_dict(offer_eligible_item_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


