# PostAudiencesIdSubAudiencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaudience** | [**Audience**](Audience.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.post_audiences_id_sub_audiences_request import PostAudiencesIdSubAudiencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAudiencesIdSubAudiencesRequest from a JSON string
post_audiences_id_sub_audiences_request_instance = PostAudiencesIdSubAudiencesRequest.from_json(json)
# print the JSON string representation of the object
print(PostAudiencesIdSubAudiencesRequest.to_json())

# convert the object into a dict
post_audiences_id_sub_audiences_request_dict = post_audiences_id_sub_audiences_request_instance.to_dict()
# create an instance of PostAudiencesIdSubAudiencesRequest from a dict
post_audiences_id_sub_audiences_request_from_dict = PostAudiencesIdSubAudiencesRequest.from_dict(post_audiences_id_sub_audiences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


