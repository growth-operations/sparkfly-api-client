# TransactionCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**external_id** | **str** |  | [optional] 
**xid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offer** | [**TransactionCampaignOffer**](TransactionCampaignOffer.md) |  | [optional] 

## Example

```python
from sparkfly.models.transaction_campaign import TransactionCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCampaign from a JSON string
transaction_campaign_instance = TransactionCampaign.from_json(json)
# print the JSON string representation of the object
print(TransactionCampaign.to_json())

# convert the object into a dict
transaction_campaign_dict = transaction_campaign_instance.to_dict()
# create an instance of TransactionCampaign from a dict
transaction_campaign_from_dict = TransactionCampaign.from_dict(transaction_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


