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


class APR(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Information about the APR on the account.
    """


    class MetaOapg:
        required = {
            "apr_percentage",
            "apr_type",
            "interest_charge_amount",
            "balance_subject_to_apr",
        }
        
        class properties:
            apr_percentage = schemas.Float64Schema
            
            
            class apr_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BALANCE_TRANSFER_APR(cls):
                    return cls("balance_transfer_apr")
                
                @schemas.classproperty
                def CASH_APR(cls):
                    return cls("cash_apr")
                
                @schemas.classproperty
                def PURCHASE_APR(cls):
                    return cls("purchase_apr")
                
                @schemas.classproperty
                def SPECIAL(cls):
                    return cls("special")
            
            
            class balance_subject_to_apr(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'balance_subject_to_apr':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class interest_charge_amount(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'interest_charge_amount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "apr_percentage": apr_percentage,
                "apr_type": apr_type,
                "balance_subject_to_apr": balance_subject_to_apr,
                "interest_charge_amount": interest_charge_amount,
            }
        additional_properties = schemas.AnyTypeSchema
    
    apr_percentage: MetaOapg.properties.apr_percentage
    apr_type: MetaOapg.properties.apr_type
    interest_charge_amount: MetaOapg.properties.interest_charge_amount
    balance_subject_to_apr: MetaOapg.properties.balance_subject_to_apr
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apr_percentage"]) -> MetaOapg.properties.apr_percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apr_type"]) -> MetaOapg.properties.apr_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interest_charge_amount"]) -> MetaOapg.properties.interest_charge_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance_subject_to_apr"]) -> MetaOapg.properties.balance_subject_to_apr: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apr_percentage"], typing_extensions.Literal["apr_type"], typing_extensions.Literal["interest_charge_amount"], typing_extensions.Literal["balance_subject_to_apr"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apr_percentage"]) -> MetaOapg.properties.apr_percentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apr_type"]) -> MetaOapg.properties.apr_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interest_charge_amount"]) -> MetaOapg.properties.interest_charge_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance_subject_to_apr"]) -> MetaOapg.properties.balance_subject_to_apr: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apr_percentage"], typing_extensions.Literal["apr_type"], typing_extensions.Literal["interest_charge_amount"], typing_extensions.Literal["balance_subject_to_apr"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        apr_percentage: typing.Union[MetaOapg.properties.apr_percentage, decimal.Decimal, int, float, ],
        apr_type: typing.Union[MetaOapg.properties.apr_type, str, ],
        interest_charge_amount: typing.Union[MetaOapg.properties.interest_charge_amount, None, decimal.Decimal, int, float, ],
        balance_subject_to_apr: typing.Union[MetaOapg.properties.balance_subject_to_apr, None, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'APR':
        return super().__new__(
            cls,
            *_args,
            apr_percentage=apr_percentage,
            apr_type=apr_type,
            interest_charge_amount=interest_charge_amount,
            balance_subject_to_apr=balance_subject_to_apr,
            _configuration=_configuration,
            **kwargs,
        )
