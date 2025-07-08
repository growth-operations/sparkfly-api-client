# CampaignIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**campaigns** | [**List[CampaignResponse]**](CampaignResponse.md) |  | [optional] 

## Example

```python
from sparkfly.models.campaign_index_body import CampaignIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignIndexBody from a JSON string
campaign_index_body_instance = CampaignIndexBody.from_json(json)
# print the JSON string representation of the object
print(CampaignIndexBody.to_json())

# convert the object into a dict
campaign_index_body_dict = campaign_index_body_instance.to_dict()
# create an instance of CampaignIndexBody from a dict
campaign_index_body_from_dict = CampaignIndexBody.from_dict(campaign_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


