# OfferStateIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offer_states** | [**List[OfferState]**](OfferState.md) |  | [optional] 

## Example

```python
from sparkfly.models.offer_state_index_body import OfferStateIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of OfferStateIndexBody from a JSON string
offer_state_index_body_instance = OfferStateIndexBody.from_json(json)
# print the JSON string representation of the object
print(OfferStateIndexBody.to_json())

# convert the object into a dict
offer_state_index_body_dict = offer_state_index_body_instance.to_dict()
# create an instance of OfferStateIndexBody from a dict
offer_state_index_body_from_dict = OfferStateIndexBody.from_dict(offer_state_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


