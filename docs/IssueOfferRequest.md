# IssueOfferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state** | [**IssueOfferRequestOfferState**](IssueOfferRequestOfferState.md) |  | [optional] 

## Example

```python
from sparkfly.models.issue_offer_request import IssueOfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueOfferRequest from a JSON string
issue_offer_request_instance = IssueOfferRequest.from_json(json)
# print the JSON string representation of the object
print(IssueOfferRequest.to_json())

# convert the object into a dict
issue_offer_request_dict = issue_offer_request_instance.to_dict()
# create an instance of IssueOfferRequest from a dict
issue_offer_request_from_dict = IssueOfferRequest.from_dict(issue_offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


