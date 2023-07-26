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


class TransferAuthorization(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Contains the authorization decision for a proposed transfer.
    """


    class MetaOapg:
        required = {
            "proposed_transfer",
            "decision",
            "created",
            "guarantee_decision",
            "guarantee_decision_rationale",
            "decision_rationale",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            created = schemas.DateTimeSchema
        
            @staticmethod
            def decision() -> typing.Type['TransferAuthorizationDecision']:
                return TransferAuthorizationDecision
        
            @staticmethod
            def decision_rationale() -> typing.Type['TransferAuthorizationDecisionRationale']:
                return TransferAuthorizationDecisionRationale
        
            @staticmethod
            def guarantee_decision() -> typing.Type['TransferAuthorizationGuaranteeDecision']:
                return TransferAuthorizationGuaranteeDecision
        
            @staticmethod
            def guarantee_decision_rationale() -> typing.Type['TransferAuthorizationGuaranteeDecisionRationale']:
                return TransferAuthorizationGuaranteeDecisionRationale
        
            @staticmethod
            def proposed_transfer() -> typing.Type['TransferAuthorizationProposedTransfer']:
                return TransferAuthorizationProposedTransfer
        
            @staticmethod
            def signal_insights() -> typing.Type['SignalInsights']:
                return SignalInsights
            __annotations__ = {
                "id": id,
                "created": created,
                "decision": decision,
                "decision_rationale": decision_rationale,
                "guarantee_decision": guarantee_decision,
                "guarantee_decision_rationale": guarantee_decision_rationale,
                "proposed_transfer": proposed_transfer,
                "signal_insights": signal_insights,
            }
        additional_properties = schemas.AnyTypeSchema
    
    proposed_transfer: 'TransferAuthorizationProposedTransfer'
    decision: 'TransferAuthorizationDecision'
    created: MetaOapg.properties.created
    guarantee_decision: 'TransferAuthorizationGuaranteeDecision'
    guarantee_decision_rationale: 'TransferAuthorizationGuaranteeDecisionRationale'
    decision_rationale: 'TransferAuthorizationDecisionRationale'
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proposed_transfer"]) -> 'TransferAuthorizationProposedTransfer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision"]) -> 'TransferAuthorizationDecision': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guarantee_decision"]) -> 'TransferAuthorizationGuaranteeDecision': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guarantee_decision_rationale"]) -> 'TransferAuthorizationGuaranteeDecisionRationale': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decision_rationale"]) -> 'TransferAuthorizationDecisionRationale': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signal_insights"]) -> 'SignalInsights': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["proposed_transfer"], typing_extensions.Literal["decision"], typing_extensions.Literal["created"], typing_extensions.Literal["guarantee_decision"], typing_extensions.Literal["guarantee_decision_rationale"], typing_extensions.Literal["decision_rationale"], typing_extensions.Literal["id"], typing_extensions.Literal["signal_insights"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proposed_transfer"]) -> 'TransferAuthorizationProposedTransfer': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision"]) -> 'TransferAuthorizationDecision': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guarantee_decision"]) -> 'TransferAuthorizationGuaranteeDecision': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guarantee_decision_rationale"]) -> 'TransferAuthorizationGuaranteeDecisionRationale': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decision_rationale"]) -> 'TransferAuthorizationDecisionRationale': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signal_insights"]) -> typing.Union['SignalInsights', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["proposed_transfer"], typing_extensions.Literal["decision"], typing_extensions.Literal["created"], typing_extensions.Literal["guarantee_decision"], typing_extensions.Literal["guarantee_decision_rationale"], typing_extensions.Literal["decision_rationale"], typing_extensions.Literal["id"], typing_extensions.Literal["signal_insights"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        proposed_transfer: 'TransferAuthorizationProposedTransfer',
        decision: 'TransferAuthorizationDecision',
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        guarantee_decision: 'TransferAuthorizationGuaranteeDecision',
        guarantee_decision_rationale: 'TransferAuthorizationGuaranteeDecisionRationale',
        decision_rationale: 'TransferAuthorizationDecisionRationale',
        id: typing.Union[MetaOapg.properties.id, str, ],
        signal_insights: typing.Union['SignalInsights', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TransferAuthorization':
        return super().__new__(
            cls,
            *_args,
            proposed_transfer=proposed_transfer,
            decision=decision,
            created=created,
            guarantee_decision=guarantee_decision,
            guarantee_decision_rationale=guarantee_decision_rationale,
            decision_rationale=decision_rationale,
            id=id,
            signal_insights=signal_insights,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.signal_insights import SignalInsights
from plaid.model.transfer_authorization_decision import TransferAuthorizationDecision
from plaid.model.transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from plaid.model.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from plaid.model.transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from plaid.model.transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer
