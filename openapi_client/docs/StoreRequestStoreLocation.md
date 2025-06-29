# StoreRequestStoreLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.store_request_store_location import StoreRequestStoreLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StoreRequestStoreLocation from a JSON string
store_request_store_location_instance = StoreRequestStoreLocation.from_json(json)
# print the JSON string representation of the object
print(StoreRequestStoreLocation.to_json())

# convert the object into a dict
store_request_store_location_dict = store_request_store_location_instance.to_dict()
# create an instance of StoreRequestStoreLocation from a dict
store_request_store_location_from_dict = StoreRequestStoreLocation.from_dict(store_request_store_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


