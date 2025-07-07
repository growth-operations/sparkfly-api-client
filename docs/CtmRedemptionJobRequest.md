# CtmRedemptionJobRequest

used for ctm show

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | **List[int]** |  | [optional] 
**redeemed_offers** | [**List[CtmRedemptionJobRequestRedeemedOffersInner]**](CtmRedemptionJobRequestRedeemedOffersInner.md) |  | [optional] 
**items** | [**List[CtmRedemptionJobRequestItemsInner]**](CtmRedemptionJobRequestItemsInner.md) |  | [optional] 
**credentials** | **List[str]** |  | [optional] 
**purchase_amt** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 
**store_number** | **str** |  | [optional] 
**credential** | **str** |  | [optional] 
**term_id** | **str** |  | [optional] 
**tran_id** | **str** |  | [optional] 
**external_transaction_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**reciept_id** | **str** |  | [optional] 
**business_date** | **str** |  | [optional] 
**translator_id** | **str** |  | [optional] 
**num_guests** | **int** |  | [optional] 
**till_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_due** | **int** |  | [optional] 
**total_discount** | **int** |  | [optional] 
**total_service** | **int** |  | [optional] 
**total_tax** | **int** |  | [optional] 
**total_paid** | **int** |  | [optional] 
**pos_vendor** | **str** |  | [optional] 
**pos_version** | **str** |  | [optional] 
**selected_offers** | [**List[CtmRedemptionJobRequestSelectedOffersInner]**](CtmRedemptionJobRequestSelectedOffersInner.md) |  | [optional] 
**revenue_center** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.ctm_redemption_job_request import CtmRedemptionJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CtmRedemptionJobRequest from a JSON string
ctm_redemption_job_request_instance = CtmRedemptionJobRequest.from_json(json)
# print the JSON string representation of the object
print(CtmRedemptionJobRequest.to_json())

# convert the object into a dict
ctm_redemption_job_request_dict = ctm_redemption_job_request_instance.to_dict()
# create an instance of CtmRedemptionJobRequest from a dict
ctm_redemption_job_request_from_dict = CtmRedemptionJobRequest.from_dict(ctm_redemption_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


