# CtmQitemsRequest

dd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_id** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**instant** | **str** |  | [optional] 
**line_number** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**desc_short** | **str** |  | [optional] 
**desc_long** | **str** |  | [optional] 
**items** | **List[object]** |  | [optional] 
**value** | **int** |  | [optional] 
**tip** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**voided** | **bool** |  | [optional] 
**sparkfly_identifier** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**auth** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 

## Example

```python
from sparkfly.models.ctm_qitems_request import CtmQitemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CtmQitemsRequest from a JSON string
ctm_qitems_request_instance = CtmQitemsRequest.from_json(json)
# print the JSON string representation of the object
print(CtmQitemsRequest.to_json())

# convert the object into a dict
ctm_qitems_request_dict = ctm_qitems_request_instance.to_dict()
# create an instance of CtmQitemsRequest from a dict
ctm_qitems_request_from_dict = CtmQitemsRequest.from_dict(ctm_qitems_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


