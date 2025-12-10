# TransactionRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**offer_state_id** | **int** |  | [optional] 
**campaign** | [**TransactionCampaign**](TransactionCampaign.md) |  | [optional] 

## Example

```python
from sparkfly.models.transaction_redemption import TransactionRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRedemption from a JSON string
transaction_redemption_instance = TransactionRedemption.from_json(json)
# print the JSON string representation of the object
print(TransactionRedemption.to_json())

# convert the object into a dict
transaction_redemption_dict = transaction_redemption_instance.to_dict()
# create an instance of TransactionRedemption from a dict
transaction_redemption_from_dict = TransactionRedemption.from_dict(transaction_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


