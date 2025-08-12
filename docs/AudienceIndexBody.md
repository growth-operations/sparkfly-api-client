# AudienceIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**audiences** | [**List[AudienceData]**](AudienceData.md) |  | 

## Example

```python
from sparkfly.models.audience_index_body import AudienceIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceIndexBody from a JSON string
audience_index_body_instance = AudienceIndexBody.from_json(json)
# print the JSON string representation of the object
print(AudienceIndexBody.to_json())

# convert the object into a dict
audience_index_body_dict = audience_index_body_instance.to_dict()
# create an instance of AudienceIndexBody from a dict
audience_index_body_from_dict = AudienceIndexBody.from_dict(audience_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


