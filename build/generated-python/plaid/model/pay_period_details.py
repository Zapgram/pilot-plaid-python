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


class PayPeriodDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details about the pay period.
    """


    class MetaOapg:
        
        class properties:
            
            
            class check_amount(
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
                ) -> 'check_amount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class distribution_breakdown(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DistributionBreakdown']:
                        return DistributionBreakdown
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DistributionBreakdown'], typing.List['DistributionBreakdown']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'distribution_breakdown':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DistributionBreakdown':
                    return super().__getitem__(i)
            
            
            class end_date(
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
                ) -> 'end_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class gross_earnings(
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
                ) -> 'gross_earnings':
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
            
            
            class pay_frequency(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PAY_FREQUENCY_UNKNOWN": "PAY_FREQUENCY_UNKNOWN",
                        "PAY_FREQUENCY_WEEKLY": "PAY_FREQUENCY_WEEKLY",
                        "PAY_FREQUENCY_BIWEEKLY": "PAY_FREQUENCY_BIWEEKLY",
                        "PAY_FREQUENCY_SEMIMONTHLY": "PAY_FREQUENCY_SEMIMONTHLY",
                        "PAY_FREQUENCY_MONTHLY": "PAY_FREQUENCY_MONTHLY",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def PAY_FREQUENCY_UNKNOWN(cls):
                    return cls("PAY_FREQUENCY_UNKNOWN")
                
                @schemas.classproperty
                def PAY_FREQUENCY_WEEKLY(cls):
                    return cls("PAY_FREQUENCY_WEEKLY")
                
                @schemas.classproperty
                def PAY_FREQUENCY_BIWEEKLY(cls):
                    return cls("PAY_FREQUENCY_BIWEEKLY")
                
                @schemas.classproperty
                def PAY_FREQUENCY_SEMIMONTHLY(cls):
                    return cls("PAY_FREQUENCY_SEMIMONTHLY")
                
                @schemas.classproperty
                def PAY_FREQUENCY_MONTHLY(cls):
                    return cls("PAY_FREQUENCY_MONTHLY")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pay_frequency':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class pay_day(
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
                ) -> 'pay_day':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class start_date(
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
                ) -> 'start_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "check_amount": check_amount,
                "distribution_breakdown": distribution_breakdown,
                "end_date": end_date,
                "gross_earnings": gross_earnings,
                "pay_date": pay_date,
                "pay_frequency": pay_frequency,
                "pay_day": pay_day,
                "start_date": start_date,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["check_amount"]) -> MetaOapg.properties.check_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["distribution_breakdown"]) -> MetaOapg.properties.distribution_breakdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_earnings"]) -> MetaOapg.properties.gross_earnings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_date"]) -> MetaOapg.properties.pay_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_frequency"]) -> MetaOapg.properties.pay_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_day"]) -> MetaOapg.properties.pay_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["check_amount"], typing_extensions.Literal["distribution_breakdown"], typing_extensions.Literal["end_date"], typing_extensions.Literal["gross_earnings"], typing_extensions.Literal["pay_date"], typing_extensions.Literal["pay_frequency"], typing_extensions.Literal["pay_day"], typing_extensions.Literal["start_date"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["check_amount"]) -> typing.Union[MetaOapg.properties.check_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["distribution_breakdown"]) -> typing.Union[MetaOapg.properties.distribution_breakdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_earnings"]) -> typing.Union[MetaOapg.properties.gross_earnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_date"]) -> typing.Union[MetaOapg.properties.pay_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_frequency"]) -> typing.Union[MetaOapg.properties.pay_frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_day"]) -> typing.Union[MetaOapg.properties.pay_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["check_amount"], typing_extensions.Literal["distribution_breakdown"], typing_extensions.Literal["end_date"], typing_extensions.Literal["gross_earnings"], typing_extensions.Literal["pay_date"], typing_extensions.Literal["pay_frequency"], typing_extensions.Literal["pay_day"], typing_extensions.Literal["start_date"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        check_amount: typing.Union[MetaOapg.properties.check_amount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        distribution_breakdown: typing.Union[MetaOapg.properties.distribution_breakdown, list, tuple, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, None, str, date, schemas.Unset] = schemas.unset,
        gross_earnings: typing.Union[MetaOapg.properties.gross_earnings, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pay_date: typing.Union[MetaOapg.properties.pay_date, None, str, date, schemas.Unset] = schemas.unset,
        pay_frequency: typing.Union[MetaOapg.properties.pay_frequency, None, str, schemas.Unset] = schemas.unset,
        pay_day: typing.Union[MetaOapg.properties.pay_day, None, str, date, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, None, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PayPeriodDetails':
        return super().__new__(
            cls,
            *_args,
            check_amount=check_amount,
            distribution_breakdown=distribution_breakdown,
            end_date=end_date,
            gross_earnings=gross_earnings,
            pay_date=pay_date,
            pay_frequency=pay_frequency,
            pay_day=pay_day,
            start_date=start_date,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.distribution_breakdown import DistributionBreakdown
