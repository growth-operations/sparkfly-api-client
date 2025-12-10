# CreateOfferListRequestOfferList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly.models.create_offer_list_request_offer_list import CreateOfferListRequestOfferList

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOfferListRequestOfferList from a JSON string
create_offer_list_request_offer_list_instance = CreateOfferListRequestOfferList.from_json(json)
# print the JSON string representation of the object
print(CreateOfferListRequestOfferList.to_json())

# convert the object into a dict
create_offer_list_request_offer_list_dict = create_offer_list_request_offer_list_instance.to_dict()
# create an instance of CreateOfferListRequestOfferList from a dict
create_offer_list_request_offer_list_from_dict = CreateOfferListRequestOfferList.from_dict(create_offer_list_request_offer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


