# CredentialIndexBodyInnerCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**member_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**redeeming_account_id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**eligible_channel_id** | **int** |  | [optional] 
**store_id** | **int** |  | [optional] 
**voided_at** | **datetime** |  | [optional] 
**redeemed_at** | **datetime** |  | [optional] 
**processed_at** | **datetime** |  | [optional] 
**reusable** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**location_address** | **str** |  | [optional] 
**supports_barcode** | **bool** |  | [optional] 
**barcodes_supported** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.credential_index_body_inner_credential import CredentialIndexBodyInnerCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialIndexBodyInnerCredential from a JSON string
credential_index_body_inner_credential_instance = CredentialIndexBodyInnerCredential.from_json(json)
# print the JSON string representation of the object
print(CredentialIndexBodyInnerCredential.to_json())

# convert the object into a dict
credential_index_body_inner_credential_dict = credential_index_body_inner_credential_instance.to_dict()
# create an instance of CredentialIndexBodyInnerCredential from a dict
credential_index_body_inner_credential_from_dict = CredentialIndexBodyInnerCredential.from_dict(credential_index_body_inner_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


