# StoreIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**stores** | [**List[Store]**](Store.md) |  | [optional] 

## Example

```python
from openapi_client.models.store_index_body import StoreIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of StoreIndexBody from a JSON string
store_index_body_instance = StoreIndexBody.from_json(json)
# print the JSON string representation of the object
print(StoreIndexBody.to_json())

# convert the object into a dict
store_index_body_dict = store_index_body_instance.to_dict()
# create an instance of StoreIndexBody from a dict
store_index_body_from_dict = StoreIndexBody.from_dict(store_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


