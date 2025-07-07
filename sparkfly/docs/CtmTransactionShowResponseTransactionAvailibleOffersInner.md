# CtmTransactionShowResponseTransactionAvailibleOffersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**valid_now** | **bool** |  | [optional] 
**invalid_reason** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.ctm_transaction_show_response_transaction_availible_offers_inner import CtmTransactionShowResponseTransactionAvailibleOffersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseTransactionAvailibleOffersInner from a JSON string
ctm_transaction_show_response_transaction_availible_offers_inner_instance = CtmTransactionShowResponseTransactionAvailibleOffersInner.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseTransactionAvailibleOffersInner.to_json())

# convert the object into a dict
ctm_transaction_show_response_transaction_availible_offers_inner_dict = ctm_transaction_show_response_transaction_availible_offers_inner_instance.to_dict()
# create an instance of CtmTransactionShowResponseTransactionAvailibleOffersInner from a dict
ctm_transaction_show_response_transaction_availible_offers_inner_from_dict = CtmTransactionShowResponseTransactionAvailibleOffersInner.from_dict(ctm_transaction_show_response_transaction_availible_offers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


