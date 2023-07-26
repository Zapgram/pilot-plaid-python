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


class TransferIntentGetRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Defines the request schema for `/transfer/intent/get`
    """


    class MetaOapg:
        required = {
            "transfer_intent_id",
        }
        
        class properties:
            transfer_intent_id = schemas.StrSchema
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
            __annotations__ = {
                "transfer_intent_id": transfer_intent_id,
                "client_id": client_id,
                "secret": secret,
            }
        additional_properties = schemas.AnyTypeSchema
    
    transfer_intent_id: MetaOapg.properties.transfer_intent_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_intent_id"]) -> MetaOapg.properties.transfer_intent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transfer_intent_id"], typing_extensions.Literal["client_id"], typing_extensions.Literal["secret"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_intent_id"]) -> MetaOapg.properties.transfer_intent_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transfer_intent_id"], typing_extensions.Literal["client_id"], typing_extensions.Literal["secret"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        transfer_intent_id: typing.Union[MetaOapg.properties.transfer_intent_id, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TransferIntentGetRequest':
        return super().__new__(
            cls,
            *_args,
            transfer_intent_id=transfer_intent_id,
            client_id=client_id,
            secret=secret,
            _configuration=_configuration,
            **kwargs,
        )