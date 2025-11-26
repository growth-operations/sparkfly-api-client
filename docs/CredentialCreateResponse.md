# CredentialCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**CredentialCreateResponseCredential**](CredentialCreateResponseCredential.md) |  | [optional] 

## Example

```python
from sparkfly.models.credential_create_response import CredentialCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialCreateResponse from a JSON string
credential_create_response_instance = CredentialCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialCreateResponse.to_json())

# convert the object into a dict
credential_create_response_dict = credential_create_response_instance.to_dict()
# create an instance of CredentialCreateResponse from a dict
credential_create_response_from_dict = CredentialCreateResponse.from_dict(credential_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


