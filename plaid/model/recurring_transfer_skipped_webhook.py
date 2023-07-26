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


class RecurringTransferSkippedWebhook(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Fired when Plaid is unable to originate a new ACH transaction of the recurring transfer on the planned date.
    """


    class MetaOapg:
        required = {
            "environment",
            "webhook_type",
            "skipped_origination_date",
            "authorization_decision",
            "recurring_transfer_id",
            "webhook_code",
        }
        
        class properties:
            webhook_type = schemas.StrSchema
            webhook_code = schemas.StrSchema
            recurring_transfer_id = schemas.StrSchema
        
            @staticmethod
            def authorization_decision() -> typing.Type['TransferAuthorizationDecision']:
                return TransferAuthorizationDecision
            skipped_origination_date = schemas.DateSchema
        
            @staticmethod
            def environment() -> typing.Type['WebhookEnvironmentValues']:
                return WebhookEnvironmentValues
        
            @staticmethod
            def authorization_decision_rationale_code() -> typing.Type['TransferAuthorizationDecisionRationaleCode']:
                return TransferAuthorizationDecisionRationaleCode
            __annotations__ = {
                "webhook_type": webhook_type,
                "webhook_code": webhook_code,
                "recurring_transfer_id": recurring_transfer_id,
                "authorization_decision": authorization_decision,
                "skipped_origination_date": skipped_origination_date,
                "environment": environment,
                "authorization_decision_rationale_code": authorization_decision_rationale_code,
            }
        additional_properties = schemas.AnyTypeSchema
    
    environment: 'WebhookEnvironmentValues'
    webhook_type: MetaOapg.properties.webhook_type
    skipped_origination_date: MetaOapg.properties.skipped_origination_date
    authorization_decision: 'TransferAuthorizationDecision'
    recurring_transfer_id: MetaOapg.properties.recurring_transfer_id
    webhook_code: MetaOapg.properties.webhook_code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skipped_origination_date"]) -> MetaOapg.properties.skipped_origination_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization_decision"]) -> 'TransferAuthorizationDecision': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_transfer_id"]) -> MetaOapg.properties.recurring_transfer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization_decision_rationale_code"]) -> 'TransferAuthorizationDecisionRationaleCode': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["skipped_origination_date"], typing_extensions.Literal["authorization_decision"], typing_extensions.Literal["recurring_transfer_id"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["authorization_decision_rationale_code"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'WebhookEnvironmentValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_type"]) -> MetaOapg.properties.webhook_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skipped_origination_date"]) -> MetaOapg.properties.skipped_origination_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization_decision"]) -> 'TransferAuthorizationDecision': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_transfer_id"]) -> MetaOapg.properties.recurring_transfer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_code"]) -> MetaOapg.properties.webhook_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization_decision_rationale_code"]) -> typing.Union['TransferAuthorizationDecisionRationaleCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["environment"], typing_extensions.Literal["webhook_type"], typing_extensions.Literal["skipped_origination_date"], typing_extensions.Literal["authorization_decision"], typing_extensions.Literal["recurring_transfer_id"], typing_extensions.Literal["webhook_code"], typing_extensions.Literal["authorization_decision_rationale_code"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        environment: 'WebhookEnvironmentValues',
        webhook_type: typing.Union[MetaOapg.properties.webhook_type, str, ],
        skipped_origination_date: typing.Union[MetaOapg.properties.skipped_origination_date, str, date, ],
        authorization_decision: 'TransferAuthorizationDecision',
        recurring_transfer_id: typing.Union[MetaOapg.properties.recurring_transfer_id, str, ],
        webhook_code: typing.Union[MetaOapg.properties.webhook_code, str, ],
        authorization_decision_rationale_code: typing.Union['TransferAuthorizationDecisionRationaleCode', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'RecurringTransferSkippedWebhook':
        return super().__new__(
            cls,
            *_args,
            environment=environment,
            webhook_type=webhook_type,
            skipped_origination_date=skipped_origination_date,
            authorization_decision=authorization_decision,
            recurring_transfer_id=recurring_transfer_id,
            webhook_code=webhook_code,
            authorization_decision_rationale_code=authorization_decision_rationale_code,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.transfer_authorization_decision import TransferAuthorizationDecision
from plaid.model.transfer_authorization_decision_rationale_code import TransferAuthorizationDecisionRationaleCode
from plaid.model.webhook_environment_values import WebhookEnvironmentValues