# OfferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**OfferRequestOffer**](OfferRequestOffer.md) |  | [optional] 

## Example

```python
from sparkfly.models.offer_request import OfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferRequest from a JSON string
offer_request_instance = OfferRequest.from_json(json)
# print the JSON string representation of the object
print(OfferRequest.to_json())

# convert the object into a dict
offer_request_dict = offer_request_instance.to_dict()
# create an instance of OfferRequest from a dict
offer_request_from_dict = OfferRequest.from_dict(offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


