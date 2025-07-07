# CtmTransactionShowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**offers** | **List[int]** |  | [optional] 
**loyalty_id** | **str** |  | [optional] 
**reusable** | **bool** |  | [optional] 
**transaction** | [**CtmTransactionShowResponseTransaction**](CtmTransactionShowResponseTransaction.md) |  | [optional] 
**availible_offers** | [**List[CtmTransactionShowResponseAvailibleOffersInner]**](CtmTransactionShowResponseAvailibleOffersInner.md) |  | [optional] 
**reusable_offers** | [**CtmTransactionShowResponseReusableOffers**](CtmTransactionShowResponseReusableOffers.md) |  | [optional] 
**store_default_language** | **str** |  | [optional] 
**account_default_language** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.ctm_transaction_show_response import CtmTransactionShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponse from a JSON string
ctm_transaction_show_response_instance = CtmTransactionShowResponse.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponse.to_json())

# convert the object into a dict
ctm_transaction_show_response_dict = ctm_transaction_show_response_instance.to_dict()
# create an instance of CtmTransactionShowResponse from a dict
ctm_transaction_show_response_from_dict = CtmTransactionShowResponse.from_dict(ctm_transaction_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


