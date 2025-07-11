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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sparkfly.models.ctm_transaction_show_response_availible_offers_inner import CtmTransactionShowResponseAvailibleOffersInner
from sparkfly.models.ctm_transaction_show_response_reusable_offers import CtmTransactionShowResponseReusableOffers
from sparkfly.models.ctm_transaction_show_response_transaction import CtmTransactionShowResponseTransaction
from typing import Optional, Set
from typing_extensions import Self

class CtmTransactionShowResponse(BaseModel):
    """
    CtmTransactionShowResponse
    """ # noqa: E501
    account_id: Optional[StrictInt] = None
    offers: Optional[List[StrictInt]] = None
    loyalty_id: Optional[StrictStr] = None
    reusable: Optional[StrictBool] = None
    transaction: Optional[CtmTransactionShowResponseTransaction] = None
    availible_offers: Optional[List[CtmTransactionShowResponseAvailibleOffersInner]] = None
    reusable_offers: Optional[CtmTransactionShowResponseReusableOffers] = None
    store_default_language: Optional[StrictStr] = None
    account_default_language: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["account_id", "offers", "loyalty_id", "reusable", "transaction", "availible_offers", "reusable_offers", "store_default_language", "account_default_language"]

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
        """Create an instance of CtmTransactionShowResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in availible_offers (list)
        _items = []
        if self.availible_offers:
            for _item_availible_offers in self.availible_offers:
                if _item_availible_offers:
                    _items.append(_item_availible_offers.to_dict())
            _dict['availible_offers'] = _items
        # override the default output from pydantic by calling `to_dict()` of reusable_offers
        if self.reusable_offers:
            _dict['reusable_offers'] = self.reusable_offers.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CtmTransactionShowResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_id": obj.get("account_id"),
            "offers": obj.get("offers"),
            "loyalty_id": obj.get("loyalty_id"),
            "reusable": obj.get("reusable"),
            "transaction": CtmTransactionShowResponseTransaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "availible_offers": [CtmTransactionShowResponseAvailibleOffersInner.from_dict(_item) for _item in obj["availible_offers"]] if obj.get("availible_offers") is not None else None,
            "reusable_offers": CtmTransactionShowResponseReusableOffers.from_dict(obj["reusable_offers"]) if obj.get("reusable_offers") is not None else None,
            "store_default_language": obj.get("store_default_language"),
            "account_default_language": obj.get("account_default_language")
        })
        return _obj


