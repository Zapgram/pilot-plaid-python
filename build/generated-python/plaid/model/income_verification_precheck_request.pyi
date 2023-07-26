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


class IncomeVerificationPrecheckRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    IncomeVerificationPrecheckRequest defines the request schema for `/income/verification/precheck`
    """


    class MetaOapg:
        
        class properties:
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['IncomeVerificationPrecheckUser']:
                return IncomeVerificationPrecheckUser
        
            @staticmethod
            def employer() -> typing.Type['IncomeVerificationPrecheckEmployer']:
                return IncomeVerificationPrecheckEmployer
        
            @staticmethod
            def payroll_institution() -> typing.Type['IncomeVerificationPrecheckPayrollInstitution']:
                return IncomeVerificationPrecheckPayrollInstitution
            
            
            class transactions_access_token(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            AccessTokenNullable,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'transactions_access_token':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class transactions_access_tokens(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions_access_tokens':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def us_military_info() -> typing.Type['IncomeVerificationPrecheckMilitaryInfo']:
                return IncomeVerificationPrecheckMilitaryInfo
            __annotations__ = {
                "client_id": client_id,
                "secret": secret,
                "user": user,
                "employer": employer,
                "payroll_institution": payroll_institution,
                "transactions_access_token": transactions_access_token,
                "transactions_access_tokens": transactions_access_tokens,
                "us_military_info": us_military_info,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'IncomeVerificationPrecheckUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer"]) -> 'IncomeVerificationPrecheckEmployer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payroll_institution"]) -> 'IncomeVerificationPrecheckPayrollInstitution': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions_access_token"]) -> MetaOapg.properties.transactions_access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions_access_tokens"]) -> MetaOapg.properties.transactions_access_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["us_military_info"]) -> 'IncomeVerificationPrecheckMilitaryInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_id", "secret", "user", "employer", "payroll_institution", "transactions_access_token", "transactions_access_tokens", "us_military_info", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['IncomeVerificationPrecheckUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer"]) -> typing.Union['IncomeVerificationPrecheckEmployer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payroll_institution"]) -> typing.Union['IncomeVerificationPrecheckPayrollInstitution', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions_access_token"]) -> typing.Union[MetaOapg.properties.transactions_access_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions_access_tokens"]) -> typing.Union[MetaOapg.properties.transactions_access_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["us_military_info"]) -> typing.Union['IncomeVerificationPrecheckMilitaryInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_id", "secret", "user", "employer", "payroll_institution", "transactions_access_token", "transactions_access_tokens", "us_military_info", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        user: typing.Union['IncomeVerificationPrecheckUser', schemas.Unset] = schemas.unset,
        employer: typing.Union['IncomeVerificationPrecheckEmployer', schemas.Unset] = schemas.unset,
        payroll_institution: typing.Union['IncomeVerificationPrecheckPayrollInstitution', schemas.Unset] = schemas.unset,
        transactions_access_token: typing.Union[MetaOapg.properties.transactions_access_token, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        transactions_access_tokens: typing.Union[MetaOapg.properties.transactions_access_tokens, list, tuple, schemas.Unset] = schemas.unset,
        us_military_info: typing.Union['IncomeVerificationPrecheckMilitaryInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IncomeVerificationPrecheckRequest':
        return super().__new__(
            cls,
            *_args,
            client_id=client_id,
            secret=secret,
            user=user,
            employer=employer,
            payroll_institution=payroll_institution,
            transactions_access_token=transactions_access_token,
            transactions_access_tokens=transactions_access_tokens,
            us_military_info=us_military_info,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.access_token_nullable import AccessTokenNullable
from plaid.model.income_verification_precheck_employer import IncomeVerificationPrecheckEmployer
from plaid.model.income_verification_precheck_military_info import IncomeVerificationPrecheckMilitaryInfo
from plaid.model.income_verification_precheck_payroll_institution import IncomeVerificationPrecheckPayrollInstitution
from plaid.model.income_verification_precheck_user import IncomeVerificationPrecheckUser
