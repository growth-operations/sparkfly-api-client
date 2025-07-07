# StoreListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_list** | [**StoreListRequestStoreList**](StoreListRequestStoreList.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.store_list_request import StoreListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListRequest from a JSON string
store_list_request_instance = StoreListRequest.from_json(json)
# print the JSON string representation of the object
print(StoreListRequest.to_json())

# convert the object into a dict
store_list_request_dict = store_list_request_instance.to_dict()
# create an instance of StoreListRequest from a dict
store_list_request_from_dict = StoreListRequest.from_dict(store_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


