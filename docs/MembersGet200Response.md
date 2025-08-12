# MembersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**members** | [**List[Member]**](Member.md) |  | [optional] 

## Example

```python
from sparkfly.models.members_get200_response import MembersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MembersGet200Response from a JSON string
members_get200_response_instance = MembersGet200Response.from_json(json)
# print the JSON string representation of the object
print(MembersGet200Response.to_json())

# convert the object into a dict
members_get200_response_dict = members_get200_response_instance.to_dict()
# create an instance of MembersGet200Response from a dict
members_get200_response_from_dict = MembersGet200Response.from_dict(members_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


