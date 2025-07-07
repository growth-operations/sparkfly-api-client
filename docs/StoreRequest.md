# StoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**StoreRequestStore**](StoreRequestStore.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.store_request import StoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreRequest from a JSON string
store_request_instance = StoreRequest.from_json(json)
# print the JSON string representation of the object
print(StoreRequest.to_json())

# convert the object into a dict
store_request_dict = store_request_instance.to_dict()
# create an instance of StoreRequest from a dict
store_request_from_dict = StoreRequest.from_dict(store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


