# CredentialCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printable** | **bool** |  | [optional] 
**credential** | [**CredentialCreateRequestCredential**](CredentialCreateRequestCredential.md) |  | [optional] 

## Example

```python
from sparkfly.models.credential_create_request import CredentialCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialCreateRequest from a JSON string
credential_create_request_instance = CredentialCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialCreateRequest.to_json())

# convert the object into a dict
credential_create_request_dict = credential_create_request_instance.to_dict()
# create an instance of CredentialCreateRequest from a dict
credential_create_request_from_dict = CredentialCreateRequest.from_dict(credential_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


