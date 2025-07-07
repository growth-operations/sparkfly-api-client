# MemberProfile

Represents personal identifying information associated with a Sparkfly Member. No fields are required nor guaranteed to be stored. Member profile data may be outsourced to third party client's upon request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The member&#39;s first name. | [optional] 
**last_name** | **str** | The member&#39;s last name. | [optional] 
**phone** | **str** | The member&#39;s contact phone number. | [optional] 
**email** | **str** | The member&#39;s e-mail address. | [optional] 
**birth_month** | **int** | Month of birth expressed as a 1-based index (1 &#x3D; January, 2 &#x3D; February, etc.) | [optional] 
**birth_day** | **int** | The day of the month the member was born. | [optional] 
**custom_data** | **object** | Arbitrary additional data attached to this member&#39;s profile. | [optional] 

## Example

```python
from sparkfly_api_client.models.member_profile import MemberProfile

# TODO update the JSON string below
json = "{}"
# create an instance of MemberProfile from a JSON string
member_profile_instance = MemberProfile.from_json(json)
# print the JSON string representation of the object
print(MemberProfile.to_json())

# convert the object into a dict
member_profile_dict = member_profile_instance.to_dict()
# create an instance of MemberProfile from a dict
member_profile_from_dict = MemberProfile.from_dict(member_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


