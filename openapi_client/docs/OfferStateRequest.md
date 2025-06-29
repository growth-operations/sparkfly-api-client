# OfferStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state** | [**OfferStateRequestOfferState**](OfferStateRequestOfferState.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_state_request import OfferStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateRequest from a JSON string
offer_state_request_instance = OfferStateRequest.from_json(json)
# print the JSON string representation of the object
print(OfferStateRequest.to_json())

# convert the object into a dict
offer_state_request_dict = offer_state_request_instance.to_dict()
# create an instance of OfferStateRequest from a dict
offer_state_request_from_dict = OfferStateRequest.from_dict(offer_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


