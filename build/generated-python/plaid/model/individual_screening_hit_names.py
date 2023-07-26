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


class IndividualScreeningHitNames(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Name information for the associated individual watchlist hit
    """


    class MetaOapg:
        required = {
            "is_primary",
            "weak_alias_determination",
            "full",
        }
        
        class properties:
            full = schemas.StrSchema
            is_primary = schemas.BoolSchema
        
            @staticmethod
            def weak_alias_determination() -> typing.Type['WeakAliasDetermination']:
                return WeakAliasDetermination
            __annotations__ = {
                "full": full,
                "is_primary": is_primary,
                "weak_alias_determination": weak_alias_determination,
            }
        additional_properties = schemas.AnyTypeSchema
    
    is_primary: MetaOapg.properties.is_primary
    weak_alias_determination: 'WeakAliasDetermination'
    full: MetaOapg.properties.full
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_primary"]) -> MetaOapg.properties.is_primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weak_alias_determination"]) -> 'WeakAliasDetermination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full"]) -> MetaOapg.properties.full: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_primary"], typing_extensions.Literal["weak_alias_determination"], typing_extensions.Literal["full"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_primary"]) -> MetaOapg.properties.is_primary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weak_alias_determination"]) -> 'WeakAliasDetermination': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full"]) -> MetaOapg.properties.full: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_primary"], typing_extensions.Literal["weak_alias_determination"], typing_extensions.Literal["full"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_primary: typing.Union[MetaOapg.properties.is_primary, bool, ],
        weak_alias_determination: 'WeakAliasDetermination',
        full: typing.Union[MetaOapg.properties.full, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'IndividualScreeningHitNames':
        return super().__new__(
            cls,
            *_args,
            is_primary=is_primary,
            weak_alias_determination=weak_alias_determination,
            full=full,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.weak_alias_determination import WeakAliasDetermination
