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


class IncomeVerificationRiskSignalsStatusWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Fired when a risk signal is available for documents uploaded via Document Income. It will typically take a minute or two for this webhook to fire after the end user has uploaded their documents in the Document Income flow. Once this webhook has fired, `/credit/payroll_income/risk_signals/get` may then be called to retrieve risk data.
    """


    class MetaOapg:
        required = {
            "environment",
            "webhook_type",
            "item_id",
            "webhook_code",
            "status",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            item_id = schemas.StrSchema
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
            user_id = schemas.StrSchema
            risk_signals_status = schemas.StrSchema
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "item_id": item_id,
                "environment": environment,
                "user_id": user_id,
                "risk_signals_status": risk_signals_status,
            }
        additional_properties = schemas.AnyTypeSchema
    
    environment: 'WebhookEnvironmentValues'
    webhook_type: MetaOapg.properties.webhook_type
    item_id: MetaOapg.properties.item_id
    webhook_code: MetaOapg.properties.webhook_code
    status: MetaOapg.additional_properties
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk_signals_status"]) -> MetaOapg.properties.risk_signals_status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["item_id"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["status"], typing_extensions.Literal["user_id"], typing_extensions.Literal["risk_signals_status"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk_signals_status"]) -> typing.Union[MetaOapg.properties.risk_signals_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["item_id"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["status"], typing_extensions.Literal["user_id"], typing_extensions.Literal["risk_signals_status"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        item_id: typing.Union[MetaOapg.properties.item_id, str, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        status: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, schemas.Unset] = schemas.unset,
        risk_signals_status: typing.Union[MetaOapg.properties.risk_signals_status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'IncomeVerificationRiskSignalsStatusWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            webhook_type=webhook_type,
            item_id=item_id,
            webhook_code=webhook_code,
            status=status,
            user_id=user_id,
            risk_signals_status=risk_signals_status,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.webhook_environment_values import WebhookEnvironmentValues