# ItemAllOfItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**merchant_id** | **object** |  | [optional] 
**manufacturer_id** | **object** |  | [optional] 
**item_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_all_of_item import ItemAllOfItem

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAllOfItem from a JSON string
item_all_of_item_instance = ItemAllOfItem.from_json(json)
# print the JSON string representation of the object
print(ItemAllOfItem.to_json())

# convert the object into a dict
item_all_of_item_dict = item_all_of_item_instance.to_dict()
# create an instance of ItemAllOfItem from a dict
item_all_of_item_from_dict = ItemAllOfItem.from_dict(item_all_of_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


