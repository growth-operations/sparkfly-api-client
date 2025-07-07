# ClarkAndRiggsIndexBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**clark_and_riggs_products** | [**List[ClarkAndRiggsProductResponseBody]**](ClarkAndRiggsProductResponseBody.md) |  | [optional] 

## Example

```python
from sparkfly.models.clark_and_riggs_index_body import ClarkAndRiggsIndexBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClarkAndRiggsIndexBody from a JSON string
clark_and_riggs_index_body_instance = ClarkAndRiggsIndexBody.from_json(json)
# print the JSON string representation of the object
print(ClarkAndRiggsIndexBody.to_json())

# convert the object into a dict
clark_and_riggs_index_body_dict = clark_and_riggs_index_body_instance.to_dict()
# create an instance of ClarkAndRiggsIndexBody from a dict
clark_and_riggs_index_body_from_dict = ClarkAndRiggsIndexBody.from_dict(clark_and_riggs_index_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


