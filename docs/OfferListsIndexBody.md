# OfferListsIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offer_lists** | [**List[OfferList]**](OfferList.md) |  | [optional] 

## Example

```python
from sparkfly.models.offer_lists_index_body import OfferListsIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of OfferListsIndexBody from a JSON string
offer_lists_index_body_instance = OfferListsIndexBody.from_json(json)
# print the JSON string representation of the object
print(OfferListsIndexBody.to_json())

# convert the object into a dict
offer_lists_index_body_dict = offer_lists_index_body_instance.to_dict()
# create an instance of OfferListsIndexBody from a dict
offer_lists_index_body_from_dict = OfferListsIndexBody.from_dict(offer_lists_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


