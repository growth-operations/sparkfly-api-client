# CampaignRequestCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**pos_offer_code** | **str** |  | [optional] 
**code_ref** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**start_display_at** | **str** |  | [optional] 
**stop_display_at** | **str** |  | [optional] 
**finding_source** | **str** |  | [optional] 
**eligible_store_numbers** | **List[str]** |  | [optional] 
**eligible_storelist_numbers** | **List[object]** |  | [optional] 
**landing_page_image_template_id** | **str** |  | [optional] 
**description_template_id** | **str** |  | [optional] 
**terms_and_conditions_template_id** | **str** |  | [optional] 
**code_count** | **str** |  | [optional] 
**redemption_allowed** | **str** |  | [optional] 
**sub_audience_id** | **int** |  | [optional] 
**audience_id** | **int** |  | [optional] 
**redemption_grace_period** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.campaign_request_campaign import CampaignRequestCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRequestCampaign from a JSON string
campaign_request_campaign_instance = CampaignRequestCampaign.from_json(json)
# print the JSON string representation of the object
print(CampaignRequestCampaign.to_json())

# convert the object into a dict
campaign_request_campaign_dict = campaign_request_campaign_instance.to_dict()
# create an instance of CampaignRequestCampaign from a dict
campaign_request_campaign_from_dict = CampaignRequestCampaign.from_dict(campaign_request_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


