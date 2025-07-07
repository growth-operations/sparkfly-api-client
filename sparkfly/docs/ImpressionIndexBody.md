# ImpressionIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**impressions** | [**List[Impression]**](Impression.md) |  | [optional] 

## Example

```python
from sparkfly.models.impression_index_body import ImpressionIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of ImpressionIndexBody from a JSON string
impression_index_body_instance = ImpressionIndexBody.from_json(json)
# print the JSON string representation of the object
print(ImpressionIndexBody.to_json())

# convert the object into a dict
impression_index_body_dict = impression_index_body_instance.to_dict()
# create an instance of ImpressionIndexBody from a dict
impression_index_body_from_dict = ImpressionIndexBody.from_dict(impression_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


