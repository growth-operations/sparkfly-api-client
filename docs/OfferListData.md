# OfferListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_list** | [**OfferList**](OfferList.md) |  | 
**errors** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.offer_list_data import OfferListData

# TODO update the JSON string below
json = "{}"
# create an instance of OfferListData from a JSON string
offer_list_data_instance = OfferListData.from_json(json)
# print the JSON string representation of the object
print(OfferListData.to_json())

# convert the object into a dict
offer_list_data_dict = offer_list_data_instance.to_dict()
# create an instance of OfferListData from a dict
offer_list_data_from_dict = OfferListData.from_dict(offer_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


