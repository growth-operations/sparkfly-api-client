# ClarkAndRiggsProductCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_channel_id** | **int** |  | [optional] 
**offer_id** | **int** |  | [optional] 
**product_id** | **str** |  | [optional] 
**book_size** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.clark_and_riggs_product_create_body import ClarkAndRiggsProductCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClarkAndRiggsProductCreateBody from a JSON string
clark_and_riggs_product_create_body_instance = ClarkAndRiggsProductCreateBody.from_json(json)
# print the JSON string representation of the object
print(ClarkAndRiggsProductCreateBody.to_json())

# convert the object into a dict
clark_and_riggs_product_create_body_dict = clark_and_riggs_product_create_body_instance.to_dict()
# create an instance of ClarkAndRiggsProductCreateBody from a dict
clark_and_riggs_product_create_body_from_dict = ClarkAndRiggsProductCreateBody.from_dict(clark_and_riggs_product_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


