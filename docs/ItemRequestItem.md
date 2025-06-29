# ItemRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_request_item import ItemRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRequestItem from a JSON string
item_request_item_instance = ItemRequestItem.from_json(json)
# print the JSON string representation of the object
print(ItemRequestItem.to_json())

# convert the object into a dict
item_request_item_dict = item_request_item_instance.to_dict()
# create an instance of ItemRequestItem from a dict
item_request_item_from_dict = ItemRequestItem.from_dict(item_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


