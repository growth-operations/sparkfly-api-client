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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sparkfly.models.offer_request_offer_formatting_eligible_store_map import OfferRequestOfferFormattingEligibleStoreMap
from typing import Optional, Set
from typing_extensions import Self

class OfferRequestOfferFormatting(BaseModel):
    """
    OfferRequestOfferFormatting
    """ # noqa: E501
    bg_image: Optional[StrictStr] = None
    custom_offer_group: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    eligible_store_map: Optional[OfferRequestOfferFormattingEligibleStoreMap] = None
    mobile_thumb_url: Optional[StrictStr] = None
    mobile_url: Optional[StrictStr] = None
    no_printable: Optional[StrictBool] = None
    offer_store_highlight_text_template: Optional[StrictStr] = None
    offer_storelist_highlight_text_template: Optional[StrictStr] = None
    short_name: Optional[StrictStr] = None
    web_thumb_url: Optional[StrictStr] = None
    web_url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["bg_image", "custom_offer_group", "description", "eligible_store_map", "mobile_thumb_url", "mobile_url", "no_printable", "offer_store_highlight_text_template", "offer_storelist_highlight_text_template", "short_name", "web_thumb_url", "web_url"]

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
        """Create an instance of OfferRequestOfferFormatting from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of eligible_store_map
        if self.eligible_store_map:
            _dict['eligible_store_map'] = self.eligible_store_map.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OfferRequestOfferFormatting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bg_image": obj.get("bg_image"),
            "custom_offer_group": obj.get("custom_offer_group"),
            "description": obj.get("description"),
            "eligible_store_map": OfferRequestOfferFormattingEligibleStoreMap.from_dict(obj["eligible_store_map"]) if obj.get("eligible_store_map") is not None else None,
            "mobile_thumb_url": obj.get("mobile_thumb_url"),
            "mobile_url": obj.get("mobile_url"),
            "no_printable": obj.get("no_printable"),
            "offer_store_highlight_text_template": obj.get("offer_store_highlight_text_template"),
            "offer_storelist_highlight_text_template": obj.get("offer_storelist_highlight_text_template"),
            "short_name": obj.get("short_name"),
            "web_thumb_url": obj.get("web_thumb_url"),
            "web_url": obj.get("web_url")
        })
        return _obj


