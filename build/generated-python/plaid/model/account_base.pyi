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


class AccountBase(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A single account at a financial institution.
    """


    class MetaOapg:
        required = {
            "official_name",
            "balances",
            "account_id",
            "subtype",
            "name",
            "type",
            "mask",
        }
        
        class properties:
            account_id = schemas.StrSchema
        
            @staticmethod
            def balances() -> typing.Type['AccountBalance']:
                return AccountBalance
            
            
            class mask(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mask':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            name = schemas.StrSchema
            
            
            class official_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'official_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def type() -> typing.Type['AccountType']:
                return AccountType
        
            @staticmethod
            def subtype() -> typing.Type['AccountSubtype']:
                return AccountSubtype
            
            
            class verification_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AUTOMATICALLY_VERIFIED(cls):
                    return cls("automatically_verified")
                
                @schemas.classproperty
                def PENDING_AUTOMATIC_VERIFICATION(cls):
                    return cls("pending_automatic_verification")
                
                @schemas.classproperty
                def PENDING_MANUAL_VERIFICATION(cls):
                    return cls("pending_manual_verification")
                
                @schemas.classproperty
                def MANUALLY_VERIFIED(cls):
                    return cls("manually_verified")
                
                @schemas.classproperty
                def VERIFICATION_EXPIRED(cls):
                    return cls("verification_expired")
                
                @schemas.classproperty
                def VERIFICATION_FAILED(cls):
                    return cls("verification_failed")
            persistent_account_id = schemas.StrSchema
            __annotations__ = {
                "account_id": account_id,
                "balances": balances,
                "mask": mask,
                "name": name,
                "official_name": official_name,
                "type": type,
                "subtype": subtype,
                "verification_status": verification_status,
                "persistent_account_id": persistent_account_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    official_name: MetaOapg.properties.official_name
    balances: 'AccountBalance'
    account_id: MetaOapg.properties.account_id
    subtype: 'AccountSubtype'
    name: MetaOapg.properties.name
    type: 'AccountType'
    mask: MetaOapg.properties.mask
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["official_name"]) -> MetaOapg.properties.official_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balances"]) -> 'AccountBalance': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtype"]) -> 'AccountSubtype': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'AccountType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mask"]) -> MetaOapg.properties.mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_status"]) -> MetaOapg.properties.verification_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persistent_account_id"]) -> MetaOapg.properties.persistent_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["official_name"], typing_extensions.Literal["balances"], typing_extensions.Literal["account_id"], typing_extensions.Literal["subtype"], typing_extensions.Literal["name"], typing_extensions.Literal["type"], typing_extensions.Literal["mask"], typing_extensions.Literal["verification_status"], typing_extensions.Literal["persistent_account_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["official_name"]) -> MetaOapg.properties.official_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balances"]) -> 'AccountBalance': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtype"]) -> 'AccountSubtype': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'AccountType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mask"]) -> MetaOapg.properties.mask: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_status"]) -> typing.Union[MetaOapg.properties.verification_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persistent_account_id"]) -> typing.Union[MetaOapg.properties.persistent_account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["official_name"], typing_extensions.Literal["balances"], typing_extensions.Literal["account_id"], typing_extensions.Literal["subtype"], typing_extensions.Literal["name"], typing_extensions.Literal["type"], typing_extensions.Literal["mask"], typing_extensions.Literal["verification_status"], typing_extensions.Literal["persistent_account_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        official_name: typing.Union[MetaOapg.properties.official_name, None, str, ],
        balances: 'AccountBalance',
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        subtype: 'AccountSubtype',
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: 'AccountType',
        mask: typing.Union[MetaOapg.properties.mask, None, str, ],
        verification_status: typing.Union[MetaOapg.properties.verification_status, str, schemas.Unset] = schemas.unset,
        persistent_account_id: typing.Union[MetaOapg.properties.persistent_account_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AccountBase':
        return super().__new__(
            cls,
            *_args,
            official_name=official_name,
            balances=balances,
            account_id=account_id,
            subtype=subtype,
            name=name,
            type=type,
            mask=mask,
            verification_status=verification_status,
            persistent_account_id=persistent_account_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.account_balance import AccountBalance
from plaid.model.account_subtype import AccountSubtype
from plaid.model.account_type import AccountType
