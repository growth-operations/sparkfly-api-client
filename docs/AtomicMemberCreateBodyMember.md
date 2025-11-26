# AtomicMemberCreateBodyMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**member_profile** | [**AtomicMemberCreateBodyMemberMemberProfile**](AtomicMemberCreateBodyMemberMemberProfile.md) |  | [optional] 
**credentials** | [**List[AtomicMemberCreateBodyMemberCredentialsInner]**](AtomicMemberCreateBodyMemberCredentialsInner.md) |  | [optional] 
**loyalty_enrollments** | [**List[AtomicMemberCreateBodyMemberLoyaltyEnrollmentsInner]**](AtomicMemberCreateBodyMemberLoyaltyEnrollmentsInner.md) |  | [optional] 

## Example

```python
from sparkfly.models.atomic_member_create_body_member import AtomicMemberCreateBodyMember

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicMemberCreateBodyMember from a JSON string
atomic_member_create_body_member_instance = AtomicMemberCreateBodyMember.from_json(json)
# print the JSON string representation of the object
print(AtomicMemberCreateBodyMember.to_json())

# convert the object into a dict
atomic_member_create_body_member_dict = atomic_member_create_body_member_instance.to_dict()
# create an instance of AtomicMemberCreateBodyMember from a dict
atomic_member_create_body_member_from_dict = AtomicMemberCreateBodyMember.from_dict(atomic_member_create_body_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


