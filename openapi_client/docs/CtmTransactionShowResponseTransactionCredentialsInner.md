# CtmTransactionShowResponseTransactionCredentialsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | [optional] 
**tx_credential** | [**CtmTransactionShowResponseTransactionCredentialsInnerTxCredential**](CtmTransactionShowResponseTransactionCredentialsInnerTxCredential.md) |  | [optional] 

## Example

```python
from openapi_client.models.ctm_transaction_show_response_transaction_credentials_inner import CtmTransactionShowResponseTransactionCredentialsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseTransactionCredentialsInner from a JSON string
ctm_transaction_show_response_transaction_credentials_inner_instance = CtmTransactionShowResponseTransactionCredentialsInner.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseTransactionCredentialsInner.to_json())

# convert the object into a dict
ctm_transaction_show_response_transaction_credentials_inner_dict = ctm_transaction_show_response_transaction_credentials_inner_instance.to_dict()
# create an instance of CtmTransactionShowResponseTransactionCredentialsInner from a dict
ctm_transaction_show_response_transaction_credentials_inner_from_dict = CtmTransactionShowResponseTransactionCredentialsInner.from_dict(ctm_transaction_show_response_transaction_credentials_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


