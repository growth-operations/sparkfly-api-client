# GetAudiences200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**audiences** | [**List[AudienceData]**](AudienceData.md) |  | [optional] 

## Example

```python
from sparkfly.models.get_audiences200_response import GetAudiences200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAudiences200Response from a JSON string
get_audiences200_response_instance = GetAudiences200Response.from_json(json)
# print the JSON string representation of the object
print(GetAudiences200Response.to_json())

# convert the object into a dict
get_audiences200_response_dict = get_audiences200_response_instance.to_dict()
# create an instance of GetAudiences200Response from a dict
get_audiences200_response_from_dict = GetAudiences200Response.from_dict(get_audiences200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


