# StoreListAllOfStoreList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**store_ids** | **List[int]** |  | [optional] 

## Example

```python
from sparkfly.models.store_list_all_of_store_list import StoreListAllOfStoreList

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListAllOfStoreList from a JSON string
store_list_all_of_store_list_instance = StoreListAllOfStoreList.from_json(json)
# print the JSON string representation of the object
print(StoreListAllOfStoreList.to_json())

# convert the object into a dict
store_list_all_of_store_list_dict = store_list_all_of_store_list_instance.to_dict()
# create an instance of StoreListAllOfStoreList from a dict
store_list_all_of_store_list_from_dict = StoreListAllOfStoreList.from_dict(store_list_all_of_store_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


