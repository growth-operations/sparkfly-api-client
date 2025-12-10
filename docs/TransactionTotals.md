# TransactionTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paid** | **int** |  | [optional] 
**discount** | **int** |  | [optional] 
**subtotal** | **int** |  | [optional] 
**service_charge** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.transaction_totals import TransactionTotals

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTotals from a JSON string
transaction_totals_instance = TransactionTotals.from_json(json)
# print the JSON string representation of the object
print(TransactionTotals.to_json())

# convert the object into a dict
transaction_totals_dict = transaction_totals_instance.to_dict()
# create an instance of TransactionTotals from a dict
transaction_totals_from_dict = TransactionTotals.from_dict(transaction_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


