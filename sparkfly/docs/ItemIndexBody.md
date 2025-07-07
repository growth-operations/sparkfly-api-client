# ItemIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**items** | [**List[Item]**](Item.md) |  | [optional] 

## Example

```python
from sparkfly.models.item_index_body import ItemIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of ItemIndexBody from a JSON string
item_index_body_instance = ItemIndexBody.from_json(json)
# print the JSON string representation of the object
print(ItemIndexBody.to_json())

# convert the object into a dict
item_index_body_dict = item_index_body_instance.to_dict()
# create an instance of ItemIndexBody from a dict
item_index_body_from_dict = ItemIndexBody.from_dict(item_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


