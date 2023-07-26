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


class WalletNumbers(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object representing the e-wallet account numbers
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def bacs() -> typing.Type['RecipientBACS']:
                return RecipientBACS
        
            @staticmethod
            def international() -> typing.Type['NumbersInternationalIBAN']:
                return NumbersInternationalIBAN
            __annotations__ = {
                "bacs": bacs,
                "international": international,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bacs"]) -> 'RecipientBACS': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["international"]) -> 'NumbersInternationalIBAN': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bacs"], typing_extensions.Literal["international"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bacs"]) -> typing.Union['RecipientBACS', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["international"]) -> typing.Union['NumbersInternationalIBAN', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bacs"], typing_extensions.Literal["international"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bacs: typing.Union['RecipientBACS', schemas.Unset] = schemas.unset,
        international: typing.Union['NumbersInternationalIBAN', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WalletNumbers':
        return super().__new__(
            cls,
            *_args,
            bacs=bacs,
            international=international,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.numbers_international_iban import NumbersInternationalIBAN
from plaid.model.recipient_bacs import RecipientBACS