# CtmTransactionShowResponseTransactionRecieptMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**barcode_format** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**reciept_type** | **int** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.ctm_transaction_show_response_transaction_reciept_messages_inner import CtmTransactionShowResponseTransactionRecieptMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseTransactionRecieptMessagesInner from a JSON string
ctm_transaction_show_response_transaction_reciept_messages_inner_instance = CtmTransactionShowResponseTransactionRecieptMessagesInner.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseTransactionRecieptMessagesInner.to_json())

# convert the object into a dict
ctm_transaction_show_response_transaction_reciept_messages_inner_dict = ctm_transaction_show_response_transaction_reciept_messages_inner_instance.to_dict()
# create an instance of CtmTransactionShowResponseTransactionRecieptMessagesInner from a dict
ctm_transaction_show_response_transaction_reciept_messages_inner_from_dict = CtmTransactionShowResponseTransactionRecieptMessagesInner.from_dict(ctm_transaction_show_response_transaction_reciept_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


