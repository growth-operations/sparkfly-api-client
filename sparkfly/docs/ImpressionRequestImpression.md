# ImpressionRequestImpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie_id** | **str** |  | 
**offer_xid** | **str** |  | 
**annotations** | [**ImpressionRequestImpressionAnnotations**](ImpressionRequestImpressionAnnotations.md) |  | [optional] 

## Example

```python
from sparkfly.models.impression_request_impression import ImpressionRequestImpression

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionRequestImpression from a JSON string
impression_request_impression_instance = ImpressionRequestImpression.from_json(json)
# print the JSON string representation of the object
print(ImpressionRequestImpression.to_json())

# convert the object into a dict
impression_request_impression_dict = impression_request_impression_instance.to_dict()
# create an instance of ImpressionRequestImpression from a dict
impression_request_impression_from_dict = ImpressionRequestImpression.from_dict(impression_request_impression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


