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


class ProcessorTransactionsRemovedWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).

Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook payload. Plaid will typically check for deleted transaction data several times a day.

This webhook is intended for use with `/processor/transactions/get`; if you are using the newer `/processor/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead.
    """


    class MetaOapg:
        required = {
            "environment",
            "account_id",
            "removed_transactions",
            "webhook_type",
            "webhook_code",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            
            
            class removed_transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'removed_transactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            account_id = schemas.StrSchema
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
        
            @staticmethod
            def error() -> typing.Type['PlaidError']:
                return PlaidError
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "removed_transactions": removed_transactions,
                "account_id": account_id,
                "environment": environment,
                "error": error,
            }
        additional_properties = schemas.AnyTypeSchema
    
    environment: 'WebhookEnvironmentValues'
    account_id: MetaOapg.properties.account_id
    removed_transactions: MetaOapg.properties.removed_transactions
    webhook_type: MetaOapg.properties.webhook_type
    webhook_code: MetaOapg.properties.webhook_code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["removed_transactions"]) -> MetaOapg.properties.removed_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'PlaidError': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["account_id"], typing_extensions.Literal["removed_transactions"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["error"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["removed_transactions"]) -> MetaOapg.properties.removed_transactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union['PlaidError', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["account_id"], typing_extensions.Literal["removed_transactions"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["error"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        removed_transactions: typing.Union[MetaOapg.properties.removed_transactions, list, tuple, ],
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        error: typing.Union['PlaidError', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ProcessorTransactionsRemovedWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            account_id=account_id,
            removed_transactions=removed_transactions,
            webhook_type=webhook_type,
            webhook_code=webhook_code,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.plaid_error import PlaidError
from plaid.model.webhook_environment_values import WebhookEnvironmentValues
