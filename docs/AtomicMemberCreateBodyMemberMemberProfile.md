# AtomicMemberCreateBodyMemberMemberProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**birth_month** | **int** |  | [optional] 
**birth_day** | **int** |  | [optional] 
**custom_data** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.atomic_member_create_body_member_member_profile import AtomicMemberCreateBodyMemberMemberProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicMemberCreateBodyMemberMemberProfile from a JSON string
atomic_member_create_body_member_member_profile_instance = AtomicMemberCreateBodyMemberMemberProfile.from_json(json)
# print the JSON string representation of the object
print(AtomicMemberCreateBodyMemberMemberProfile.to_json())

# convert the object into a dict
atomic_member_create_body_member_member_profile_dict = atomic_member_create_body_member_member_profile_instance.to_dict()
# create an instance of AtomicMemberCreateBodyMemberMemberProfile from a dict
atomic_member_create_body_member_member_profile_from_dict = AtomicMemberCreateBodyMemberMemberProfile.from_dict(atomic_member_create_body_member_member_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


