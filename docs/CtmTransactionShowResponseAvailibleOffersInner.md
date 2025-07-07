# CtmTransactionShowResponseAvailibleOffersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**eligible_channel_id** | **int** |  | [optional] 
**activation_date** | **str** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.ctm_transaction_show_response_availible_offers_inner import CtmTransactionShowResponseAvailibleOffersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseAvailibleOffersInner from a JSON string
ctm_transaction_show_response_availible_offers_inner_instance = CtmTransactionShowResponseAvailibleOffersInner.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseAvailibleOffersInner.to_json())

# convert the object into a dict
ctm_transaction_show_response_availible_offers_inner_dict = ctm_transaction_show_response_availible_offers_inner_instance.to_dict()
# create an instance of CtmTransactionShowResponseAvailibleOffersInner from a dict
ctm_transaction_show_response_availible_offers_inner_from_dict = CtmTransactionShowResponseAvailibleOffersInner.from_dict(ctm_transaction_show_response_availible_offers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


