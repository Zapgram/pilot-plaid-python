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


class WalletTransactionAmount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The amount and currency of a transaction
    """


    class MetaOapg:
        required = {
            "iso_currency_code",
            "value",
        }
        
        class properties:
        
            @staticmethod
            def iso_currency_code() -> typing.Type['WalletISOCurrencyCode']:
                return WalletISOCurrencyCode
            
            
            class value(
                schemas.Float64Schema
            ):
                pass
            __annotations__ = {
                "iso_currency_code": iso_currency_code,
                "value": value,
            }
        additional_properties = schemas.AnyTypeSchema
    
    iso_currency_code: 'WalletISOCurrencyCode'
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> 'WalletISOCurrencyCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["value"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> 'WalletISOCurrencyCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["value"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        iso_currency_code: 'WalletISOCurrencyCode',
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WalletTransactionAmount':
        return super().__new__(
            cls,
            *_args,
            iso_currency_code=iso_currency_code,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.wallet_iso_currency_code import WalletISOCurrencyCode
