# MemberIndexBody


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
from sparkfly.models.member_index_body import MemberIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of MemberIndexBody from a JSON string
member_index_body_instance = MemberIndexBody.from_json(json)
# print the JSON string representation of the object
print(MemberIndexBody.to_json())

# convert the object into a dict
member_index_body_dict = member_index_body_instance.to_dict()
# create an instance of MemberIndexBody from a dict
member_index_body_from_dict = MemberIndexBody.from_dict(member_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


