# CtmRedemptionJobRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ln** | **str** |  | [optional] 
**lln** | **str** |  | [optional] 
**entry_id** | **str** |  | [optional] 
**linked_entry_id** | **str** |  | [optional] 
**cat** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**ic** | **str** |  | [optional] 
**qw** | **int** |  | [optional] 
**original_qw** | **int** |  | [optional] 
**price** | **int** |  | [optional] 
**original_price** | **int** |  | [optional] 
**disc_val** | **int** |  | [optional] 
**seat** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**voided** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ctm_redemption_job_request_items_inner import CtmRedemptionJobRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CtmRedemptionJobRequestItemsInner from a JSON string
ctm_redemption_job_request_items_inner_instance = CtmRedemptionJobRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(CtmRedemptionJobRequestItemsInner.to_json())

# convert the object into a dict
ctm_redemption_job_request_items_inner_dict = ctm_redemption_job_request_items_inner_instance.to_dict()
# create an instance of CtmRedemptionJobRequestItemsInner from a dict
ctm_redemption_job_request_items_inner_from_dict = CtmRedemptionJobRequestItemsInner.from_dict(ctm_redemption_job_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


