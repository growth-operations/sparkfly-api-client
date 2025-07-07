# ImpressionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impression** | [**ImpressionRequestImpression**](ImpressionRequestImpression.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.impression_request import ImpressionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionRequest from a JSON string
impression_request_instance = ImpressionRequest.from_json(json)
# print the JSON string representation of the object
print(ImpressionRequest.to_json())

# convert the object into a dict
impression_request_dict = impression_request_instance.to_dict()
# create an instance of ImpressionRequest from a dict
impression_request_from_dict = ImpressionRequest.from_dict(impression_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


