# CtmTransactionShowResponseTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[CtmTransactionShowResponseTransactionErrorsInner]**](CtmTransactionShowResponseTransactionErrorsInner.md) |  | [optional] 
**display_messages** | [**List[CtmTransactionShowResponseTransactionDisplayMessagesInner]**](CtmTransactionShowResponseTransactionDisplayMessagesInner.md) |  | [optional] 
**reciept_messages** | [**List[CtmTransactionShowResponseTransactionRecieptMessagesInner]**](CtmTransactionShowResponseTransactionRecieptMessagesInner.md) |  | [optional] 
**credentials** | [**List[CtmTransactionShowResponseTransactionCredentialsInner]**](CtmTransactionShowResponseTransactionCredentialsInner.md) |  | [optional] 
**add_offers** | [**List[CtmTransactionShowResponseTransactionAddOffersInner]**](CtmTransactionShowResponseTransactionAddOffersInner.md) |  | [optional] 
**remove_offers** | [**List[CtmTransactionShowResponseTransactionAddOffersInner]**](CtmTransactionShowResponseTransactionAddOffersInner.md) |  | [optional] 
**availible_offers** | [**List[CtmTransactionShowResponseTransactionAvailibleOffersInner]**](CtmTransactionShowResponseTransactionAvailibleOffersInner.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.ctm_transaction_show_response_transaction import CtmTransactionShowResponseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseTransaction from a JSON string
ctm_transaction_show_response_transaction_instance = CtmTransactionShowResponseTransaction.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseTransaction.to_json())

# convert the object into a dict
ctm_transaction_show_response_transaction_dict = ctm_transaction_show_response_transaction_instance.to_dict()
# create an instance of CtmTransactionShowResponseTransaction from a dict
ctm_transaction_show_response_transaction_from_dict = CtmTransactionShowResponseTransaction.from_dict(ctm_transaction_show_response_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


