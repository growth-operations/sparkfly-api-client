# PostOfferListsRequestOfferList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly.models.post_offer_lists_request_offer_list import PostOfferListsRequestOfferList

# TODO update the JSON string below
json = "{}"
# create an instance of PostOfferListsRequestOfferList from a JSON string
post_offer_lists_request_offer_list_instance = PostOfferListsRequestOfferList.from_json(json)
# print the JSON string representation of the object
print(PostOfferListsRequestOfferList.to_json())

# convert the object into a dict
post_offer_lists_request_offer_list_dict = post_offer_lists_request_offer_list_instance.to_dict()
# create an instance of PostOfferListsRequestOfferList from a dict
post_offer_lists_request_offer_list_from_dict = PostOfferListsRequestOfferList.from_dict(post_offer_lists_request_offer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


