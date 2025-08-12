# AudienceIndexData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | [**List[AudienceData]**](AudienceData.md) |  | 

## Example

```python
from sparkfly.models.audience_index_data import AudienceIndexData

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceIndexData from a JSON string
audience_index_data_instance = AudienceIndexData.from_json(json)
# print the JSON string representation of the object
print(AudienceIndexData.to_json())

# convert the object into a dict
audience_index_data_dict = audience_index_data_instance.to_dict()
# create an instance of AudienceIndexData from a dict
audience_index_data_from_dict = AudienceIndexData.from_dict(audience_index_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


