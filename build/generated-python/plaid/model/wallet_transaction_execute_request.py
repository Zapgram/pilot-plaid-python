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


class WalletTransactionExecuteRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WalletTransactionExecuteRequest defines the request schema for `/wallet/transaction/execute`
    """


    class MetaOapg:
        required = {
            "reference",
            "amount",
            "wallet_id",
            "counterparty",
            "idempotency_key",
        }
        
        class properties:
        
            @staticmethod
            def idempotency_key() -> typing.Type['WalletTransactionIdempotencyKey']:
                return WalletTransactionIdempotencyKey
            
            
            class wallet_id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
        
            @staticmethod
            def counterparty() -> typing.Type['WalletTransactionCounterparty']:
                return WalletTransactionCounterparty
        
            @staticmethod
            def amount() -> typing.Type['WalletTransactionAmount']:
                return WalletTransactionAmount
            
            
            class reference(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 6
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
            __annotations__ = {
                "idempotency_key": idempotency_key,
                "wallet_id": wallet_id,
                "counterparty": counterparty,
                "amount": amount,
                "reference": reference,
                "client_id": client_id,
                "secret": secret,
            }
    
    reference: MetaOapg.properties.reference
    amount: 'WalletTransactionAmount'
    wallet_id: MetaOapg.properties.wallet_id
    counterparty: 'WalletTransactionCounterparty'
    idempotency_key: 'WalletTransactionIdempotencyKey'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idempotency_key"]) -> 'WalletTransactionIdempotencyKey': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wallet_id"]) -> MetaOapg.properties.wallet_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["counterparty"]) -> 'WalletTransactionCounterparty': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'WalletTransactionAmount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["idempotency_key", "wallet_id", "counterparty", "amount", "reference", "client_id", "secret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idempotency_key"]) -> 'WalletTransactionIdempotencyKey': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wallet_id"]) -> MetaOapg.properties.wallet_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["counterparty"]) -> 'WalletTransactionCounterparty': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'WalletTransactionAmount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["idempotency_key", "wallet_id", "counterparty", "amount", "reference", "client_id", "secret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        reference: typing.Union[MetaOapg.properties.reference, str, ],
        amount: 'WalletTransactionAmount',
        wallet_id: typing.Union[MetaOapg.properties.wallet_id, str, ],
        counterparty: 'WalletTransactionCounterparty',
        idempotency_key: 'WalletTransactionIdempotencyKey',
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletTransactionExecuteRequest':
        return super().__new__(
            cls,
            *_args,
            reference=reference,
            amount=amount,
            wallet_id=wallet_id,
            counterparty=counterparty,
            idempotency_key=idempotency_key,
            client_id=client_id,
            secret=secret,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.wallet_transaction_amount import WalletTransactionAmount
from plaid.model.wallet_transaction_counterparty import WalletTransactionCounterparty
from plaid.model.wallet_transaction_idempotency_key import WalletTransactionIdempotencyKey
