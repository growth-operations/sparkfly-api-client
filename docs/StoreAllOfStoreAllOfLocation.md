# StoreAllOfStoreAllOfLocation


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
from sparkfly_api_client.models.store_all_of_store_all_of_location import StoreAllOfStoreAllOfLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StoreAllOfStoreAllOfLocation from a JSON string
store_all_of_store_all_of_location_instance = StoreAllOfStoreAllOfLocation.from_json(json)
# print the JSON string representation of the object
print(StoreAllOfStoreAllOfLocation.to_json())

# convert the object into a dict
store_all_of_store_all_of_location_dict = store_all_of_store_all_of_location_instance.to_dict()
# create an instance of StoreAllOfStoreAllOfLocation from a dict
store_all_of_store_all_of_location_from_dict = StoreAllOfStoreAllOfLocation.from_dict(store_all_of_store_all_of_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


