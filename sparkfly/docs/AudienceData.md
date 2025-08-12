# AudienceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | [**Audience**](Audience.md) |  | 
**errors** | **object** |  | [optional] 

## Example

```python
from sparkfly.models.audience_data import AudienceData

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceData from a JSON string
audience_data_instance = AudienceData.from_json(json)
# print the JSON string representation of the object
print(AudienceData.to_json())

# convert the object into a dict
audience_data_dict = audience_data_instance.to_dict()
# create an instance of AudienceData from a dict
audience_data_from_dict = AudienceData.from_dict(audience_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


