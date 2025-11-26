# CredentialCreateRequestCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_identifier** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 
**reusable** | **bool** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**store_id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**printable** | **bool** |  | [optional] 
**offer_ids** | **List[int]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.credential_create_request_credential import CredentialCreateRequestCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialCreateRequestCredential from a JSON string
credential_create_request_credential_instance = CredentialCreateRequestCredential.from_json(json)
# print the JSON string representation of the object
print(CredentialCreateRequestCredential.to_json())

# convert the object into a dict
credential_create_request_credential_dict = credential_create_request_credential_instance.to_dict()
# create an instance of CredentialCreateRequestCredential from a dict
credential_create_request_credential_from_dict = CredentialCreateRequestCredential.from_dict(credential_create_request_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


