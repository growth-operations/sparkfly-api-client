# PosOfferCodeIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**pos_offer_codes** | [**List[PosOfferCode]**](PosOfferCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.pos_offer_code_index_body import PosOfferCodeIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of PosOfferCodeIndexBody from a JSON string
pos_offer_code_index_body_instance = PosOfferCodeIndexBody.from_json(json)
# print the JSON string representation of the object
print(PosOfferCodeIndexBody.to_json())

# convert the object into a dict
pos_offer_code_index_body_dict = pos_offer_code_index_body_instance.to_dict()
# create an instance of PosOfferCodeIndexBody from a dict
pos_offer_code_index_body_from_dict = PosOfferCodeIndexBody.from_dict(pos_offer_code_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


