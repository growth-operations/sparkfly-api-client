# StoreAllOfStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**contacts** | [**StoreRequestStoreContacts**](StoreRequestStoreContacts.md) |  | [optional] 
**location** | [**StoreAllOfStoreAllOfLocation**](StoreAllOfStoreAllOfLocation.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 
**online_ordering_id** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.store_all_of_store import StoreAllOfStore

# TODO update the JSON string below
json = "{}"
# create an instance of StoreAllOfStore from a JSON string
store_all_of_store_instance = StoreAllOfStore.from_json(json)
# print the JSON string representation of the object
print(StoreAllOfStore.to_json())

# convert the object into a dict
store_all_of_store_dict = store_all_of_store_instance.to_dict()
# create an instance of StoreAllOfStore from a dict
store_all_of_store_from_dict = StoreAllOfStore.from_dict(store_all_of_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


