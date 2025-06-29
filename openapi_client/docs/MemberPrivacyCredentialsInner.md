# MemberPrivacyCredentialsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**offer_ids** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.member_privacy_credentials_inner import MemberPrivacyCredentialsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPrivacyCredentialsInner from a JSON string
member_privacy_credentials_inner_instance = MemberPrivacyCredentialsInner.from_json(json)
# print the JSON string representation of the object
print(MemberPrivacyCredentialsInner.to_json())

# convert the object into a dict
member_privacy_credentials_inner_dict = member_privacy_credentials_inner_instance.to_dict()
# create an instance of MemberPrivacyCredentialsInner from a dict
member_privacy_credentials_inner_from_dict = MemberPrivacyCredentialsInner.from_dict(member_privacy_credentials_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


