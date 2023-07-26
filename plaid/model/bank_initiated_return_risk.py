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


class BankInitiatedReturnRisk(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: "R01", "R02", "R03", "R04", "R06", "R08",  "R09", "R13", "R16", "R17", "R20", "R23". These returns have a turnaround time of 2 banking days.
    """


    class MetaOapg:
        required = {
            "score",
            "risk_tier",
        }
        
        class properties:
        
            @staticmethod
            def score() -> typing.Type['SignalScore']:
                return SignalScore
        
            @staticmethod
            def risk_tier() -> typing.Type['BankInitiatedRiskTier']:
                return BankInitiatedRiskTier
            __annotations__ = {
                "score": score,
                "risk_tier": risk_tier,
            }
    
    score: 'SignalScore'
    risk_tier: 'BankInitiatedRiskTier'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> 'SignalScore': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk_tier"]) -> 'BankInitiatedRiskTier': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["score", "risk_tier", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> 'SignalScore': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk_tier"]) -> 'BankInitiatedRiskTier': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["score", "risk_tier", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        score: 'SignalScore',
        risk_tier: 'BankInitiatedRiskTier',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankInitiatedReturnRisk':
        return super().__new__(
            cls,
            *_args,
            score=score,
            risk_tier=risk_tier,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.bank_initiated_risk_tier import BankInitiatedRiskTier
from plaid.model.signal_score import SignalScore