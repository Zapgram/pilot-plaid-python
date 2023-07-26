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


class Transfer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a transfer within the Transfers API.
    """


    class MetaOapg:
        required = {
            "amount",
            "metadata",
            "credit_funds_source",
            "created",
            "guarantee_decision",
            "description",
            "failure_reason",
            "type",
            "cancellable",
            "expected_settlement_date",
            "standard_return_window",
            "network",
            "refunds",
            "funding_account_id",
            "originator_client_id",
            "guarantee_decision_rationale",
            "iso_currency_code",
            "origination_account_id",
            "recurring_transfer_id",
            "unauthorized_return_window",
            "id",
            "user",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def funding_account_id() -> typing.Type['TransferFundingAccountIDResponseNullable']:
                return TransferFundingAccountIDResponseNullable
        
            @staticmethod
            def type() -> typing.Type['TransferType']:
                return TransferType
        
            @staticmethod
            def user() -> typing.Type['TransferUserInResponse']:
                return TransferUserInResponse
            amount = schemas.StrSchema
            description = schemas.StrSchema
            created = schemas.DateTimeSchema
        
            @staticmethod
            def status() -> typing.Type['TransferStatus']:
                return TransferStatus
        
            @staticmethod
            def network() -> typing.Type['TransferNetwork']:
                return TransferNetwork
            cancellable = schemas.BoolSchema
        
            @staticmethod
            def failure_reason() -> typing.Type['TransferFailure']:
                return TransferFailure
        
            @staticmethod
            def metadata() -> typing.Type['TransferMetadata']:
                return TransferMetadata
            origination_account_id = schemas.StrSchema
        
            @staticmethod
            def guarantee_decision() -> typing.Type['TransferAuthorizationGuaranteeDecision']:
                return TransferAuthorizationGuaranteeDecision
        
            @staticmethod
            def guarantee_decision_rationale() -> typing.Type['TransferAuthorizationGuaranteeDecisionRationale']:
                return TransferAuthorizationGuaranteeDecisionRationale
            iso_currency_code = schemas.StrSchema
            
            
            class standard_return_window(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'standard_return_window':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class unauthorized_return_window(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unauthorized_return_window':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class expected_settlement_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expected_settlement_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class originator_client_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'originator_client_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class refunds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransferRefund']:
                        return TransferRefund
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TransferRefund'], typing.List['TransferRefund']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refunds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransferRefund':
                    return super().__getitem__(i)
            
            
            class recurring_transfer_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'recurring_transfer_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def credit_funds_source() -> typing.Type['TransferCreditFundsSource']:
                return TransferCreditFundsSource
        
            @staticmethod
            def ach_class() -> typing.Type['ACHClass']:
                return ACHClass
            account_id = schemas.StrSchema
        
            @staticmethod
            def sweep_status() -> typing.Type['TransferSweepStatus']:
                return TransferSweepStatus
            
            
            class expected_sweep_settlement_schedule(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransferExpectedSweepSettlementScheduleItem']:
                        return TransferExpectedSweepSettlementScheduleItem
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TransferExpectedSweepSettlementScheduleItem'], typing.List['TransferExpectedSweepSettlementScheduleItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expected_sweep_settlement_schedule':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransferExpectedSweepSettlementScheduleItem':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "funding_account_id": funding_account_id,
                "type": type,
                "user": user,
                "amount": amount,
                "description": description,
                "created": created,
                "status": status,
                "network": network,
                "cancellable": cancellable,
                "failure_reason": failure_reason,
                "metadata": metadata,
                "origination_account_id": origination_account_id,
                "guarantee_decision": guarantee_decision,
                "guarantee_decision_rationale": guarantee_decision_rationale,
                "iso_currency_code": iso_currency_code,
                "standard_return_window": standard_return_window,
                "unauthorized_return_window": unauthorized_return_window,
                "expected_settlement_date": expected_settlement_date,
                "originator_client_id": originator_client_id,
                "refunds": refunds,
                "recurring_transfer_id": recurring_transfer_id,
                "credit_funds_source": credit_funds_source,
                "ach_class": ach_class,
                "account_id": account_id,
                "sweep_status": sweep_status,
                "expected_sweep_settlement_schedule": expected_sweep_settlement_schedule,
            }
        additional_properties = schemas.AnyTypeSchema
    
    amount: MetaOapg.properties.amount
    metadata: 'TransferMetadata'
    credit_funds_source: 'TransferCreditFundsSource'
    created: MetaOapg.properties.created
    guarantee_decision: 'TransferAuthorizationGuaranteeDecision'
    description: MetaOapg.properties.description
    failure_reason: 'TransferFailure'
    type: 'TransferType'
    cancellable: MetaOapg.properties.cancellable
    expected_settlement_date: MetaOapg.properties.expected_settlement_date
    standard_return_window: MetaOapg.properties.standard_return_window
    network: 'TransferNetwork'
    refunds: MetaOapg.properties.refunds
    funding_account_id: 'TransferFundingAccountIDResponseNullable'
    originator_client_id: MetaOapg.properties.originator_client_id
    guarantee_decision_rationale: 'TransferAuthorizationGuaranteeDecisionRationale'
    iso_currency_code: MetaOapg.properties.iso_currency_code
    origination_account_id: MetaOapg.properties.origination_account_id
    recurring_transfer_id: MetaOapg.properties.recurring_transfer_id
    unauthorized_return_window: MetaOapg.properties.unauthorized_return_window
    id: MetaOapg.properties.id
    user: 'TransferUserInResponse'
    status: 'TransferStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'TransferMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credit_funds_source"]) -> 'TransferCreditFundsSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guarantee_decision"]) -> 'TransferAuthorizationGuaranteeDecision': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failure_reason"]) -> 'TransferFailure': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TransferType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancellable"]) -> MetaOapg.properties.cancellable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expected_settlement_date"]) -> MetaOapg.properties.expected_settlement_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standard_return_window"]) -> MetaOapg.properties.standard_return_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'TransferNetwork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refunds"]) -> MetaOapg.properties.refunds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["funding_account_id"]) -> 'TransferFundingAccountIDResponseNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originator_client_id"]) -> MetaOapg.properties.originator_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guarantee_decision_rationale"]) -> 'TransferAuthorizationGuaranteeDecisionRationale': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_transfer_id"]) -> MetaOapg.properties.recurring_transfer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unauthorized_return_window"]) -> MetaOapg.properties.unauthorized_return_window: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'TransferUserInResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'TransferStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach_class"]) -> 'ACHClass': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sweep_status"]) -> 'TransferSweepStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expected_sweep_settlement_schedule"]) -> MetaOapg.properties.expected_sweep_settlement_schedule: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["metadata"], typing_extensions.Literal["credit_funds_source"], typing_extensions.Literal["created"], typing_extensions.Literal["guarantee_decision"], typing_extensions.Literal["description"], typing_extensions.Literal["failure_reason"], typing_extensions.Literal["type"], typing_extensions.Literal["cancellable"], typing_extensions.Literal["expected_settlement_date"], typing_extensions.Literal["standard_return_window"], typing_extensions.Literal["network"], typing_extensions.Literal["refunds"], typing_extensions.Literal["funding_account_id"], typing_extensions.Literal["originator_client_id"], typing_extensions.Literal["guarantee_decision_rationale"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["origination_account_id"], typing_extensions.Literal["recurring_transfer_id"], typing_extensions.Literal["unauthorized_return_window"], typing_extensions.Literal["id"], typing_extensions.Literal["user"], typing_extensions.Literal["status"], typing_extensions.Literal["ach_class"], typing_extensions.Literal["account_id"], typing_extensions.Literal["sweep_status"], typing_extensions.Literal["expected_sweep_settlement_schedule"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'TransferMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credit_funds_source"]) -> 'TransferCreditFundsSource': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guarantee_decision"]) -> 'TransferAuthorizationGuaranteeDecision': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failure_reason"]) -> 'TransferFailure': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TransferType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancellable"]) -> MetaOapg.properties.cancellable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expected_settlement_date"]) -> MetaOapg.properties.expected_settlement_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standard_return_window"]) -> MetaOapg.properties.standard_return_window: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> 'TransferNetwork': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refunds"]) -> MetaOapg.properties.refunds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["funding_account_id"]) -> 'TransferFundingAccountIDResponseNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originator_client_id"]) -> MetaOapg.properties.originator_client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guarantee_decision_rationale"]) -> 'TransferAuthorizationGuaranteeDecisionRationale': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_transfer_id"]) -> MetaOapg.properties.recurring_transfer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unauthorized_return_window"]) -> MetaOapg.properties.unauthorized_return_window: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'TransferUserInResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'TransferStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach_class"]) -> typing.Union['ACHClass', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sweep_status"]) -> typing.Union['TransferSweepStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expected_sweep_settlement_schedule"]) -> typing.Union[MetaOapg.properties.expected_sweep_settlement_schedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["metadata"], typing_extensions.Literal["credit_funds_source"], typing_extensions.Literal["created"], typing_extensions.Literal["guarantee_decision"], typing_extensions.Literal["description"], typing_extensions.Literal["failure_reason"], typing_extensions.Literal["type"], typing_extensions.Literal["cancellable"], typing_extensions.Literal["expected_settlement_date"], typing_extensions.Literal["standard_return_window"], typing_extensions.Literal["network"], typing_extensions.Literal["refunds"], typing_extensions.Literal["funding_account_id"], typing_extensions.Literal["originator_client_id"], typing_extensions.Literal["guarantee_decision_rationale"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["origination_account_id"], typing_extensions.Literal["recurring_transfer_id"], typing_extensions.Literal["unauthorized_return_window"], typing_extensions.Literal["id"], typing_extensions.Literal["user"], typing_extensions.Literal["status"], typing_extensions.Literal["ach_class"], typing_extensions.Literal["account_id"], typing_extensions.Literal["sweep_status"], typing_extensions.Literal["expected_sweep_settlement_schedule"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        metadata: 'TransferMetadata',
        credit_funds_source: 'TransferCreditFundsSource',
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        guarantee_decision: 'TransferAuthorizationGuaranteeDecision',
        description: typing.Union[MetaOapg.properties.description, str, ],
        failure_reason: 'TransferFailure',
        type: 'TransferType',
        cancellable: typing.Union[MetaOapg.properties.cancellable, bool, ],
        expected_settlement_date: typing.Union[MetaOapg.properties.expected_settlement_date, None, str, date, ],
        standard_return_window: typing.Union[MetaOapg.properties.standard_return_window, None, str, date, ],
        network: 'TransferNetwork',
        refunds: typing.Union[MetaOapg.properties.refunds, list, tuple, ],
        funding_account_id: 'TransferFundingAccountIDResponseNullable',
        originator_client_id: typing.Union[MetaOapg.properties.originator_client_id, None, str, ],
        guarantee_decision_rationale: 'TransferAuthorizationGuaranteeDecisionRationale',
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        origination_account_id: typing.Union[MetaOapg.properties.origination_account_id, str, ],
        recurring_transfer_id: typing.Union[MetaOapg.properties.recurring_transfer_id, None, str, ],
        unauthorized_return_window: typing.Union[MetaOapg.properties.unauthorized_return_window, None, str, date, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        user: 'TransferUserInResponse',
        status: 'TransferStatus',
        ach_class: typing.Union['ACHClass', schemas.Unset] = schemas.unset,
        account_id: typing.Union[MetaOapg.properties.account_id, str, schemas.Unset] = schemas.unset,
        sweep_status: typing.Union['TransferSweepStatus', schemas.Unset] = schemas.unset,
        expected_sweep_settlement_schedule: typing.Union[MetaOapg.properties.expected_sweep_settlement_schedule, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'Transfer':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            metadata=metadata,
            credit_funds_source=credit_funds_source,
            created=created,
            guarantee_decision=guarantee_decision,
            description=description,
            failure_reason=failure_reason,
            type=type,
            cancellable=cancellable,
            expected_settlement_date=expected_settlement_date,
            standard_return_window=standard_return_window,
            network=network,
            refunds=refunds,
            funding_account_id=funding_account_id,
            originator_client_id=originator_client_id,
            guarantee_decision_rationale=guarantee_decision_rationale,
            iso_currency_code=iso_currency_code,
            origination_account_id=origination_account_id,
            recurring_transfer_id=recurring_transfer_id,
            unauthorized_return_window=unauthorized_return_window,
            id=id,
            user=user,
            status=status,
            ach_class=ach_class,
            account_id=account_id,
            sweep_status=sweep_status,
            expected_sweep_settlement_schedule=expected_sweep_settlement_schedule,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.ach_class import ACHClass
from plaid.model.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from plaid.model.transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from plaid.model.transfer_credit_funds_source import TransferCreditFundsSource
from plaid.model.transfer_expected_sweep_settlement_schedule_item import TransferExpectedSweepSettlementScheduleItem
from plaid.model.transfer_failure import TransferFailure
from plaid.model.transfer_funding_account_id_response_nullable import TransferFundingAccountIDResponseNullable
from plaid.model.transfer_metadata import TransferMetadata
from plaid.model.transfer_network import TransferNetwork
from plaid.model.transfer_refund import TransferRefund
from plaid.model.transfer_status import TransferStatus
from plaid.model.transfer_sweep_status import TransferSweepStatus
from plaid.model.transfer_type import TransferType
from plaid.model.transfer_user_in_response import TransferUserInResponse
