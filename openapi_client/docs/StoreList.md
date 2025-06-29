# StoreList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**store_list** | [**StoreListAllOfStoreList**](StoreListAllOfStoreList.md) |  | [optional] 

## Example

```python
from openapi_client.models.store_list import StoreList

# TODO update the JSON string below
json = "{}"
# create an instance of StoreList from a JSON string
store_list_instance = StoreList.from_json(json)
# print the JSON string representation of the object
print(StoreList.to_json())

# convert the object into a dict
store_list_dict = store_list_instance.to_dict()
# create an instance of StoreList from a dict
store_list_from_dict = StoreList.from_dict(store_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


