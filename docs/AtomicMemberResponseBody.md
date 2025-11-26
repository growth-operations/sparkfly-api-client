# AtomicMemberResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**AtomicMemberResponseBodyMember**](AtomicMemberResponseBodyMember.md) |  | [optional] 

## Example

```python
from sparkfly.models.atomic_member_response_body import AtomicMemberResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AtomicMemberResponseBody from a JSON string
atomic_member_response_body_instance = AtomicMemberResponseBody.from_json(json)
# print the JSON string representation of the object
print(AtomicMemberResponseBody.to_json())

# convert the object into a dict
atomic_member_response_body_dict = atomic_member_response_body_instance.to_dict()
# create an instance of AtomicMemberResponseBody from a dict
atomic_member_response_body_from_dict = AtomicMemberResponseBody.from_dict(atomic_member_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


