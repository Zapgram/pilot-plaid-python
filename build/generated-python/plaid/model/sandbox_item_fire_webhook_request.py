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


class SandboxItemFireWebhookRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    SandboxItemFireWebhookRequest defines the request schema for `/sandbox/item/fire_webhook`
    """


    class MetaOapg:
        required = {
            "access_token",
            "webhook_code",
        }
        
        class properties:
            access_token = schemas.StrSchema
            
            
            class webhook_code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DEFAULT_UPDATE": "DEFAULT_UPDATE",
                        "NEW_ACCOUNTS_AVAILABLE": "NEW_ACCOUNTS_AVAILABLE",
                        "AUTH_DATA_UPDATE": "AUTH_DATA_UPDATE",
                        "RECURRING_TRANSACTIONS_UPDATE": "RECURRING_TRANSACTIONS_UPDATE",
                        "SYNC_UPDATES_AVAILABLE": "SYNC_UPDATES_AVAILABLE",
                        "PRODUCT_READY": "PRODUCT_READY",
                        "ERROR": "ERROR",
                    }
                
                @schemas.classproperty
                def DEFAULT_UPDATE(cls):
                    return cls("DEFAULT_UPDATE")
                
                @schemas.classproperty
                def NEW_ACCOUNTS_AVAILABLE(cls):
                    return cls("NEW_ACCOUNTS_AVAILABLE")
                
                @schemas.classproperty
                def AUTH_DATA_UPDATE(cls):
                    return cls("AUTH_DATA_UPDATE")
                
                @schemas.classproperty
                def RECURRING_TRANSACTIONS_UPDATE(cls):
                    return cls("RECURRING_TRANSACTIONS_UPDATE")
                
                @schemas.classproperty
                def SYNC_UPDATES_AVAILABLE(cls):
                    return cls("SYNC_UPDATES_AVAILABLE")
                
                @schemas.classproperty
                def PRODUCT_READY(cls):
                    return cls("PRODUCT_READY")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
        
            @staticmethod
            def webhook_type() -> typing.Type['WebhookType']:
                return WebhookType
            __annotations__ = {
                "access_token": access_token,
                "webhook_code": webhook_code,
                "client_id": client_id,
                "secret": secret,
                "webhook_type": webhook_type,
            }
    
    access_token: MetaOapg.properties.access_token
    webhook_code: MetaOapg.properties.webhook_code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> 'WebhookType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_token", "webhook_code", "client_id", "secret", "webhook_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> typing.Union['WebhookType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_token", "webhook_code", "client_id", "secret", "webhook_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        access_token: typing.Union[MetaOapg.properties.access_token, str, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        webhook_type: typing.Union['WebhookType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SandboxItemFireWebhookRequest':
        return super().__new__(
            cls,
            *_args,
            access_token=access_token,
            webhook_code=webhook_code,
            client_id=client_id,
            secret=secret,
            webhook_type=webhook_type,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.webhook_type import WebhookType
