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
from typing import Optional, Set
from typing_extensions import Self

class ItemSetAllOfItemSet(BaseModel):
    """
    ItemSetAllOfItemSet
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    merchant_id: Optional[StrictStr] = None
    manufacturer_id: Optional[StrictStr] = None
    manufacturer_name: Optional[StrictStr] = None
    item_ids: Optional[List[Dict[str, Any]]] = None
    set_type: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "name", "merchant_id", "manufacturer_id", "manufacturer_name", "item_ids", "set_type"]

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
        """Create an instance of ItemSetAllOfItemSet from a JSON string"""
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
        """Create an instance of ItemSetAllOfItemSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "merchant_id": obj.get("merchant_id"),
            "manufacturer_id": obj.get("manufacturer_id"),
            "manufacturer_name": obj.get("manufacturer_name"),
            "item_ids": obj.get("item_ids"),
            "set_type": obj.get("set_type")
        })
        return _obj


