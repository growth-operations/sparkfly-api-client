# PostAudiencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | [**Audience**](Audience.md) |  | [optional] 

## Example

```python
from sparkfly.models.post_audiences_request import PostAudiencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAudiencesRequest from a JSON string
post_audiences_request_instance = PostAudiencesRequest.from_json(json)
# print the JSON string representation of the object
print(PostAudiencesRequest.to_json())

# convert the object into a dict
post_audiences_request_dict = post_audiences_request_instance.to_dict()
# create an instance of PostAudiencesRequest from a dict
post_audiences_request_from_dict = PostAudiencesRequest.from_dict(post_audiences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


