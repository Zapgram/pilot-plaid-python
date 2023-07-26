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


class DepositSwitchTargetAccount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The deposit switch destination account
    """


    class MetaOapg:
        required = {
            "account_number",
            "account_name",
            "account_subtype",
            "routing_number",
        }
        
        class properties:
            account_number = schemas.StrSchema
            routing_number = schemas.StrSchema
            account_name = schemas.StrSchema
            
            
            class account_subtype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "checking": "CHECKING",
                        "savings": "SAVINGS",
                    }
                
                @schemas.classproperty
                def CHECKING(cls):
                    return cls("checking")
                
                @schemas.classproperty
                def SAVINGS(cls):
                    return cls("savings")
            __annotations__ = {
                "account_number": account_number,
                "routing_number": routing_number,
                "account_name": account_name,
                "account_subtype": account_subtype,
            }
        additional_properties = schemas.AnyTypeSchema
    
    account_number: MetaOapg.properties.account_number
    account_name: MetaOapg.properties.account_name
    account_subtype: MetaOapg.properties.account_subtype
    routing_number: MetaOapg.properties.routing_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_number"]) -> MetaOapg.properties.account_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_name"]) -> MetaOapg.properties.account_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_subtype"]) -> MetaOapg.properties.account_subtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routing_number"]) -> MetaOapg.properties.routing_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_number"], typing_extensions.Literal["account_name"], typing_extensions.Literal["account_subtype"], typing_extensions.Literal["routing_number"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_number"]) -> MetaOapg.properties.account_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_name"]) -> MetaOapg.properties.account_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_subtype"]) -> MetaOapg.properties.account_subtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routing_number"]) -> MetaOapg.properties.routing_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_number"], typing_extensions.Literal["account_name"], typing_extensions.Literal["account_subtype"], typing_extensions.Literal["routing_number"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        account_number: typing.Union[MetaOapg.properties.account_number, str, ],
        account_name: typing.Union[MetaOapg.properties.account_name, str, ],
        account_subtype: typing.Union[MetaOapg.properties.account_subtype, str, ],
        routing_number: typing.Union[MetaOapg.properties.routing_number, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'DepositSwitchTargetAccount':
        return super().__new__(
            cls,
            *_args,
            account_number=account_number,
            account_name=account_name,
            account_subtype=account_subtype,
            routing_number=routing_number,
            _configuration=_configuration,
            **kwargs,
        )
