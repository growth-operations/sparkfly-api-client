# CreateAudienceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | [**Audience**](Audience.md) |  | [optional] 

## Example

```python
from sparkfly.models.create_audience_request import CreateAudienceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAudienceRequest from a JSON string
create_audience_request_instance = CreateAudienceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAudienceRequest.to_json())

# convert the object into a dict
create_audience_request_dict = create_audience_request_instance.to_dict()
# create an instance of CreateAudienceRequest from a dict
create_audience_request_from_dict = CreateAudienceRequest.from_dict(create_audience_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


