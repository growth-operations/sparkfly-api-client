# SubAudienceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaudience** | [**SubAudience**](SubAudience.md) |  | [optional] 
**errors** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.sub_audience_data import SubAudienceData

# TODO update the JSON string below
json = "{}"
# create an instance of SubAudienceData from a JSON string
sub_audience_data_instance = SubAudienceData.from_json(json)
# print the JSON string representation of the object
print(SubAudienceData.to_json())

# convert the object into a dict
sub_audience_data_dict = sub_audience_data_instance.to_dict()
# create an instance of SubAudienceData from a dict
sub_audience_data_from_dict = SubAudienceData.from_dict(sub_audience_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


