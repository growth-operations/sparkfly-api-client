# CredentialBatchIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**credential_batches** | [**List[CredentialBatchResponseBody]**](CredentialBatchResponseBody.md) |  | [optional] 

## Example

```python
from sparkfly.models.credential_batch_index_body import CredentialBatchIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialBatchIndexBody from a JSON string
credential_batch_index_body_instance = CredentialBatchIndexBody.from_json(json)
# print the JSON string representation of the object
print(CredentialBatchIndexBody.to_json())

# convert the object into a dict
credential_batch_index_body_dict = credential_batch_index_body_instance.to_dict()
# create an instance of CredentialBatchIndexBody from a dict
credential_batch_index_body_from_dict = CredentialBatchIndexBody.from_dict(credential_batch_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


