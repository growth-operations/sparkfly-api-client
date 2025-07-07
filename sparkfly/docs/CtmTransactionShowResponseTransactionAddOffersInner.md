# CtmTransactionShowResponseTransactionAddOffersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_identifier** | **str** |  | [optional] 
**rpe_auth_code** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**pos_offer_code_type** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**ammount** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**qualifying_items** | [**List[CtmTransactionShowResponseTransactionAddOffersInnerQualifyingItemsInner]**](CtmTransactionShowResponseTransactionAddOffersInnerQualifyingItemsInner.md) |  | [optional] 
**tip** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**auth** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.ctm_transaction_show_response_transaction_add_offers_inner import CtmTransactionShowResponseTransactionAddOffersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseTransactionAddOffersInner from a JSON string
ctm_transaction_show_response_transaction_add_offers_inner_instance = CtmTransactionShowResponseTransactionAddOffersInner.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseTransactionAddOffersInner.to_json())

# convert the object into a dict
ctm_transaction_show_response_transaction_add_offers_inner_dict = ctm_transaction_show_response_transaction_add_offers_inner_instance.to_dict()
# create an instance of CtmTransactionShowResponseTransactionAddOffersInner from a dict
ctm_transaction_show_response_transaction_add_offers_inner_from_dict = CtmTransactionShowResponseTransactionAddOffersInner.from_dict(ctm_transaction_show_response_transaction_add_offers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


