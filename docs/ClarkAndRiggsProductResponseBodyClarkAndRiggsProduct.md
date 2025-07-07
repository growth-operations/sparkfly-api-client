# ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**offer** | [**ClarkAndRiggsProductResponseBodyClarkAndRiggsProductOffer**](ClarkAndRiggsProductResponseBodyClarkAndRiggsProductOffer.md) |  | [optional] 
**eligible_channel** | [**ClarkAndRiggsProductResponseBodyClarkAndRiggsProductOffer**](ClarkAndRiggsProductResponseBodyClarkAndRiggsProductOffer.md) |  | [optional] 
**product_id** | **str** |  | [optional] 
**book_size** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from sparkfly_api_client.models.clark_and_riggs_product_response_body_clark_and_riggs_product import ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct from a JSON string
clark_and_riggs_product_response_body_clark_and_riggs_product_instance = ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct.from_json(json)
# print the JSON string representation of the object
print(ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct.to_json())

# convert the object into a dict
clark_and_riggs_product_response_body_clark_and_riggs_product_dict = clark_and_riggs_product_response_body_clark_and_riggs_product_instance.to_dict()
# create an instance of ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct from a dict
clark_and_riggs_product_response_body_clark_and_riggs_product_from_dict = ClarkAndRiggsProductResponseBodyClarkAndRiggsProduct.from_dict(clark_and_riggs_product_response_body_clark_and_riggs_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


