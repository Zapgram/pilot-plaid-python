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


class WalletTransactionListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WalletTransactionListResponse defines the response schema for `/wallet/transaction/list`
    """


    class MetaOapg:
        required = {
            "transactions",
            "request_id",
        }
        
        class properties:
            
            
            class transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletTransaction']:
                        return WalletTransaction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WalletTransaction'], typing.List['WalletTransaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WalletTransaction':
                    return super().__getitem__(i)
            request_id = schemas.StrSchema
            next_cursor = schemas.StrSchema
            __annotations__ = {
                "transactions": transactions,
                "request_id": request_id,
                "next_cursor": next_cursor,
            }
        additional_properties = schemas.AnyTypeSchema
    
    transactions: MetaOapg.properties.transactions
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_cursor"]) -> MetaOapg.properties.next_cursor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transactions"], typing_extensions.Literal["request_id"], typing_extensions.Literal["next_cursor"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_cursor"]) -> typing.Union[MetaOapg.properties.next_cursor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transactions"], typing_extensions.Literal["request_id"], typing_extensions.Literal["next_cursor"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        next_cursor: typing.Union[MetaOapg.properties.next_cursor, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WalletTransactionListResponse':
        return super().__new__(
            cls,
            *_args,
            transactions=transactions,
            request_id=request_id,
            next_cursor=next_cursor,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.wallet_transaction import WalletTransaction
