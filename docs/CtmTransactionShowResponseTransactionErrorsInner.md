# CtmTransactionShowResponseTransactionErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**pos_offer_code_type** | **str** |  | [optional] 
**validation_id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**priority** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.ctm_transaction_show_response_transaction_errors_inner import CtmTransactionShowResponseTransactionErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseTransactionErrorsInner from a JSON string
ctm_transaction_show_response_transaction_errors_inner_instance = CtmTransactionShowResponseTransactionErrorsInner.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseTransactionErrorsInner.to_json())

# convert the object into a dict
ctm_transaction_show_response_transaction_errors_inner_dict = ctm_transaction_show_response_transaction_errors_inner_instance.to_dict()
# create an instance of CtmTransactionShowResponseTransactionErrorsInner from a dict
ctm_transaction_show_response_transaction_errors_inner_from_dict = CtmTransactionShowResponseTransactionErrorsInner.from_dict(ctm_transaction_show_response_transaction_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


