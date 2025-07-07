# MemberPrivacyMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.member_privacy_member import MemberPrivacyMember

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPrivacyMember from a JSON string
member_privacy_member_instance = MemberPrivacyMember.from_json(json)
# print the JSON string representation of the object
print(MemberPrivacyMember.to_json())

# convert the object into a dict
member_privacy_member_dict = member_privacy_member_instance.to_dict()
# create an instance of MemberPrivacyMember from a dict
member_privacy_member_from_dict = MemberPrivacyMember.from_dict(member_privacy_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


