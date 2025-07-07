# ItemSetAllOfItemSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**manufacturer_id** | **str** |  | [optional] 
**manufacturer_name** | **str** |  | [optional] 
**item_ids** | **List[object]** |  | [optional] 
**set_type** | **int** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.item_set_all_of_item_set import ItemSetAllOfItemSet

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetAllOfItemSet from a JSON string
item_set_all_of_item_set_instance = ItemSetAllOfItemSet.from_json(json)
# print the JSON string representation of the object
print(ItemSetAllOfItemSet.to_json())

# convert the object into a dict
item_set_all_of_item_set_dict = item_set_all_of_item_set_instance.to_dict()
# create an instance of ItemSetAllOfItemSet from a dict
item_set_all_of_item_set_from_dict = ItemSetAllOfItemSet.from_dict(item_set_all_of_item_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


