# ItemSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**item_set** | [**ItemSetAllOfItemSet**](ItemSetAllOfItemSet.md) |  | [optional] 

## Example

```python
from sparkfly.models.item_set import ItemSet

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSet from a JSON string
item_set_instance = ItemSet.from_json(json)
# print the JSON string representation of the object
print(ItemSet.to_json())

# convert the object into a dict
item_set_dict = item_set_instance.to_dict()
# create an instance of ItemSet from a dict
item_set_from_dict = ItemSet.from_dict(item_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


