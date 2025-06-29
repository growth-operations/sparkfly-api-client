# MemberPrivacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberPrivacyMember**](MemberPrivacyMember.md) |  | [optional] 
**credentials** | [**List[MemberPrivacyCredentialsInner]**](MemberPrivacyCredentialsInner.md) |  | [optional] 
**offer_activities** | **List[object]** |  | [optional] 
**transactions** | **List[object]** |  | [optional] 
**impressions** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.member_privacy import MemberPrivacy

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPrivacy from a JSON string
member_privacy_instance = MemberPrivacy.from_json(json)
# print the JSON string representation of the object
print(MemberPrivacy.to_json())

# convert the object into a dict
member_privacy_dict = member_privacy_instance.to_dict()
# create an instance of MemberPrivacy from a dict
member_privacy_from_dict = MemberPrivacy.from_dict(member_privacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


