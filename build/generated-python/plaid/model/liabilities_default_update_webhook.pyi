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


class LiabilitiesDefaultUpdateWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The webhook of type `LIABILITIES` and code `DEFAULT_UPDATE` will be fired when new or updated liabilities have been detected on a liabilities item.
    """


    class MetaOapg:
        required = {
            "environment",
            "webhook_type",
            "item_id",
            "account_ids_with_updated_liabilities",
            "webhook_code",
            "account_ids_with_new_liabilities",
            "error",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            item_id = schemas.StrSchema
        
            @staticmethod
            def error() -> typing.Type['PlaidError']:
                return PlaidError
            
            
            class account_ids_with_new_liabilities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_ids_with_new_liabilities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def account_ids_with_updated_liabilities() -> typing.Type['LiabilitiesAccountIdsWithUpdatedLiabilities']:
                return LiabilitiesAccountIdsWithUpdatedLiabilities
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "item_id": item_id,
                "error": error,
                "account_ids_with_new_liabilities": account_ids_with_new_liabilities,
                "account_ids_with_updated_liabilities": account_ids_with_updated_liabilities,
                "environment": environment,
            }
    
    environment: 'WebhookEnvironmentValues'
    webhook_type: MetaOapg.properties.webhook_type
    item_id: MetaOapg.properties.item_id
    account_ids_with_updated_liabilities: 'LiabilitiesAccountIdsWithUpdatedLiabilities'
    webhook_code: MetaOapg.properties.webhook_code
    account_ids_with_new_liabilities: MetaOapg.properties.account_ids_with_new_liabilities
    error: 'PlaidError'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'PlaidError': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_ids_with_new_liabilities"]) -> MetaOapg.properties.account_ids_with_new_liabilities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_ids_with_updated_liabilities"]) -> 'LiabilitiesAccountIdsWithUpdatedLiabilities': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["webhook_type", "webhook_code", "item_id", "error", "account_ids_with_new_liabilities", "account_ids_with_updated_liabilities", "environment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> 'PlaidError': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_ids_with_new_liabilities"]) -> MetaOapg.properties.account_ids_with_new_liabilities: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_ids_with_updated_liabilities"]) -> 'LiabilitiesAccountIdsWithUpdatedLiabilities': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["webhook_type", "webhook_code", "item_id", "error", "account_ids_with_new_liabilities", "account_ids_with_updated_liabilities", "environment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        item_id: typing.Union[MetaOapg.properties.item_id, str, ],
        account_ids_with_updated_liabilities: 'LiabilitiesAccountIdsWithUpdatedLiabilities',
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        account_ids_with_new_liabilities: typing.Union[MetaOapg.properties.account_ids_with_new_liabilities, list, tuple, ],
        error: 'PlaidError',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiabilitiesDefaultUpdateWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            webhook_type=webhook_type,
            item_id=item_id,
            account_ids_with_updated_liabilities=account_ids_with_updated_liabilities,
            webhook_code=webhook_code,
            account_ids_with_new_liabilities=account_ids_with_new_liabilities,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.liabilities_account_ids_with_updated_liabilities import LiabilitiesAccountIdsWithUpdatedLiabilities
from plaid.model.plaid_error import PlaidError
from plaid.model.webhook_environment_values import WebhookEnvironmentValues
