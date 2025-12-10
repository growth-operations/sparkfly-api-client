# TransactionAppliedCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.transaction_applied_credential import TransactionAppliedCredential

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionAppliedCredential from a JSON string
transaction_applied_credential_instance = TransactionAppliedCredential.from_json(json)
# print the JSON string representation of the object
print(TransactionAppliedCredential.to_json())

# convert the object into a dict
transaction_applied_credential_dict = transaction_applied_credential_instance.to_dict()
# create an instance of TransactionAppliedCredential from a dict
transaction_applied_credential_from_dict = TransactionAppliedCredential.from_dict(transaction_applied_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


