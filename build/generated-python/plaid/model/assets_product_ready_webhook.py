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


class AssetsProductReadyWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Fired when the Asset Report has been generated and `/asset_report/get` is ready to be called.  If you attempt to retrieve an Asset Report before this webhook has fired, you’ll receive a response with the HTTP status code 400 and a Plaid error code of `PRODUCT_NOT_READY`.
    """


    class MetaOapg:
        required = {
            "environment",
            "webhook_type",
            "webhook_code",
            "asset_report_id",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            asset_report_id = schemas.StrSchema
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
            report_type = schemas.StrSchema
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "asset_report_id": asset_report_id,
                "environment": environment,
                "report_type": report_type,
            }
        additional_properties = schemas.AnyTypeSchema
    
    environment: 'WebhookEnvironmentValues'
    webhook_type: MetaOapg.properties.webhook_type
    webhook_code: MetaOapg.properties.webhook_code
    asset_report_id: MetaOapg.properties.asset_report_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset_report_id"]) -> MetaOapg.properties.asset_report_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_type"]) -> MetaOapg.properties.report_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["asset_report_id"], typing_extensions.Literal["report_type"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset_report_id"]) -> MetaOapg.properties.asset_report_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_type"]) -> typing.Union[MetaOapg.properties.report_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["asset_report_id"], typing_extensions.Literal["report_type"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        asset_report_id: typing.Union[MetaOapg.properties.asset_report_id, str, ],
        report_type: typing.Union[MetaOapg.properties.report_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AssetsProductReadyWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            webhook_type=webhook_type,
            webhook_code=webhook_code,
            asset_report_id=asset_report_id,
            report_type=report_type,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.webhook_environment_values import WebhookEnvironmentValues
