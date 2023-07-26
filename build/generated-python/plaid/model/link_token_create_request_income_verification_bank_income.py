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


class LinkTokenCreateRequestIncomeVerificationBankIncome(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`.
    """


    class MetaOapg:
        required = {
            "days_requested",
        }
        
        class properties:
            
            
            class days_requested(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 731
                    inclusive_minimum = 1
            
            
            class enable_multiple_items(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enable_multiple_items':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "days_requested": days_requested,
                "enable_multiple_items": enable_multiple_items,
            }
    
    days_requested: MetaOapg.properties.days_requested
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days_requested"]) -> MetaOapg.properties.days_requested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_multiple_items"]) -> MetaOapg.properties.enable_multiple_items: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["days_requested", "enable_multiple_items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days_requested"]) -> MetaOapg.properties.days_requested: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_multiple_items"]) -> typing.Union[MetaOapg.properties.enable_multiple_items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["days_requested", "enable_multiple_items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        days_requested: typing.Union[MetaOapg.properties.days_requested, decimal.Decimal, int, ],
        enable_multiple_items: typing.Union[MetaOapg.properties.enable_multiple_items, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LinkTokenCreateRequestIncomeVerificationBankIncome':
        return super().__new__(
            cls,
            *_args,
            days_requested=days_requested,
            enable_multiple_items=enable_multiple_items,
            _configuration=_configuration,
            **kwargs,
        )
