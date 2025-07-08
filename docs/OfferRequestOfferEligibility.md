# OfferRequestOfferEligibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ids** | **List[int]** |  | [optional] 
**store_list_ids** | **List[object]** |  | [optional] 
**member_list_ids** | **List[object]** |  | [optional] 
**channel_ids** | **List[object]** |  | [optional] 

## Example

```python
from sparkfly.models.offer_request_offer_eligibility import OfferRequestOfferEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of OfferRequestOfferEligibility from a JSON string
offer_request_offer_eligibility_instance = OfferRequestOfferEligibility.from_json(json)
# print the JSON string representation of the object
print(OfferRequestOfferEligibility.to_json())

# convert the object into a dict
offer_request_offer_eligibility_dict = offer_request_offer_eligibility_instance.to_dict()
# create an instance of OfferRequestOfferEligibility from a dict
offer_request_offer_eligibility_from_dict = OfferRequestOfferEligibility.from_dict(offer_request_offer_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


