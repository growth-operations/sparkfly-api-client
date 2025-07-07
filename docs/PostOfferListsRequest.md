# PostOfferListsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_list** | [**PostOfferListsRequestOfferList**](PostOfferListsRequestOfferList.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.post_offer_lists_request import PostOfferListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostOfferListsRequest from a JSON string
post_offer_lists_request_instance = PostOfferListsRequest.from_json(json)
# print the JSON string representation of the object
print(PostOfferListsRequest.to_json())

# convert the object into a dict
post_offer_lists_request_dict = post_offer_lists_request_instance.to_dict()
# create an instance of PostOfferListsRequest from a dict
post_offer_lists_request_from_dict = PostOfferListsRequest.from_dict(post_offer_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


