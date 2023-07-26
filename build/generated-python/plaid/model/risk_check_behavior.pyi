# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.394.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from plaid import schemas  # noqa: F401


class RiskCheckBehavior(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Result summary object specifying values for `behavior` attributes of risk check, when available.
    """


    class MetaOapg:
        required = {
            "bot_detected",
            "user_interactions",
            "fraud_ring_detected",
        }
        
        class properties:
        
            @staticmethod
            def user_interactions() -> typing.Type['RiskCheckBehaviorUserInteractionsLabel']:
                return RiskCheckBehaviorUserInteractionsLabel
        
            @staticmethod
            def fraud_ring_detected() -> typing.Type['RiskCheckBehaviorFraudRingDetectedLabel']:
                return RiskCheckBehaviorFraudRingDetectedLabel
        
            @staticmethod
            def bot_detected() -> typing.Type['RiskCheckBehaviorBotDetectedLabel']:
                return RiskCheckBehaviorBotDetectedLabel
            __annotations__ = {
                "user_interactions": user_interactions,
                "fraud_ring_detected": fraud_ring_detected,
                "bot_detected": bot_detected,
            }
        additional_properties = schemas.AnyTypeSchema

    
    bot_detected: 'RiskCheckBehaviorBotDetectedLabel'
    user_interactions: 'RiskCheckBehaviorUserInteractionsLabel'
    fraud_ring_detected: 'RiskCheckBehaviorFraudRingDetectedLabel'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bot_detected"]) -> 'RiskCheckBehaviorBotDetectedLabel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_interactions"]) -> 'RiskCheckBehaviorUserInteractionsLabel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fraud_ring_detected"]) -> 'RiskCheckBehaviorFraudRingDetectedLabel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bot_detected"], typing_extensions.Literal["user_interactions"], typing_extensions.Literal["fraud_ring_detected"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bot_detected"]) -> 'RiskCheckBehaviorBotDetectedLabel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_interactions"]) -> 'RiskCheckBehaviorUserInteractionsLabel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fraud_ring_detected"]) -> 'RiskCheckBehaviorFraudRingDetectedLabel': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bot_detected"], typing_extensions.Literal["user_interactions"], typing_extensions.Literal["fraud_ring_detected"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'RiskCheckBehavior':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.risk_check_behavior_bot_detected_label import RiskCheckBehaviorBotDetectedLabel
from plaid.model.risk_check_behavior_fraud_ring_detected_label import RiskCheckBehaviorFraudRingDetectedLabel
from plaid.model.risk_check_behavior_user_interactions_label import RiskCheckBehaviorUserInteractionsLabel
