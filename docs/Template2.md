# Template2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **object** |  | [optional] 
**template_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**options** | **str** |  | [optional] 

## Example

```python
from sparkfly_api_client.models.template2 import Template2

# TODO update the JSON string below
json = "{}"
# create an instance of Template2 from a JSON string
template2_instance = Template2.from_json(json)
# print the JSON string representation of the object
print(Template2.to_json())

# convert the object into a dict
template2_dict = template2_instance.to_dict()
# create an instance of Template2 from a dict
template2_from_dict = Template2.from_dict(template2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


