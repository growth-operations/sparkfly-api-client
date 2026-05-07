# CredentialIndexBody

A paged list of credentials matching a search. Each entry in `credentials` mirrors the shape of `credential_create_response`, with a `credential` object and an `errors` object. Multiple entries may share the same `identifier` — only the entry whose `voided_at` is null is the currently active credential. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**credentials** | [**List[CredentialIndexBodyInner]**](CredentialIndexBodyInner.md) |  | [optional] 

## Example

```python
from sparkfly.models.credential_index_body import CredentialIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialIndexBody from a JSON string
credential_index_body_instance = CredentialIndexBody.from_json(json)
# print the JSON string representation of the object
print(CredentialIndexBody.to_json())

# convert the object into a dict
credential_index_body_dict = credential_index_body_instance.to_dict()
# create an instance of CredentialIndexBody from a dict
credential_index_body_from_dict = CredentialIndexBody.from_dict(credential_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


