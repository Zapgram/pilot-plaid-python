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


class PaymentInitiationRecipient(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PaymentInitiationRecipient defines a payment initiation recipient
    """


    class MetaOapg:
        required = {
            "name",
            "recipient_id",
        }
        
        class properties:
            recipient_id = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['PaymentInitiationAddress']:
                return PaymentInitiationAddress
            
            
            class iban(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iban':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def bacs() -> typing.Type['RecipientBACSNullable']:
                return RecipientBACSNullable
            __annotations__ = {
                "recipient_id": recipient_id,
                "name": name,
                "address": address,
                "iban": iban,
                "bacs": bacs,
            }
        additional_properties = schemas.AnyTypeSchema
    
    name: MetaOapg.properties.name
    recipient_id: MetaOapg.properties.recipient_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient_id"]) -> MetaOapg.properties.recipient_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'PaymentInitiationAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bacs"]) -> 'RecipientBACSNullable': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["recipient_id"], typing_extensions.Literal["address"], typing_extensions.Literal["iban"], typing_extensions.Literal["bacs"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient_id"]) -> MetaOapg.properties.recipient_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['PaymentInitiationAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> typing.Union[MetaOapg.properties.iban, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bacs"]) -> typing.Union['RecipientBACSNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["recipient_id"], typing_extensions.Literal["address"], typing_extensions.Literal["iban"], typing_extensions.Literal["bacs"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        recipient_id: typing.Union[MetaOapg.properties.recipient_id, str, ],
        address: typing.Union['PaymentInitiationAddress', schemas.Unset] = schemas.unset,
        iban: typing.Union[MetaOapg.properties.iban, None, str, schemas.Unset] = schemas.unset,
        bacs: typing.Union['RecipientBACSNullable', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PaymentInitiationRecipient':
        return super().__new__(
            cls,
            *_args,
            name=name,
            recipient_id=recipient_id,
            address=address,
            iban=iban,
            bacs=bacs,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.payment_initiation_address import PaymentInitiationAddress
from plaid.model.recipient_bacs_nullable import RecipientBACSNullable