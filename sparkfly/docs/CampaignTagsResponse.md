# CampaignTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_channel_tags** | **List[str]** |  | [optional] 

## Example

```python
from sparkfly.models.campaign_tags_response import CampaignTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignTagsResponse from a JSON string
campaign_tags_response_instance = CampaignTagsResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignTagsResponse.to_json())

# convert the object into a dict
campaign_tags_response_dict = campaign_tags_response_instance.to_dict()
# create an instance of CampaignTagsResponse from a dict
campaign_tags_response_from_dict = CampaignTagsResponse.from_dict(campaign_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


