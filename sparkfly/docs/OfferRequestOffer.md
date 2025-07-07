# OfferRequestOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**offer_type** | **int** |  | [optional] 
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


