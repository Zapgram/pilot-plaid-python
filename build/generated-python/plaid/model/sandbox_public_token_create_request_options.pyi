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


class SandboxPublicTokenCreateRequestOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An optional set of options to be used when configuring the Item. If specified, must not be `null`.
    """


    class MetaOapg:
        
        class properties:
            webhook = schemas.StrSchema
        
            @staticmethod
            def override_username() -> typing.Type['SandboxOverrideUsername']:
                return SandboxOverrideUsername
        
            @staticmethod
            def override_password() -> typing.Type['SandboxOverridePassword']:
                return SandboxOverridePassword
        
            @staticmethod
            def transactions() -> typing.Type['SandboxPublicTokenCreateRequestOptionsTransactions']:
                return SandboxPublicTokenCreateRequestOptionsTransactions
        
            @staticmethod
            def income_verification() -> typing.Type['SandboxPublicTokenCreateRequestOptionsIncomeVerification']:
                return SandboxPublicTokenCreateRequestOptionsIncomeVerification
            __annotations__ = {
                "webhook": webhook,
                "override_username": override_username,
                "override_password": override_password,
                "transactions": transactions,
                "income_verification": income_verification,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> MetaOapg.properties.webhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["override_username"]) -> 'SandboxOverrideUsername': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["override_password"]) -> 'SandboxOverridePassword': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> 'SandboxPublicTokenCreateRequestOptionsTransactions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income_verification"]) -> 'SandboxPublicTokenCreateRequestOptionsIncomeVerification': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["webhook", "override_username", "override_password", "transactions", "income_verification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> typing.Union[MetaOapg.properties.webhook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["override_username"]) -> typing.Union['SandboxOverrideUsername', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["override_password"]) -> typing.Union['SandboxOverridePassword', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union['SandboxPublicTokenCreateRequestOptionsTransactions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income_verification"]) -> typing.Union['SandboxPublicTokenCreateRequestOptionsIncomeVerification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["webhook", "override_username", "override_password", "transactions", "income_verification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        webhook: typing.Union[MetaOapg.properties.webhook, str, schemas.Unset] = schemas.unset,
        override_username: typing.Union['SandboxOverrideUsername', schemas.Unset] = schemas.unset,
        override_password: typing.Union['SandboxOverridePassword', schemas.Unset] = schemas.unset,
        transactions: typing.Union['SandboxPublicTokenCreateRequestOptionsTransactions', schemas.Unset] = schemas.unset,
        income_verification: typing.Union['SandboxPublicTokenCreateRequestOptionsIncomeVerification', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SandboxPublicTokenCreateRequestOptions':
        return super().__new__(
            cls,
            *_args,
            webhook=webhook,
            override_username=override_username,
            override_password=override_password,
            transactions=transactions,
            income_verification=income_verification,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.sandbox_override_password import SandboxOverridePassword
from plaid.model.sandbox_override_username import SandboxOverrideUsername
from plaid.model.sandbox_public_token_create_request_options_income_verification import SandboxPublicTokenCreateRequestOptionsIncomeVerification
from plaid.model.sandbox_public_token_create_request_options_transactions import SandboxPublicTokenCreateRequestOptionsTransactions