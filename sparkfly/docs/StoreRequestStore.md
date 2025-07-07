# StoreRequestStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**phone** | **str** |  | [optional] 
**contacts** | [**StoreRequestStoreContacts**](StoreRequestStoreContacts.md) |  | [optional] 
**location** | [**StoreRequestStoreLocation**](StoreRequestStoreLocation.md) |  | [optional] 

## Example

```python
from sparkfly.models.store_request_store import StoreRequestStore

# TODO update the JSON string below
json = "{}"
# create an instance of StoreRequestStore from a JSON string
store_request_store_instance = StoreRequestStore.from_json(json)
# print the JSON string representation of the object
print(StoreRequestStore.to_json())

# convert the object into a dict
store_request_store_dict = store_request_store_instance.to_dict()
# create an instance of StoreRequestStore from a dict
store_request_store_from_dict = StoreRequestStore.from_dict(store_request_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


