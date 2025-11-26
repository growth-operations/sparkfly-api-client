# AtomicMemberCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**AtomicMemberCreateBodyMember**](AtomicMemberCreateBodyMember.md) |  | [optional] 

## Example

```python
from sparkfly.models.atomic_member_create_body import AtomicMemberCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicMemberCreateBody from a JSON string
atomic_member_create_body_instance = AtomicMemberCreateBody.from_json(json)
# print the JSON string representation of the object
print(AtomicMemberCreateBody.to_json())

# convert the object into a dict
atomic_member_create_body_dict = atomic_member_create_body_instance.to_dict()
# create an instance of AtomicMemberCreateBody from a dict
atomic_member_create_body_from_dict = AtomicMemberCreateBody.from_dict(atomic_member_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


