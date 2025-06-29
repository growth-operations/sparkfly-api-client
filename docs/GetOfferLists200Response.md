# GetOfferLists200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**offer_lists** | [**List[GetOfferLists200ResponseOfferListsInner]**](GetOfferLists200ResponseOfferListsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_offer_lists200_response import GetOfferLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOfferLists200Response from a JSON string
get_offer_lists200_response_instance = GetOfferLists200Response.from_json(json)
# print the JSON string representation of the object
print(GetOfferLists200Response.to_json())

# convert the object into a dict
get_offer_lists200_response_dict = get_offer_lists200_response_instance.to_dict()
# create an instance of GetOfferLists200Response from a dict
get_offer_lists200_response_from_dict = GetOfferLists200Response.from_dict(get_offer_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


