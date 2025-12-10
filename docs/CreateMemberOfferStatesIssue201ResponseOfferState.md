# CreateMemberOfferStatesIssue201ResponseOfferState

The newly created offer_state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID of the offer_state. | 
**member_id** | **int** | The member ID the offer_state was issued to. | 
**offer_id** | **int** | The ID of the offer that was issued to the member. | 
**campaign_id** | **str** | The Campaign XID of the campaign that was used to perform the issuance. | 
**activates_at** | **datetime** | When the offer_state will become redeemable at the POS, if specified in the request. | [optional] 
**expires_at** | **datetime** | When the offer_state will stop being redeemable at the POS, if specified in the request. | [optional] 
**credential_identifier** | **str** | The credential identifier that can be entered or scanned at the POS to redeem the issued offer_state. | 

## Example

```python
from sparkfly.models.create_member_offer_states_issue201_response_offer_state import CreateMemberOfferStatesIssue201ResponseOfferState

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberOfferStatesIssue201ResponseOfferState from a JSON string
create_member_offer_states_issue201_response_offer_state_instance = CreateMemberOfferStatesIssue201ResponseOfferState.from_json(json)
# print the JSON string representation of the object
print(CreateMemberOfferStatesIssue201ResponseOfferState.to_json())

# convert the object into a dict
create_member_offer_states_issue201_response_offer_state_dict = create_member_offer_states_issue201_response_offer_state_instance.to_dict()
# create an instance of CreateMemberOfferStatesIssue201ResponseOfferState from a dict
create_member_offer_states_issue201_response_offer_state_from_dict = CreateMemberOfferStatesIssue201ResponseOfferState.from_dict(create_member_offer_states_issue201_response_offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


