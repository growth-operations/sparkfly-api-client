# MemberRequestMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**notification_mode** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.member_request_member import MemberRequestMember

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRequestMember from a JSON string
member_request_member_instance = MemberRequestMember.from_json(json)
# print the JSON string representation of the object
print(MemberRequestMember.to_json())

# convert the object into a dict
member_request_member_dict = member_request_member_instance.to_dict()
# create an instance of MemberRequestMember from a dict
member_request_member_from_dict = MemberRequestMember.from_dict(member_request_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


