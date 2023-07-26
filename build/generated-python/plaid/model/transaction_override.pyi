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


class TransactionOverride(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Data to populate as test transaction data. If not specified, random transactions will be generated instead.
    """


    class MetaOapg:
        required = {
            "amount",
            "date_posted",
            "description",
            "date_transacted",
        }
        
        class properties:
            date_transacted = schemas.DateSchema
            date_posted = schemas.DateSchema
            amount = schemas.Float64Schema
            description = schemas.StrSchema
            currency = schemas.StrSchema
            __annotations__ = {
                "date_transacted": date_transacted,
                "date_posted": date_posted,
                "amount": amount,
                "description": description,
                "currency": currency,
            }
        additional_properties = schemas.AnyTypeSchema
    
    amount: MetaOapg.properties.amount
    date_posted: MetaOapg.properties.date_posted
    description: MetaOapg.properties.description
    date_transacted: MetaOapg.properties.date_transacted
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_posted"]) -> MetaOapg.properties.date_posted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_transacted"]) -> MetaOapg.properties.date_transacted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["date_posted"], typing_extensions.Literal["description"], typing_extensions.Literal["date_transacted"], typing_extensions.Literal["currency"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_posted"]) -> MetaOapg.properties.date_posted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_transacted"]) -> MetaOapg.properties.date_transacted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["date_posted"], typing_extensions.Literal["description"], typing_extensions.Literal["date_transacted"], typing_extensions.Literal["currency"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        date_posted: typing.Union[MetaOapg.properties.date_posted, str, date, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        date_transacted: typing.Union[MetaOapg.properties.date_transacted, str, date, ],
        currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TransactionOverride':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            date_posted=date_posted,
            description=description,
            date_transacted=date_transacted,
            currency=currency,
            _configuration=_configuration,
            **kwargs,
        )
