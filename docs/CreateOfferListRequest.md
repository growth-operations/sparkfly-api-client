# CreateOfferListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_list** | [**CreateOfferListRequestOfferList**](CreateOfferListRequestOfferList.md) |  | [optional] 

## Example

```python
from sparkfly.models.create_offer_list_request import CreateOfferListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOfferListRequest from a JSON string
create_offer_list_request_instance = CreateOfferListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOfferListRequest.to_json())

# convert the object into a dict
create_offer_list_request_dict = create_offer_list_request_instance.to_dict()
# create an instance of CreateOfferListRequest from a dict
create_offer_list_request_from_dict = CreateOfferListRequest.from_dict(create_offer_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


