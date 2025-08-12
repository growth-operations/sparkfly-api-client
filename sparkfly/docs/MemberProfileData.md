# MemberProfileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_profile** | [**MemberProfile**](MemberProfile.md) |  | 
**errors** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.member_profile_data import MemberProfileData

# TODO update the JSON string below
json = "{}"
# create an instance of MemberProfileData from a JSON string
member_profile_data_instance = MemberProfileData.from_json(json)
# print the JSON string representation of the object
print(MemberProfileData.to_json())

# convert the object into a dict
member_profile_data_dict = member_profile_data_instance.to_dict()
# create an instance of MemberProfileData from a dict
member_profile_data_from_dict = MemberProfileData.from_dict(member_profile_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


