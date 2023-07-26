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


class HoldingsDefaultUpdateWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Fired when new or updated holdings have been detected on an investment account. The webhook typically fires in response to any newly added holdings or price changes to existing holdings, most commonly after market close.
    """


    class MetaOapg:
        required = {
            "environment",
            "webhook_type",
            "item_id",
            "new_holdings",
            "webhook_code",
            "updated_holdings",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            item_id = schemas.StrSchema
            new_holdings = schemas.NumberSchema
            updated_holdings = schemas.NumberSchema
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
        
            @staticmethod
            def error() -> typing.Type['PlaidError']:
                return PlaidError
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "item_id": item_id,
                "new_holdings": new_holdings,
                "updated_holdings": updated_holdings,
                "environment": environment,
                "error": error,
            }
        additional_properties = schemas.AnyTypeSchema
    
    environment: 'WebhookEnvironmentValues'
    webhook_type: MetaOapg.properties.webhook_type
    item_id: MetaOapg.properties.item_id
    new_holdings: MetaOapg.properties.new_holdings
    webhook_code: MetaOapg.properties.webhook_code
    updated_holdings: MetaOapg.properties.updated_holdings
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_holdings"]) -> MetaOapg.properties.new_holdings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_holdings"]) -> MetaOapg.properties.updated_holdings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'PlaidError': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["item_id"], typing_extensions.Literal["new_holdings"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["updated_holdings"], typing_extensions.Literal["error"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_holdings"]) -> MetaOapg.properties.new_holdings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_holdings"]) -> MetaOapg.properties.updated_holdings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union['PlaidError', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["item_id"], typing_extensions.Literal["new_holdings"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["updated_holdings"], typing_extensions.Literal["error"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        item_id: typing.Union[MetaOapg.properties.item_id, str, ],
        new_holdings: typing.Union[MetaOapg.properties.new_holdings, decimal.Decimal, int, float, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        updated_holdings: typing.Union[MetaOapg.properties.updated_holdings, decimal.Decimal, int, float, ],
        error: typing.Union['PlaidError', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'HoldingsDefaultUpdateWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            webhook_type=webhook_type,
            item_id=item_id,
            new_holdings=new_holdings,
            webhook_code=webhook_code,
            updated_holdings=updated_holdings,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.plaid_error import PlaidError
from plaid.model.webhook_environment_values import WebhookEnvironmentValues