# OfferIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offers** | [**List[Offer]**](Offer.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_index_body import OfferIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of OfferIndexBody from a JSON string
offer_index_body_instance = OfferIndexBody.from_json(json)
# print the JSON string representation of the object
print(OfferIndexBody.to_json())

# convert the object into a dict
offer_index_body_dict = offer_index_body_instance.to_dict()
# create an instance of OfferIndexBody from a dict
offer_index_body_from_dict = OfferIndexBody.from_dict(offer_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


