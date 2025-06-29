# OfferEligibleItemSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_item_set** | [**OfferEligibleItemSetRequestEligibleItemSet**](OfferEligibleItemSetRequestEligibleItemSet.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_eligible_item_set_request import OfferEligibleItemSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferEligibleItemSetRequest from a JSON string
offer_eligible_item_set_request_instance = OfferEligibleItemSetRequest.from_json(json)
# print the JSON string representation of the object
print(OfferEligibleItemSetRequest.to_json())

# convert the object into a dict
offer_eligible_item_set_request_dict = offer_eligible_item_set_request_instance.to_dict()
# create an instance of OfferEligibleItemSetRequest from a dict
offer_eligible_item_set_request_from_dict = OfferEligibleItemSetRequest.from_dict(offer_eligible_item_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


