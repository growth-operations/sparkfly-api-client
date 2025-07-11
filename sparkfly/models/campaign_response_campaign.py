# coding: utf-8

"""
    Core Operations

    The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API.  The Sparkfly documentation site is under development. If the documentation you're after isn't available here, please contact support@sparkfly.com and we will get you what you need.

    The version of the OpenAPI document: 1.0
    Contact: support@sparkfly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CampaignResponseCampaign(BaseModel):
    """
    CampaignResponseCampaign
    """ # noqa: E501
    id: Optional[StrictInt] = None
    xid: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    code_ref: Optional[StrictStr] = None
    code_count: Optional[StrictStr] = None
    external_id: Optional[StrictStr] = None
    offer_id: Optional[StrictInt] = None
    channel_id: Optional[StrictInt] = None
    channel_name: Optional[StrictStr] = None
    pos_offer_code: Optional[StrictStr] = None
    online_offer_code: Optional[StrictStr] = None
    activation_date: Optional[StrictStr] = None
    expiration_date: Optional[StrictStr] = None
    start_display_at: Optional[StrictStr] = None
    funding_source: Optional[StrictStr] = None
    eligible_channel_tags: Optional[List[Dict[str, Any]]] = None
    eligible_store_ids: Optional[List[Dict[str, Any]]] = None
    eligible_store_numbers: Optional[List[Dict[str, Any]]] = None
    eligible_storelist_ids: Optional[List[Dict[str, Any]]] = None
    eligible_storelist_numbers: Optional[List[Dict[str, Any]]] = None
    landing_page_image_template_id: Optional[StrictStr] = None
    description_template_id: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    terms_and_conditions_template_id: Optional[StrictStr] = None
    terms_and_conditions: Optional[StrictStr] = None
    security: Optional[StrictStr] = None
    landing_page_urls: Optional[Dict[str, Any]] = None
    allow_return_later: Optional[StrictBool] = None
    redemption_identifier_type: Optional[StrictInt] = None
    member_required: Optional[StrictBool] = None
    max_redemptions_per_member: Optional[StrictStr] = None
    dynamic_expiration: Optional[StrictStr] = None
    sub_audience_id: Optional[StrictInt] = None
    audience_id: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    redemption_grace_period: Optional[Annotated[int, Field(multiple_of=60, strict=True)]] = None
    __properties: ClassVar[List[str]] = ["id", "xid", "name", "code_ref", "code_count", "external_id", "offer_id", "channel_id", "channel_name", "pos_offer_code", "online_offer_code", "activation_date", "expiration_date", "start_display_at", "funding_source", "eligible_channel_tags", "eligible_store_ids", "eligible_store_numbers", "eligible_storelist_ids", "eligible_storelist_numbers", "landing_page_image_template_id", "description_template_id", "description", "terms_and_conditions_template_id", "terms_and_conditions", "security", "landing_page_urls", "allow_return_later", "redemption_identifier_type", "member_required", "max_redemptions_per_member", "dynamic_expiration", "sub_audience_id", "audience_id", "status", "redemption_grace_period"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CampaignResponseCampaign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignResponseCampaign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "xid": obj.get("xid"),
            "name": obj.get("name"),
            "code_ref": obj.get("code_ref"),
            "code_count": obj.get("code_count"),
            "external_id": obj.get("external_id"),
            "offer_id": obj.get("offer_id"),
            "channel_id": obj.get("channel_id"),
            "channel_name": obj.get("channel_name"),
            "pos_offer_code": obj.get("pos_offer_code"),
            "online_offer_code": obj.get("online_offer_code"),
            "activation_date": obj.get("activation_date"),
            "expiration_date": obj.get("expiration_date"),
            "start_display_at": obj.get("start_display_at"),
            "funding_source": obj.get("funding_source"),
            "eligible_channel_tags": obj.get("eligible_channel_tags"),
            "eligible_store_ids": obj.get("eligible_store_ids"),
            "eligible_store_numbers": obj.get("eligible_store_numbers"),
            "eligible_storelist_ids": obj.get("eligible_storelist_ids"),
            "eligible_storelist_numbers": obj.get("eligible_storelist_numbers"),
            "landing_page_image_template_id": obj.get("landing_page_image_template_id"),
            "description_template_id": obj.get("description_template_id"),
            "description": obj.get("description"),
            "terms_and_conditions_template_id": obj.get("terms_and_conditions_template_id"),
            "terms_and_conditions": obj.get("terms_and_conditions"),
            "security": obj.get("security"),
            "landing_page_urls": obj.get("landing_page_urls"),
            "allow_return_later": obj.get("allow_return_later"),
            "redemption_identifier_type": obj.get("redemption_identifier_type"),
            "member_required": obj.get("member_required"),
            "max_redemptions_per_member": obj.get("max_redemptions_per_member"),
            "dynamic_expiration": obj.get("dynamic_expiration"),
            "sub_audience_id": obj.get("sub_audience_id"),
            "audience_id": obj.get("audience_id"),
            "status": obj.get("status"),
            "redemption_grace_period": obj.get("redemption_grace_period")
        })
        return _obj


