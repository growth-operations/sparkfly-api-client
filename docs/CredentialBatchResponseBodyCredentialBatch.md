# CredentialBatchResponseBodyCredentialBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | [**CredentialBatchResponseBodyCredentialBatchAllOfOffer**](CredentialBatchResponseBodyCredentialBatchAllOfOffer.md) |  | [optional] 
**campaign** | [**CredentialBatchResponseBodyCredentialBatchAllOfCampaign**](CredentialBatchResponseBodyCredentialBatchAllOfCampaign.md) |  | [optional] 
**name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**fulfillment_method** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.credential_batch_response_body_credential_batch import CredentialBatchResponseBodyCredentialBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBatchResponseBodyCredentialBatch from a JSON string
credential_batch_response_body_credential_batch_instance = CredentialBatchResponseBodyCredentialBatch.from_json(json)
# print the JSON string representation of the object
print(CredentialBatchResponseBodyCredentialBatch.to_json())

# convert the object into a dict
credential_batch_response_body_credential_batch_dict = credential_batch_response_body_credential_batch_instance.to_dict()
# create an instance of CredentialBatchResponseBodyCredentialBatch from a dict
credential_batch_response_body_credential_batch_from_dict = CredentialBatchResponseBodyCredentialBatch.from_dict(credential_batch_response_body_credential_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


