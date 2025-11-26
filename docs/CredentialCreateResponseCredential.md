# CredentialCreateResponseCredential


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
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**credential_type** | **int** |  | [optional] 
**annotations** | **object** |  | [optional] 
**printable** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 
**redemption_identifier_type** | **int** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**offer_name** | **str** |  | [optional] 
**location_address** | **str** |  | [optional] 
**supports_barcode** | **bool** |  | [optional] 
**barcodes_supported** | **str** |  | [optional] 
**code_lifetime** | **int** |  | [optional] 
**offer_expires** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**custom_data** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.credential_create_response_credential import CredentialCreateResponseCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialCreateResponseCredential from a JSON string
credential_create_response_credential_instance = CredentialCreateResponseCredential.from_json(json)
# print the JSON string representation of the object
print(CredentialCreateResponseCredential.to_json())

# convert the object into a dict
credential_create_response_credential_dict = credential_create_response_credential_instance.to_dict()
# create an instance of CredentialCreateResponseCredential from a dict
credential_create_response_credential_from_dict = CredentialCreateResponseCredential.from_dict(credential_create_response_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


