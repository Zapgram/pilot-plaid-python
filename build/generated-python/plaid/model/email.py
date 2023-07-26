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


class Email(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object representing an email address
    """


    class MetaOapg:
        required = {
            "data",
            "type",
            "primary",
        }
        
        class properties:
            data = schemas.StrSchema
            primary = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "primary": "PRIMARY",
                        "secondary": "SECONDARY",
                        "other": "OTHER",
                    }
                
                @schemas.classproperty
                def PRIMARY(cls):
                    return cls("primary")
                
                @schemas.classproperty
                def SECONDARY(cls):
                    return cls("secondary")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
            __annotations__ = {
                "data": data,
                "primary": primary,
                "type": type,
            }
        additional_properties = schemas.AnyTypeSchema
    
    data: MetaOapg.properties.data
    type: MetaOapg.properties.type
    primary: MetaOapg.properties.primary
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data"], typing_extensions.Literal["type"], typing_extensions.Literal["primary"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data"], typing_extensions.Literal["type"], typing_extensions.Literal["primary"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        primary: typing.Union[MetaOapg.properties.primary, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'Email':
        return super().__new__(
            cls,
            *_args,
            data=data,
            type=type,
            primary=primary,
            _configuration=_configuration,
            **kwargs,
        )
