# CtmTransactionJobRequest

used for ctm update and transaction update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **List[str]** |  | [optional] 
**items** | **List[object]** |  | [optional] 
**purchase_amt** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 
**term_id** | **str** |  | [optional] 
**tran_id** | **str** |  | [optional] 
**receipt_id** | **str** |  | [optional] 
**operator_id** | **str** |  | [optional] 
**business_date** | **str** |  | [optional] 
**translator_id** | **str** |  | [optional] 
**num_guests** | **int** |  | [optional] 
**till_id** | **str** |  | [optional] 
**total_due** | **int** |  | [optional] 
**total_discount** | **int** |  | [optional] 
**total_service** | **int** |  | [optional] 
**total_tax** | **int** |  | [optional] 
**total_paid** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 

## Example

```python
from sparkfly.models.ctm_transaction_job_request import CtmTransactionJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CtmTransactionJobRequest from a JSON string
ctm_transaction_job_request_instance = CtmTransactionJobRequest.from_json(json)
# print the JSON string representation of the object
print(CtmTransactionJobRequest.to_json())

# convert the object into a dict
ctm_transaction_job_request_dict = ctm_transaction_job_request_instance.to_dict()
# create an instance of CtmTransactionJobRequest from a dict
ctm_transaction_job_request_from_dict = CtmTransactionJobRequest.from_dict(ctm_transaction_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


