# ItemSetIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**item_sets** | [**List[ItemSet]**](ItemSet.md) |  | [optional] 

## Example

```python
from sparkfly.models.item_set_index_body import ItemSetIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetIndexBody from a JSON string
item_set_index_body_instance = ItemSetIndexBody.from_json(json)
# print the JSON string representation of the object
print(ItemSetIndexBody.to_json())

# convert the object into a dict
item_set_index_body_dict = item_set_index_body_instance.to_dict()
# create an instance of ItemSetIndexBody from a dict
item_set_index_body_from_dict = ItemSetIndexBody.from_dict(item_set_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


