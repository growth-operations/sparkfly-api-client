# MemberAllOfMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**notification_mode** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.member_all_of_member import MemberAllOfMember

# TODO update the JSON string below
json = "{}"
# create an instance of MemberAllOfMember from a JSON string
member_all_of_member_instance = MemberAllOfMember.from_json(json)
# print the JSON string representation of the object
print(MemberAllOfMember.to_json())

# convert the object into a dict
member_all_of_member_dict = member_all_of_member_instance.to_dict()
# create an instance of MemberAllOfMember from a dict
member_all_of_member_from_dict = MemberAllOfMember.from_dict(member_all_of_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


