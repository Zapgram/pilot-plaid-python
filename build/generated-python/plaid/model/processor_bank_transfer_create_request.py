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


class ProcessorBankTransferCreateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Defines the request schema for `/processor/bank_transfer/create`
    """


    class MetaOapg:
        required = {
            "amount",
            "iso_currency_code",
            "description",
            "idempotency_key",
            "processor_token",
            "type",
            "user",
            "network",
        }
        
        class properties:
        
            @staticmethod
            def idempotency_key() -> typing.Type['BankTransferIdempotencyKey']:
                return BankTransferIdempotencyKey
            processor_token = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['BankTransferType']:
                return BankTransferType
        
            @staticmethod
            def network() -> typing.Type['BankTransferNetwork']:
                return BankTransferNetwork
            amount = schemas.StrSchema
            iso_currency_code = schemas.StrSchema
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
        
            @staticmethod
            def user() -> typing.Type['BankTransferUser']:
                return BankTransferUser
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
        
            @staticmethod
            def ach_class() -> typing.Type['ACHClass']:
                return ACHClass
            
            
            class custom_tag(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_tag':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def metadata() -> typing.Type['BankTransferMetadata']:
                return BankTransferMetadata
            
            
            class origination_account_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'origination_account_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "idempotency_key": idempotency_key,
                "processor_token": processor_token,
                "type": type,
                "network": network,
                "amount": amount,
                "iso_currency_code": iso_currency_code,
                "description": description,
                "user": user,
                "client_id": client_id,
                "secret": secret,
                "ach_class": ach_class,
                "custom_tag": custom_tag,
                "metadata": metadata,
                "origination_account_id": origination_account_id,
            }
    
    amount: MetaOapg.properties.amount
    iso_currency_code: MetaOapg.properties.iso_currency_code
    description: MetaOapg.properties.description
    idempotency_key: 'BankTransferIdempotencyKey'
    processor_token: MetaOapg.properties.processor_token
    type: 'BankTransferType'
    user: 'BankTransferUser'
    network: 'BankTransferNetwork'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idempotency_key"]) -> 'BankTransferIdempotencyKey': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processor_token"]) -> MetaOapg.properties.processor_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'BankTransferType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'BankTransferNetwork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'BankTransferUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach_class"]) -> 'ACHClass': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_tag"]) -> MetaOapg.properties.custom_tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'BankTransferMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["idempotency_key", "processor_token", "type", "network", "amount", "iso_currency_code", "description", "user", "client_id", "secret", "ach_class", "custom_tag", "metadata", "origination_account_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idempotency_key"]) -> 'BankTransferIdempotencyKey': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processor_token"]) -> MetaOapg.properties.processor_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'BankTransferType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> 'BankTransferNetwork': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'BankTransferUser': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach_class"]) -> typing.Union['ACHClass', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_tag"]) -> typing.Union[MetaOapg.properties.custom_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['BankTransferMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origination_account_id"]) -> typing.Union[MetaOapg.properties.origination_account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["idempotency_key", "processor_token", "type", "network", "amount", "iso_currency_code", "description", "user", "client_id", "secret", "ach_class", "custom_tag", "metadata", "origination_account_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        idempotency_key: 'BankTransferIdempotencyKey',
        processor_token: typing.Union[MetaOapg.properties.processor_token, str, ],
        type: 'BankTransferType',
        user: 'BankTransferUser',
        network: 'BankTransferNetwork',
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        ach_class: typing.Union['ACHClass', schemas.Unset] = schemas.unset,
        custom_tag: typing.Union[MetaOapg.properties.custom_tag, None, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['BankTransferMetadata', schemas.Unset] = schemas.unset,
        origination_account_id: typing.Union[MetaOapg.properties.origination_account_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProcessorBankTransferCreateRequest':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            iso_currency_code=iso_currency_code,
            description=description,
            idempotency_key=idempotency_key,
            processor_token=processor_token,
            type=type,
            user=user,
            network=network,
            client_id=client_id,
            secret=secret,
            ach_class=ach_class,
            custom_tag=custom_tag,
            metadata=metadata,
            origination_account_id=origination_account_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.ach_class import ACHClass
from plaid.model.bank_transfer_idempotency_key import BankTransferIdempotencyKey
from plaid.model.bank_transfer_metadata import BankTransferMetadata
from plaid.model.bank_transfer_network import BankTransferNetwork
from plaid.model.bank_transfer_type import BankTransferType
from plaid.model.bank_transfer_user import BankTransferUser
