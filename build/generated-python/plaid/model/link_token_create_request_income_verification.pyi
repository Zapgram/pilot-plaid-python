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


class LinkTokenCreateRequestIncomeVerification(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies options for initializing Link for use with the Income product. This field is required if `income_verification` is included in the `products` array.
    """


    class MetaOapg:
        
        class properties:
            income_verification_id = schemas.StrSchema
            asset_report_id = schemas.StrSchema
            precheck_id = schemas.StrSchema
            
            
            class access_tokens(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'access_tokens':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class income_source_types(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IncomeVerificationSourceType']:
                        return IncomeVerificationSourceType
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['IncomeVerificationSourceType'], typing.List['IncomeVerificationSourceType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'income_source_types':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IncomeVerificationSourceType':
                    return super().__getitem__(i)
        
            @staticmethod
            def bank_income() -> typing.Type['LinkTokenCreateRequestIncomeVerificationBankIncome']:
                return LinkTokenCreateRequestIncomeVerificationBankIncome
        
            @staticmethod
            def payroll_income() -> typing.Type['LinkTokenCreateRequestIncomeVerificationPayrollIncome']:
                return LinkTokenCreateRequestIncomeVerificationPayrollIncome
            
            
            class stated_income_sources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LinkTokenCreateRequestUserStatedIncomeSource']:
                        return LinkTokenCreateRequestUserStatedIncomeSource
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['LinkTokenCreateRequestUserStatedIncomeSource'], typing.List['LinkTokenCreateRequestUserStatedIncomeSource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stated_income_sources':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LinkTokenCreateRequestUserStatedIncomeSource':
                    return super().__getitem__(i)
            __annotations__ = {
                "income_verification_id": income_verification_id,
                "asset_report_id": asset_report_id,
                "precheck_id": precheck_id,
                "access_tokens": access_tokens,
                "income_source_types": income_source_types,
                "bank_income": bank_income,
                "payroll_income": payroll_income,
                "stated_income_sources": stated_income_sources,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income_verification_id"]) -> MetaOapg.properties.income_verification_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset_report_id"]) -> MetaOapg.properties.asset_report_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["precheck_id"]) -> MetaOapg.properties.precheck_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_tokens"]) -> MetaOapg.properties.access_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income_source_types"]) -> MetaOapg.properties.income_source_types: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_income"]) -> 'LinkTokenCreateRequestIncomeVerificationBankIncome': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payroll_income"]) -> 'LinkTokenCreateRequestIncomeVerificationPayrollIncome': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stated_income_sources"]) -> MetaOapg.properties.stated_income_sources: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["income_verification_id", "asset_report_id", "precheck_id", "access_tokens", "income_source_types", "bank_income", "payroll_income", "stated_income_sources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income_verification_id"]) -> typing.Union[MetaOapg.properties.income_verification_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset_report_id"]) -> typing.Union[MetaOapg.properties.asset_report_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["precheck_id"]) -> typing.Union[MetaOapg.properties.precheck_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_tokens"]) -> typing.Union[MetaOapg.properties.access_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income_source_types"]) -> typing.Union[MetaOapg.properties.income_source_types, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_income"]) -> typing.Union['LinkTokenCreateRequestIncomeVerificationBankIncome', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payroll_income"]) -> typing.Union['LinkTokenCreateRequestIncomeVerificationPayrollIncome', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stated_income_sources"]) -> typing.Union[MetaOapg.properties.stated_income_sources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["income_verification_id", "asset_report_id", "precheck_id", "access_tokens", "income_source_types", "bank_income", "payroll_income", "stated_income_sources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        income_verification_id: typing.Union[MetaOapg.properties.income_verification_id, str, schemas.Unset] = schemas.unset,
        asset_report_id: typing.Union[MetaOapg.properties.asset_report_id, str, schemas.Unset] = schemas.unset,
        precheck_id: typing.Union[MetaOapg.properties.precheck_id, str, schemas.Unset] = schemas.unset,
        access_tokens: typing.Union[MetaOapg.properties.access_tokens, list, tuple, schemas.Unset] = schemas.unset,
        income_source_types: typing.Union[MetaOapg.properties.income_source_types, list, tuple, schemas.Unset] = schemas.unset,
        bank_income: typing.Union['LinkTokenCreateRequestIncomeVerificationBankIncome', schemas.Unset] = schemas.unset,
        payroll_income: typing.Union['LinkTokenCreateRequestIncomeVerificationPayrollIncome', schemas.Unset] = schemas.unset,
        stated_income_sources: typing.Union[MetaOapg.properties.stated_income_sources, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LinkTokenCreateRequestIncomeVerification':
        return super().__new__(
            cls,
            *_args,
            income_verification_id=income_verification_id,
            asset_report_id=asset_report_id,
            precheck_id=precheck_id,
            access_tokens=access_tokens,
            income_source_types=income_source_types,
            bank_income=bank_income,
            payroll_income=payroll_income,
            stated_income_sources=stated_income_sources,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.income_verification_source_type import IncomeVerificationSourceType
from plaid.model.link_token_create_request_income_verification_bank_income import LinkTokenCreateRequestIncomeVerificationBankIncome
from plaid.model.link_token_create_request_income_verification_payroll_income import LinkTokenCreateRequestIncomeVerificationPayrollIncome
from plaid.model.link_token_create_request_user_stated_income_source import LinkTokenCreateRequestUserStatedIncomeSource
