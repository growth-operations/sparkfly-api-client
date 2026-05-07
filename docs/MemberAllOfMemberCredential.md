# MemberAllOfMemberCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**channel_id** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.member_all_of_member_credential import MemberAllOfMemberCredential

# TODO update the JSON string below
json = "{}"
# create an instance of MemberAllOfMemberCredential from a JSON string
member_all_of_member_credential_instance = MemberAllOfMemberCredential.from_json(json)
# print the JSON string representation of the object
print(MemberAllOfMemberCredential.to_json())

# convert the object into a dict
member_all_of_member_credential_dict = member_all_of_member_credential_instance.to_dict()
# create an instance of MemberAllOfMemberCredential from a dict
member_all_of_member_credential_from_dict = MemberAllOfMemberCredential.from_dict(member_all_of_member_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


