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


class WalletTransactionListRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WalletTransactionListRequest defines the request schema for `/wallet/transaction/list`
    """


    class MetaOapg:
        required = {
            "wallet_id",
        }
        
        class properties:
            
            
            class wallet_id(
                schemas.StrSchema
            ):
                pass
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
            
            
            class cursor(
                schemas.StrSchema
            ):
                pass
            
            
            class count(
                schemas.IntSchema
            ):
                pass
        
            @staticmethod
            def options() -> typing.Type['WalletTransactionListRequestOptions']:
                return WalletTransactionListRequestOptions
            __annotations__ = {
                "wallet_id": wallet_id,
                "client_id": client_id,
                "secret": secret,
                "cursor": cursor,
                "count": count,
                "options": options,
            }
    
    wallet_id: MetaOapg.properties.wallet_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wallet_id"]) -> MetaOapg.properties.wallet_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'WalletTransactionListRequestOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["wallet_id", "client_id", "secret", "cursor", "count", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wallet_id"]) -> MetaOapg.properties.wallet_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cursor"]) -> typing.Union[MetaOapg.properties.cursor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['WalletTransactionListRequestOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["wallet_id", "client_id", "secret", "cursor", "count", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        wallet_id: typing.Union[MetaOapg.properties.wallet_id, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        cursor: typing.Union[MetaOapg.properties.cursor, str, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        options: typing.Union['WalletTransactionListRequestOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletTransactionListRequest':
        return super().__new__(
            cls,
            *_args,
            wallet_id=wallet_id,
            client_id=client_id,
            secret=secret,
            cursor=cursor,
            count=count,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.wallet_transaction_list_request_options import WalletTransactionListRequestOptions