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


class TransferRepaymentReturn(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a return on a Guaranteed ACH transfer that is included in the specified repayment.
    """


    class MetaOapg:
        required = {
            "amount",
            "event_id",
            "iso_currency_code",
            "transfer_id",
        }
        
        class properties:
            transfer_id = schemas.StrSchema
            
            
            class event_id(
                schemas.IntSchema
            ):
                pass
            amount = schemas.StrSchema
            iso_currency_code = schemas.StrSchema
            __annotations__ = {
                "transfer_id": transfer_id,
                "event_id": event_id,
                "amount": amount,
                "iso_currency_code": iso_currency_code,
            }
        additional_properties = schemas.AnyTypeSchema
    
    amount: MetaOapg.properties.amount
    event_id: MetaOapg.properties.event_id
    iso_currency_code: MetaOapg.properties.iso_currency_code
    transfer_id: MetaOapg.properties.transfer_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_id"]) -> MetaOapg.properties.event_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_id"]) -> MetaOapg.properties.transfer_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["event_id"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["transfer_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_id"]) -> MetaOapg.properties.event_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_id"]) -> MetaOapg.properties.transfer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["event_id"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["transfer_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        event_id: typing.Union[MetaOapg.properties.event_id, decimal.Decimal, int, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        transfer_id: typing.Union[MetaOapg.properties.transfer_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TransferRepaymentReturn':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            event_id=event_id,
            iso_currency_code=iso_currency_code,
            transfer_id=transfer_id,
            _configuration=_configuration,
            **kwargs,
        )
