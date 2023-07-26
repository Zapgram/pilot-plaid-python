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


class Total(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object representing both the current pay period and year to date amount for a category.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def canonical_description() -> typing.Type['TotalCanonicalDescription']:
                return TotalCanonicalDescription
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def current_pay() -> typing.Type['Pay']:
                return Pay
        
            @staticmethod
            def ytd_pay() -> typing.Type['Pay']:
                return Pay
            __annotations__ = {
                "canonical_description": canonical_description,
                "description": description,
                "current_pay": current_pay,
                "ytd_pay": ytd_pay,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["canonical_description"]) -> 'TotalCanonicalDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_pay"]) -> 'Pay': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ytd_pay"]) -> 'Pay': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["canonical_description"], typing_extensions.Literal["description"], typing_extensions.Literal["current_pay"], typing_extensions.Literal["ytd_pay"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["canonical_description"]) -> typing.Union['TotalCanonicalDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_pay"]) -> typing.Union['Pay', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ytd_pay"]) -> typing.Union['Pay', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["canonical_description"], typing_extensions.Literal["description"], typing_extensions.Literal["current_pay"], typing_extensions.Literal["ytd_pay"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        canonical_description: typing.Union['TotalCanonicalDescription', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        current_pay: typing.Union['Pay', schemas.Unset] = schemas.unset,
        ytd_pay: typing.Union['Pay', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'Total':
        return super().__new__(
            cls,
            *_args,
            canonical_description=canonical_description,
            description=description,
            current_pay=current_pay,
            ytd_pay=ytd_pay,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.pay import Pay
from plaid.model.total_canonical_description import TotalCanonicalDescription
