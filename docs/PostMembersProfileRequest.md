# PostMembersProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_profile** | [**MemberProfile**](MemberProfile.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.post_members_profile_request import PostMembersProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMembersProfileRequest from a JSON string
post_members_profile_request_instance = PostMembersProfileRequest.from_json(json)
# print the JSON string representation of the object
print(PostMembersProfileRequest.to_json())

# convert the object into a dict
post_members_profile_request_dict = post_members_profile_request_instance.to_dict()
# create an instance of PostMembersProfileRequest from a dict
post_members_profile_request_from_dict = PostMembersProfileRequest.from_dict(post_members_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


