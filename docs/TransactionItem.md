# TransactionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**item_code** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**ext_price** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.transaction_item import TransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionItem from a JSON string
transaction_item_instance = TransactionItem.from_json(json)
# print the JSON string representation of the object
print(TransactionItem.to_json())

# convert the object into a dict
transaction_item_dict = transaction_item_instance.to_dict()
# create an instance of TransactionItem from a dict
transaction_item_from_dict = TransactionItem.from_dict(transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


