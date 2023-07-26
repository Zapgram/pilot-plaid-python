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


class ClientProvidedRawTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A client-provided transaction for Plaid to enhance.
    """


    class MetaOapg:
        required = {
            "amount",
            "iso_currency_code",
            "description",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            description = schemas.StrSchema
            amount = schemas.Float64Schema
            iso_currency_code = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "description": description,
                "amount": amount,
                "iso_currency_code": iso_currency_code,
            }
        additional_properties = schemas.AnyTypeSchema
    
    amount: MetaOapg.properties.amount
    iso_currency_code: MetaOapg.properties.iso_currency_code
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ClientProvidedRawTransaction':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            iso_currency_code=iso_currency_code,
            description=description,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
