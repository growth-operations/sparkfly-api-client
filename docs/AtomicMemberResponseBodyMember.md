# AtomicMemberResponseBodyMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**identifier** | **str** |  | 
**member_profile** | [**AtomicMemberResponseBodyMemberMemberProfile**](AtomicMemberResponseBodyMemberMemberProfile.md) |  | [optional] 
**credentials** | [**List[AtomicMemberResponseBodyMemberCredentialsInner]**](AtomicMemberResponseBodyMemberCredentialsInner.md) |  | [optional] 
**loyalty_enrollments** | [**List[AtomicMemberResponseBodyMemberLoyaltyEnrollmentsInner]**](AtomicMemberResponseBodyMemberLoyaltyEnrollmentsInner.md) |  | [optional] 

## Example

```python
from sparkfly.models.atomic_member_response_body_member import AtomicMemberResponseBodyMember

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicMemberResponseBodyMember from a JSON string
atomic_member_response_body_member_instance = AtomicMemberResponseBodyMember.from_json(json)
# print the JSON string representation of the object
print(AtomicMemberResponseBodyMember.to_json())

# convert the object into a dict
atomic_member_response_body_member_dict = atomic_member_response_body_member_instance.to_dict()
# create an instance of AtomicMemberResponseBodyMember from a dict
atomic_member_response_body_member_from_dict = AtomicMemberResponseBodyMember.from_dict(atomic_member_response_body_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


