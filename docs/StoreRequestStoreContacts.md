# StoreRequestStoreContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**StoreRequestStoreContactsPrimary**](StoreRequestStoreContactsPrimary.md) |  | [optional] 
**secondary** | [**StoreRequestStoreContactsPrimary**](StoreRequestStoreContactsPrimary.md) |  | [optional] 

## Example

```python
from sparkfly_api_client.models.store_request_store_contacts import StoreRequestStoreContacts

# TODO update the JSON string below
json = "{}"
# create an instance of StoreRequestStoreContacts from a JSON string
store_request_store_contacts_instance = StoreRequestStoreContacts.from_json(json)
# print the JSON string representation of the object
print(StoreRequestStoreContacts.to_json())

# convert the object into a dict
store_request_store_contacts_dict = store_request_store_contacts_instance.to_dict()
# create an instance of StoreRequestStoreContacts from a dict
store_request_store_contacts_from_dict = StoreRequestStoreContacts.from_dict(store_request_store_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


