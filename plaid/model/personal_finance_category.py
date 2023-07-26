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


class PersonalFinanceCategory(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.

See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    """


    class MetaOapg:
        required = {
            "detailed",
            "primary",
        }
        
        class properties:
            primary = schemas.StrSchema
            detailed = schemas.StrSchema
            
            
            class confidence_level(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'confidence_level':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "primary": primary,
                "detailed": detailed,
                "confidence_level": confidence_level,
            }
        additional_properties = schemas.AnyTypeSchema

    
    detailed: MetaOapg.properties.detailed
    primary: MetaOapg.properties.primary
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detailed"]) -> MetaOapg.properties.detailed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidence_level"]) -> MetaOapg.properties.confidence_level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["detailed"], typing_extensions.Literal["primary"], typing_extensions.Literal["confidence_level"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detailed"]) -> MetaOapg.properties.detailed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidence_level"]) -> typing.Union[MetaOapg.properties.confidence_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["detailed"], typing_extensions.Literal["primary"], typing_extensions.Literal["confidence_level"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        confidence_level: typing.Union[MetaOapg.properties.confidence_level, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PersonalFinanceCategory':
        return super().__new__(
            cls,
            *_args,
            confidence_level=confidence_level,
            _configuration=_configuration,
            **kwargs,
        )