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


class CreditBankEmployment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Detailed information for the bank employment.
    """


    class MetaOapg:
        required = {
            "account_id",
            "earliest_deposit_date",
            "employer",
            "latest_deposit_date",
            "bank_employment_id",
        }
        
        class properties:
            bank_employment_id = schemas.StrSchema
            account_id = schemas.StrSchema
        
            @staticmethod
            def employer() -> typing.Type['CreditBankEmployer']:
                return CreditBankEmployer
            latest_deposit_date = schemas.DateSchema
            earliest_deposit_date = schemas.DateSchema
            __annotations__ = {
                "bank_employment_id": bank_employment_id,
                "account_id": account_id,
                "employer": employer,
                "latest_deposit_date": latest_deposit_date,
                "earliest_deposit_date": earliest_deposit_date,
            }
    
    account_id: MetaOapg.properties.account_id
    earliest_deposit_date: MetaOapg.properties.earliest_deposit_date
    employer: 'CreditBankEmployer'
    latest_deposit_date: MetaOapg.properties.latest_deposit_date
    bank_employment_id: MetaOapg.properties.bank_employment_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_employment_id"]) -> MetaOapg.properties.bank_employment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer"]) -> 'CreditBankEmployer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest_deposit_date"]) -> MetaOapg.properties.latest_deposit_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earliest_deposit_date"]) -> MetaOapg.properties.earliest_deposit_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bank_employment_id", "account_id", "employer", "latest_deposit_date", "earliest_deposit_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_employment_id"]) -> MetaOapg.properties.bank_employment_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer"]) -> 'CreditBankEmployer': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest_deposit_date"]) -> MetaOapg.properties.latest_deposit_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earliest_deposit_date"]) -> MetaOapg.properties.earliest_deposit_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bank_employment_id", "account_id", "employer", "latest_deposit_date", "earliest_deposit_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        earliest_deposit_date: typing.Union[MetaOapg.properties.earliest_deposit_date, str, date, ],
        employer: 'CreditBankEmployer',
        latest_deposit_date: typing.Union[MetaOapg.properties.latest_deposit_date, str, date, ],
        bank_employment_id: typing.Union[MetaOapg.properties.bank_employment_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreditBankEmployment':
        return super().__new__(
            cls,
            *_args,
            account_id=account_id,
            earliest_deposit_date=earliest_deposit_date,
            employer=employer,
            latest_deposit_date=latest_deposit_date,
            bank_employment_id=bank_employment_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.credit_bank_employer import CreditBankEmployer
