# SubAudienceIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**subaudiences** | [**List[SubAudienceData]**](SubAudienceData.md) |  | 

## Example

```python
from sparkfly.models.sub_audience_index_body import SubAudienceIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubAudienceIndexBody from a JSON string
sub_audience_index_body_instance = SubAudienceIndexBody.from_json(json)
# print the JSON string representation of the object
print(SubAudienceIndexBody.to_json())

# convert the object into a dict
sub_audience_index_body_dict = sub_audience_index_body_instance.to_dict()
# create an instance of SubAudienceIndexBody from a dict
sub_audience_index_body_from_dict = SubAudienceIndexBody.from_dict(sub_audience_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


