# CtmTransactionShowResponseReusableOffers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redemption_limit** | **int** |  | [optional] 
**redeem_until_depleted** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ctm_transaction_show_response_reusable_offers import CtmTransactionShowResponseReusableOffers

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionShowResponseReusableOffers from a JSON string
ctm_transaction_show_response_reusable_offers_instance = CtmTransactionShowResponseReusableOffers.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionShowResponseReusableOffers.to_json())

# convert the object into a dict
ctm_transaction_show_response_reusable_offers_dict = ctm_transaction_show_response_reusable_offers_instance.to_dict()
# create an instance of CtmTransactionShowResponseReusableOffers from a dict
ctm_transaction_show_response_reusable_offers_from_dict = CtmTransactionShowResponseReusableOffers.from_dict(ctm_transaction_show_response_reusable_offers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


