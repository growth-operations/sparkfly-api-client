# CreateSubAudienceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaudience** | [**Audience**](Audience.md) |  | [optional] 

## Example

```python
from sparkfly.models.create_sub_audience_request import CreateSubAudienceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubAudienceRequest from a JSON string
create_sub_audience_request_instance = CreateSubAudienceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubAudienceRequest.to_json())

# convert the object into a dict
create_sub_audience_request_dict = create_sub_audience_request_instance.to_dict()
# create an instance of CreateSubAudienceRequest from a dict
create_sub_audience_request_from_dict = CreateSubAudienceRequest.from_dict(create_sub_audience_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


