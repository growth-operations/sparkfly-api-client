# OfferEligibleItemSetRequestEligibleItemSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_type** | **int** |  | [optional] 
**req_qty** | **int** |  | [optional] 
**item_set_id** | **int** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.offer_eligible_item_set_request_eligible_item_set import OfferEligibleItemSetRequestEligibleItemSet

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibleItemSetRequestEligibleItemSet from a JSON string
offer_eligible_item_set_request_eligible_item_set_instance = OfferEligibleItemSetRequestEligibleItemSet.from_json(json)
# print the JSON string representation of the object
print(OfferEligibleItemSetRequestEligibleItemSet.to_json())

# convert the object into a dict
offer_eligible_item_set_request_eligible_item_set_dict = offer_eligible_item_set_request_eligible_item_set_instance.to_dict()
# create an instance of OfferEligibleItemSetRequestEligibleItemSet from a dict
offer_eligible_item_set_request_eligible_item_set_from_dict = OfferEligibleItemSetRequestEligibleItemSet.from_dict(offer_eligible_item_set_request_eligible_item_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


