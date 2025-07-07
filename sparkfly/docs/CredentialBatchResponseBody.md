# CredentialBatchResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_batch** | [**CredentialBatchResponseBodyCredentialBatch**](CredentialBatchResponseBodyCredentialBatch.md) |  | [optional] 

## Example

```python
from sparkfly.models.credential_batch_response_body import CredentialBatchResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBatchResponseBody from a JSON string
credential_batch_response_body_instance = CredentialBatchResponseBody.from_json(json)
# print the JSON string representation of the object
print(CredentialBatchResponseBody.to_json())

# convert the object into a dict
credential_batch_response_body_dict = credential_batch_response_body_instance.to_dict()
# create an instance of CredentialBatchResponseBody from a dict
credential_batch_response_body_from_dict = CredentialBatchResponseBody.from_dict(credential_batch_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


