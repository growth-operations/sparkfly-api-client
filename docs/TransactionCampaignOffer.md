# TransactionCampaignOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.transaction_campaign_offer import TransactionCampaignOffer

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCampaignOffer from a JSON string
transaction_campaign_offer_instance = TransactionCampaignOffer.from_json(json)
# print the JSON string representation of the object
print(TransactionCampaignOffer.to_json())

# convert the object into a dict
transaction_campaign_offer_dict = transaction_campaign_offer_instance.to_dict()
# create an instance of TransactionCampaignOffer from a dict
transaction_campaign_offer_from_dict = TransactionCampaignOffer.from_dict(transaction_campaign_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


