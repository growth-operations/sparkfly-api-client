# IssueOfferRequestOfferState

The offer_state to issue to the member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ref_id** | **str** | An external reference identifier that will be attached to the offer_state. Meaning and value are not specified and may be useful for external systems that wish to attach data to an offer_state. | [optional] 
**campaign_id** | **str** | The Sparkfly campaign XID to use when issuing the offer_state. Must be an active (non-suspended) campaign under an active offer. | 
**activates_at** | **datetime** | When the issued offer should become redeemable at the POS. | [optional] 
**expires_at** | **datetime** | When the issued offer should stop being redeemable at the POS. | [optional] 
**member_identifier** | **str** | The member&#39;s external identifier. This field is required if member_id is absent. | [optional] 
**member_id** | **int** | The primary identifier of the member. This field is required if member_identifier is absent. | [optional] 

## Example

```python
from sparkfly.models.issue_offer_request_offer_state import IssueOfferRequestOfferState

# TODO update the JSON string below
json = "{}"
# create an instance of IssueOfferRequestOfferState from a JSON string
issue_offer_request_offer_state_instance = IssueOfferRequestOfferState.from_json(json)
# print the JSON string representation of the object
print(IssueOfferRequestOfferState.to_json())

# convert the object into a dict
issue_offer_request_offer_state_dict = issue_offer_request_offer_state_instance.to_dict()
# create an instance of IssueOfferRequestOfferState from a dict
issue_offer_request_offer_state_from_dict = IssueOfferRequestOfferState.from_dict(issue_offer_request_offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


