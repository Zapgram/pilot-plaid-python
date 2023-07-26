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


class StatementsListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    StatementsListResponse defines the response schema for `/statements/list`
    """


    class MetaOapg:
        required = {
            "item_id",
            "accounts",
            "institution_name",
            "request_id",
            "institution_id",
        }
        
        class properties:
            
            
            class accounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatementsAccount']:
                        return StatementsAccount
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['StatementsAccount'], typing.List['StatementsAccount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatementsAccount':
                    return super().__getitem__(i)
            institution_id = schemas.StrSchema
            institution_name = schemas.StrSchema
            item_id = schemas.StrSchema
            request_id = schemas.StrSchema
            __annotations__ = {
                "accounts": accounts,
                "institution_id": institution_id,
                "institution_name": institution_name,
                "item_id": item_id,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    item_id: MetaOapg.properties.item_id
    accounts: MetaOapg.properties.accounts
    institution_name: MetaOapg.properties.institution_name
    request_id: MetaOapg.properties.request_id
    institution_id: MetaOapg.properties.institution_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution_name"]) -> MetaOapg.properties.institution_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution_id"]) -> MetaOapg.properties.institution_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["item_id"], typing_extensions.Literal["accounts"], typing_extensions.Literal["institution_name"], typing_extensions.Literal["request_id"], typing_extensions.Literal["institution_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution_name"]) -> MetaOapg.properties.institution_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution_id"]) -> MetaOapg.properties.institution_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["item_id"], typing_extensions.Literal["accounts"], typing_extensions.Literal["institution_name"], typing_extensions.Literal["request_id"], typing_extensions.Literal["institution_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        item_id: typing.Union[MetaOapg.properties.item_id, str, ],
        accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, ],
        institution_name: typing.Union[MetaOapg.properties.institution_name, str, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        institution_id: typing.Union[MetaOapg.properties.institution_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'StatementsListResponse':
        return super().__new__(
            cls,
            *_args,
            item_id=item_id,
            accounts=accounts,
            institution_name=institution_name,
            request_id=request_id,
            institution_id=institution_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.statements_account import StatementsAccount
