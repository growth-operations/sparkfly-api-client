# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**item** | [**ItemAllOfItem**](ItemAllOfItem.md) |  | [optional] 

## Example

```python
from sparkfly.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


