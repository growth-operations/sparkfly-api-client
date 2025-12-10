# CreateMemberOfferStatesIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_state** | [**CreateMemberOfferStatesIssueRequestOfferState**](CreateMemberOfferStatesIssueRequestOfferState.md) |  | [optional] 

## Example

```python
from sparkfly.models.create_member_offer_states_issue_request import CreateMemberOfferStatesIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberOfferStatesIssueRequest from a JSON string
create_member_offer_states_issue_request_instance = CreateMemberOfferStatesIssueRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMemberOfferStatesIssueRequest.to_json())

# convert the object into a dict
create_member_offer_states_issue_request_dict = create_member_offer_states_issue_request_instance.to_dict()
# create an instance of CreateMemberOfferStatesIssueRequest from a dict
create_member_offer_states_issue_request_from_dict = CreateMemberOfferStatesIssueRequest.from_dict(create_member_offer_states_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


