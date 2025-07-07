# ImpressionAllOfImpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie_id** | **str** |  | [optional] 
**offer_xid** | **str** |  | [optional] 
**annotations** | [**ImpressionRequestImpressionAnnotations**](ImpressionRequestImpressionAnnotations.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**creative_name** | **str** |  | [optional] 
**errors** | [**Errors**](Errors.md) |  | [optional] 

## Example

```python
from sparkfly.models.impression_all_of_impression import ImpressionAllOfImpression

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionAllOfImpression from a JSON string
impression_all_of_impression_instance = ImpressionAllOfImpression.from_json(json)
# print the JSON string representation of the object
print(ImpressionAllOfImpression.to_json())

# convert the object into a dict
impression_all_of_impression_dict = impression_all_of_impression_instance.to_dict()
# create an instance of ImpressionAllOfImpression from a dict
impression_all_of_impression_from_dict = ImpressionAllOfImpression.from_dict(impression_all_of_impression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


