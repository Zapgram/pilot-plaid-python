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


class PaymentConsentPeriodicAmount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Defines consent payments limitations per period.
    """


    class MetaOapg:
        required = {
            "amount",
            "interval",
            "alignment",
        }
        
        class properties:
        
            @staticmethod
            def amount() -> typing.Type['PaymentConsentPeriodicAmountAmount']:
                return PaymentConsentPeriodicAmountAmount
        
            @staticmethod
            def interval() -> typing.Type['PaymentConsentPeriodicInterval']:
                return PaymentConsentPeriodicInterval
        
            @staticmethod
            def alignment() -> typing.Type['PaymentConsentPeriodicAlignment']:
                return PaymentConsentPeriodicAlignment
            __annotations__ = {
                "amount": amount,
                "interval": interval,
                "alignment": alignment,
            }
    
    amount: 'PaymentConsentPeriodicAmountAmount'
    interval: 'PaymentConsentPeriodicInterval'
    alignment: 'PaymentConsentPeriodicAlignment'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'PaymentConsentPeriodicAmountAmount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> 'PaymentConsentPeriodicInterval': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alignment"]) -> 'PaymentConsentPeriodicAlignment': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "interval", "alignment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'PaymentConsentPeriodicAmountAmount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> 'PaymentConsentPeriodicInterval': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alignment"]) -> 'PaymentConsentPeriodicAlignment': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "interval", "alignment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: 'PaymentConsentPeriodicAmountAmount',
        interval: 'PaymentConsentPeriodicInterval',
        alignment: 'PaymentConsentPeriodicAlignment',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentConsentPeriodicAmount':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            interval=interval,
            alignment=alignment,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.payment_consent_periodic_alignment import PaymentConsentPeriodicAlignment
from plaid.model.payment_consent_periodic_amount_amount import PaymentConsentPeriodicAmountAmount
from plaid.model.payment_consent_periodic_interval import PaymentConsentPeriodicInterval