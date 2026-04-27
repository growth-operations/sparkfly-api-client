# CredentialIndexBodyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**CredentialIndexBodyInnerCredential**](CredentialIndexBodyInnerCredential.md) |  | 
**errors** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.credential_index_body_inner import CredentialIndexBodyInner

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialIndexBodyInner from a JSON string
credential_index_body_inner_instance = CredentialIndexBodyInner.from_json(json)
# print the JSON string representation of the object
print(CredentialIndexBodyInner.to_json())

# convert the object into a dict
credential_index_body_inner_dict = credential_index_body_inner_instance.to_dict()
# create an instance of CredentialIndexBodyInner from a dict
credential_index_body_inner_from_dict = CredentialIndexBodyInner.from_dict(credential_index_body_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


