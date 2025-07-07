# PostMembersIdOfferStatesIssue201ResponseOfferState

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
from sparkfly_api_client.models.post_members_id_offer_states_issue201_response_offer_state import PostMembersIdOfferStatesIssue201ResponseOfferState

# TODO update the JSON string below
json = "{}"
# create an instance of PostMembersIdOfferStatesIssue201ResponseOfferState from a JSON string
post_members_id_offer_states_issue201_response_offer_state_instance = PostMembersIdOfferStatesIssue201ResponseOfferState.from_json(json)
# print the JSON string representation of the object
print(PostMembersIdOfferStatesIssue201ResponseOfferState.to_json())

# convert the object into a dict
post_members_id_offer_states_issue201_response_offer_state_dict = post_members_id_offer_states_issue201_response_offer_state_instance.to_dict()
# create an instance of PostMembersIdOfferStatesIssue201ResponseOfferState from a dict
post_members_id_offer_states_issue201_response_offer_state_from_dict = PostMembersIdOfferStatesIssue201ResponseOfferState.from_dict(post_members_id_offer_states_issue201_response_offer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


