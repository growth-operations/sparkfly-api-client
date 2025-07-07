# OfferState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**offer_state** | [**OfferStateAllOfOfferState**](OfferStateAllOfOfferState.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.offer_state import OfferState

# TODO update the JSON string below
json = "{}"
# create an instance of OfferState from a JSON string
offer_state_instance = OfferState.from_json(json)
# print the JSON string representation of the object
print(OfferState.to_json())

# convert the object into a dict
offer_state_dict = offer_state_instance.to_dict()
# create an instance of OfferState from a dict
offer_state_from_dict = OfferState.from_dict(offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


