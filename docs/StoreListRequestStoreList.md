# StoreListRequestStoreList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**store_ids** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.store_list_request_store_list import StoreListRequestStoreList

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListRequestStoreList from a JSON string
store_list_request_store_list_instance = StoreListRequestStoreList.from_json(json)
# print the JSON string representation of the object
print(StoreListRequestStoreList.to_json())

# convert the object into a dict
store_list_request_store_list_dict = store_list_request_store_list_instance.to_dict()
# create an instance of StoreListRequestStoreList from a dict
store_list_request_store_list_from_dict = StoreListRequestStoreList.from_dict(store_list_request_store_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


