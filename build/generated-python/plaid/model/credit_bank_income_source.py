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


class CreditBankIncomeSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Detailed information for the income source.
    """


    class MetaOapg:
        
        class properties:
            income_source_id = schemas.StrSchema
            income_description = schemas.StrSchema
        
            @staticmethod
            def income_category() -> typing.Type['CreditBankIncomeCategory']:
                return CreditBankIncomeCategory
            account_id = schemas.StrSchema
            start_date = schemas.DateSchema
            end_date = schemas.DateSchema
        
            @staticmethod
            def pay_frequency() -> typing.Type['CreditBankIncomePayFrequency']:
                return CreditBankIncomePayFrequency
            total_amount = schemas.NumberSchema
            transaction_count = schemas.IntSchema
            
            
            class historical_summary(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CreditBankIncomeHistoricalSummary']:
                        return CreditBankIncomeHistoricalSummary
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CreditBankIncomeHistoricalSummary'], typing.List['CreditBankIncomeHistoricalSummary']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'historical_summary':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CreditBankIncomeHistoricalSummary':
                    return super().__getitem__(i)
            __annotations__ = {
                "income_source_id": income_source_id,
                "income_description": income_description,
                "income_category": income_category,
                "account_id": account_id,
                "start_date": start_date,
                "end_date": end_date,
                "pay_frequency": pay_frequency,
                "total_amount": total_amount,
                "transaction_count": transaction_count,
                "historical_summary": historical_summary,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income_source_id"]) -> MetaOapg.properties.income_source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income_description"]) -> MetaOapg.properties.income_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income_category"]) -> 'CreditBankIncomeCategory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_frequency"]) -> 'CreditBankIncomePayFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_count"]) -> MetaOapg.properties.transaction_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historical_summary"]) -> MetaOapg.properties.historical_summary: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["income_source_id", "income_description", "income_category", "account_id", "start_date", "end_date", "pay_frequency", "total_amount", "transaction_count", "historical_summary", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income_source_id"]) -> typing.Union[MetaOapg.properties.income_source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income_description"]) -> typing.Union[MetaOapg.properties.income_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income_category"]) -> typing.Union['CreditBankIncomeCategory', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_frequency"]) -> typing.Union['CreditBankIncomePayFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_amount"]) -> typing.Union[MetaOapg.properties.total_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_count"]) -> typing.Union[MetaOapg.properties.transaction_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historical_summary"]) -> typing.Union[MetaOapg.properties.historical_summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["income_source_id", "income_description", "income_category", "account_id", "start_date", "end_date", "pay_frequency", "total_amount", "transaction_count", "historical_summary", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        income_source_id: typing.Union[MetaOapg.properties.income_source_id, str, schemas.Unset] = schemas.unset,
        income_description: typing.Union[MetaOapg.properties.income_description, str, schemas.Unset] = schemas.unset,
        income_category: typing.Union['CreditBankIncomeCategory', schemas.Unset] = schemas.unset,
        account_id: typing.Union[MetaOapg.properties.account_id, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, date, schemas.Unset] = schemas.unset,
        pay_frequency: typing.Union['CreditBankIncomePayFrequency', schemas.Unset] = schemas.unset,
        total_amount: typing.Union[MetaOapg.properties.total_amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        transaction_count: typing.Union[MetaOapg.properties.transaction_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        historical_summary: typing.Union[MetaOapg.properties.historical_summary, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreditBankIncomeSource':
        return super().__new__(
            cls,
            *_args,
            income_source_id=income_source_id,
            income_description=income_description,
            income_category=income_category,
            account_id=account_id,
            start_date=start_date,
            end_date=end_date,
            pay_frequency=pay_frequency,
            total_amount=total_amount,
            transaction_count=transaction_count,
            historical_summary=historical_summary,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.credit_bank_income_category import CreditBankIncomeCategory
from plaid.model.credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary
from plaid.model.credit_bank_income_pay_frequency import CreditBankIncomePayFrequency
