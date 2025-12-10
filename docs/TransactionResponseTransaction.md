# TransactionResponseTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**transaction_identifier** | **str** |  | [optional] 
**receipt_id** | **str** |  | [optional] 
**totals** | [**TransactionTotals**](TransactionTotals.md) |  | [optional] 
**external_id** | **str** |  | [optional] 
**store_number** | **str** |  | [optional] 
**store_id** | **int** |  | [optional] 
**occurred_at** | **datetime** |  | [optional] 
**transaction_items** | [**List[TransactionItem]**](TransactionItem.md) |  | [optional] 
**redemptions** | [**List[TransactionRedemption]**](TransactionRedemption.md) |  | [optional] 
**applied_credentials** | [**List[TransactionAppliedCredential]**](TransactionAppliedCredential.md) |  | [optional] 

## Example

```python
from sparkfly.models.transaction_response_transaction import TransactionResponseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseTransaction from a JSON string
transaction_response_transaction_instance = TransactionResponseTransaction.from_json(json)
# print the JSON string representation of the object
print(TransactionResponseTransaction.to_json())

# convert the object into a dict
transaction_response_transaction_dict = transaction_response_transaction_instance.to_dict()
# create an instance of TransactionResponseTransaction from a dict
transaction_response_transaction_from_dict = TransactionResponseTransaction.from_dict(transaction_response_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


