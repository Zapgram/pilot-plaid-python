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


class PaystubDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object representing details that can be found on the paystub.
    """


    class MetaOapg:
        
        class properties:
            
            
            class pay_period_start_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pay_period_start_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class pay_period_end_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pay_period_end_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class pay_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pay_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class paystub_provider(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paystub_provider':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def pay_frequency() -> typing.Type['PaystubPayFrequency']:
                return PaystubPayFrequency
            __annotations__ = {
                "pay_period_start_date": pay_period_start_date,
                "pay_period_end_date": pay_period_end_date,
                "pay_date": pay_date,
                "paystub_provider": paystub_provider,
                "pay_frequency": pay_frequency,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_period_start_date"]) -> MetaOapg.properties.pay_period_start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_period_end_date"]) -> MetaOapg.properties.pay_period_end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_date"]) -> MetaOapg.properties.pay_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paystub_provider"]) -> MetaOapg.properties.paystub_provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_frequency"]) -> 'PaystubPayFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pay_period_start_date"], typing_extensions.Literal["pay_period_end_date"], typing_extensions.Literal["pay_date"], typing_extensions.Literal["paystub_provider"], typing_extensions.Literal["pay_frequency"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_period_start_date"]) -> typing.Union[MetaOapg.properties.pay_period_start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_period_end_date"]) -> typing.Union[MetaOapg.properties.pay_period_end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_date"]) -> typing.Union[MetaOapg.properties.pay_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paystub_provider"]) -> typing.Union[MetaOapg.properties.paystub_provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_frequency"]) -> typing.Union['PaystubPayFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pay_period_start_date"], typing_extensions.Literal["pay_period_end_date"], typing_extensions.Literal["pay_date"], typing_extensions.Literal["paystub_provider"], typing_extensions.Literal["pay_frequency"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pay_period_start_date: typing.Union[MetaOapg.properties.pay_period_start_date, None, str, date, schemas.Unset] = schemas.unset,
        pay_period_end_date: typing.Union[MetaOapg.properties.pay_period_end_date, None, str, date, schemas.Unset] = schemas.unset,
        pay_date: typing.Union[MetaOapg.properties.pay_date, None, str, date, schemas.Unset] = schemas.unset,
        paystub_provider: typing.Union[MetaOapg.properties.paystub_provider, None, str, schemas.Unset] = schemas.unset,
        pay_frequency: typing.Union['PaystubPayFrequency', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PaystubDetails':
        return super().__new__(
            cls,
            *_args,
            pay_period_start_date=pay_period_start_date,
            pay_period_end_date=pay_period_end_date,
            pay_date=pay_date,
            paystub_provider=paystub_provider,
            pay_frequency=pay_frequency,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.paystub_pay_frequency import PaystubPayFrequency