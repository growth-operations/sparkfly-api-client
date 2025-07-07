# CredentialBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fulfillment_method** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.credential_batch_request import CredentialBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBatchRequest from a JSON string
credential_batch_request_instance = CredentialBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialBatchRequest.to_json())

# convert the object into a dict
credential_batch_request_dict = credential_batch_request_instance.to_dict()
# create an instance of CredentialBatchRequest from a dict
credential_batch_request_from_dict = CredentialBatchRequest.from_dict(credential_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


