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


class ProcessorInitialUpdateWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).

Fired when an Item's initial transaction pull is completed. Once this webhook has been fired, transaction data for the most recent 30 days can be fetched for the Item. If [Account Select v2](https://plaid.com/docs/link/customization/#account-select) is enabled, this webhook will also be fired if account selections for the Item are updated, with `new_transactions` set to the number of net new transactions pulled after the account selection update.

This webhook is intended for use with `/processor/transactions/get`; if you are using the newer `/processor/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead.
    """


    class MetaOapg:
        required = {
            "environment",
            "account_id",
            "webhook_type",
            "new_transactions",
            "webhook_code",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            new_transactions = schemas.NumberSchema
            account_id = schemas.StrSchema
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
            
            
            class error(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "new_transactions": new_transactions,
                "account_id": account_id,
                "environment": environment,
                "error": error,
            }
        additional_properties = schemas.AnyTypeSchema
    
    environment: 'WebhookEnvironmentValues'
    account_id: MetaOapg.properties.account_id
    webhook_type: MetaOapg.properties.webhook_type
    new_transactions: MetaOapg.properties.new_transactions
    webhook_code: MetaOapg.properties.webhook_code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_transactions"]) -> MetaOapg.properties.new_transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["account_id"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["new_transactions"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["error"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_transactions"]) -> MetaOapg.properties.new_transactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["account_id"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["new_transactions"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["error"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        new_transactions: typing.Union[MetaOapg.properties.new_transactions, decimal.Decimal, int, float, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        error: typing.Union[MetaOapg.properties.error, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ProcessorInitialUpdateWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            account_id=account_id,
            webhook_type=webhook_type,
            new_transactions=new_transactions,
            webhook_code=webhook_code,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.webhook_environment_values import WebhookEnvironmentValues