# StoreListIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**store_lists** | [**List[StoreList]**](StoreList.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.store_list_index_body import StoreListIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of StoreListIndexBody from a JSON string
store_list_index_body_instance = StoreListIndexBody.from_json(json)
# print the JSON string representation of the object
print(StoreListIndexBody.to_json())

# convert the object into a dict
store_list_index_body_dict = store_list_index_body_instance.to_dict()
# create an instance of StoreListIndexBody from a dict
store_list_index_body_from_dict = StoreListIndexBody.from_dict(store_list_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


