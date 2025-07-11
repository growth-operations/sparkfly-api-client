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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sparkfly.models.ctm_redemption_job_request_redeemed_offers_inner_qualifying_items_inner import CtmRedemptionJobRequestRedeemedOffersInnerQualifyingItemsInner
from typing import Optional, Set
from typing_extensions import Self

class CtmRedemptionJobRequestRedeemedOffersInner(BaseModel):
    """
    CtmRedemptionJobRequestRedeemedOffersInner
    """ # noqa: E501
    offer_id: Optional[StrictInt] = None
    value: Optional[StrictInt] = None
    override_ammount: Optional[StrictInt] = None
    credential: Optional[StrictStr] = None
    rpe_auth_code: Optional[StrictStr] = None
    pos_offer_code_type: Optional[StrictStr] = None
    linked_item_entry_id: Optional[StrictStr] = None
    qualifying_items: Optional[List[CtmRedemptionJobRequestRedeemedOffersInnerQualifyingItemsInner]] = None
    __properties: ClassVar[List[str]] = ["offer_id", "value", "override_ammount", "credential", "rpe_auth_code", "pos_offer_code_type", "linked_item_entry_id", "qualifying_items"]

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
        """Create an instance of CtmRedemptionJobRequestRedeemedOffersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in qualifying_items (list)
        _items = []
        if self.qualifying_items:
            for _item_qualifying_items in self.qualifying_items:
                if _item_qualifying_items:
                    _items.append(_item_qualifying_items.to_dict())
            _dict['qualifying_items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CtmRedemptionJobRequestRedeemedOffersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offer_id": obj.get("offer_id"),
            "value": obj.get("value"),
            "override_ammount": obj.get("override_ammount"),
            "credential": obj.get("credential"),
            "rpe_auth_code": obj.get("rpe_auth_code"),
            "pos_offer_code_type": obj.get("pos_offer_code_type"),
            "linked_item_entry_id": obj.get("linked_item_entry_id"),
            "qualifying_items": [CtmRedemptionJobRequestRedeemedOffersInnerQualifyingItemsInner.from_dict(_item) for _item in obj["qualifying_items"]] if obj.get("qualifying_items") is not None else None
        })
        return _obj


