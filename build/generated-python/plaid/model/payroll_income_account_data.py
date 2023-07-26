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


class PayrollIncomeAccountData(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object containing account level data.
    """


    class MetaOapg:
        required = {
            "account_id",
            "rate_of_pay",
            "pay_frequency",
        }
        
        class properties:
            
            
            class account_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def rate_of_pay() -> typing.Type['PayrollIncomeRateOfPay']:
                return PayrollIncomeRateOfPay
            
            
            class pay_frequency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
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
            __annotations__ = {
                "account_id": account_id,
                "rate_of_pay": rate_of_pay,
                "pay_frequency": pay_frequency,
            }
        additional_properties = schemas.AnyTypeSchema

    
    account_id: MetaOapg.properties.account_id
    rate_of_pay: 'PayrollIncomeRateOfPay'
    pay_frequency: MetaOapg.properties.pay_frequency
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_of_pay"]) -> 'PayrollIncomeRateOfPay': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_frequency"]) -> MetaOapg.properties.pay_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_id"], typing_extensions.Literal["rate_of_pay"], typing_extensions.Literal["pay_frequency"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_of_pay"]) -> 'PayrollIncomeRateOfPay': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_frequency"]) -> MetaOapg.properties.pay_frequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_id"], typing_extensions.Literal["rate_of_pay"], typing_extensions.Literal["pay_frequency"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PayrollIncomeAccountData':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.payroll_income_rate_of_pay import PayrollIncomeRateOfPay