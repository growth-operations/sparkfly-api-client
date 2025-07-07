# ItemSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_set** | [**ItemSetRequestItemSet**](ItemSetRequestItemSet.md) |  | [optional] 

## Example

```python
from sparkfly.models.item_set_request import ItemSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSetRequest from a JSON string
item_set_request_instance = ItemSetRequest.from_json(json)
# print the JSON string representation of the object
print(ItemSetRequest.to_json())

# convert the object into a dict
item_set_request_dict = item_set_request_instance.to_dict()
# create an instance of ItemSetRequest from a dict
item_set_request_from_dict = ItemSetRequest.from_dict(item_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


