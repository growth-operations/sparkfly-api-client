# StoreAllOfStoreLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**lat** | **int** |  | [optional] 
**lng** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.store_all_of_store_location import StoreAllOfStoreLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StoreAllOfStoreLocation from a JSON string
store_all_of_store_location_instance = StoreAllOfStoreLocation.from_json(json)
# print the JSON string representation of the object
print(StoreAllOfStoreLocation.to_json())

# convert the object into a dict
store_all_of_store_location_dict = store_all_of_store_location_instance.to_dict()
# create an instance of StoreAllOfStoreLocation from a dict
store_all_of_store_location_from_dict = StoreAllOfStoreLocation.from_dict(store_all_of_store_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


