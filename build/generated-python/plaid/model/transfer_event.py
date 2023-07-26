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


class TransferEvent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents an event in the Transfers API.
    """


    class MetaOapg:
        required = {
            "sweep_id",
            "sweep_amount",
            "failure_reason",
            "transfer_id",
            "refund_id",
            "funding_account_id",
            "originator_client_id",
            "account_id",
            "event_id",
            "event_type",
            "transfer_amount",
            "origination_account_id",
            "transfer_type",
            "timestamp",
        }
        
        class properties:
            
            
            class event_id(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            timestamp = schemas.DateTimeSchema
        
            @staticmethod
            def event_type() -> typing.Type['TransferEventType']:
                return TransferEventType
            account_id = schemas.StrSchema
        
            @staticmethod
            def funding_account_id() -> typing.Type['TransferFundingAccountIDResponseNullable']:
                return TransferFundingAccountIDResponseNullable
            transfer_id = schemas.StrSchema
            
            
            class origination_account_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'origination_account_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def transfer_type() -> typing.Type['TransferType']:
                return TransferType
            transfer_amount = schemas.StrSchema
        
            @staticmethod
            def failure_reason() -> typing.Type['TransferFailure']:
                return TransferFailure
        
            @staticmethod
            def sweep_id() -> typing.Type['TransferSweepID']:
                return TransferSweepID
        
            @staticmethod
            def sweep_amount() -> typing.Type['TransferSweepAmount']:
                return TransferSweepAmount
            
            
            class refund_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refund_id':
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
            __annotations__ = {
                "event_id": event_id,
                "timestamp": timestamp,
                "event_type": event_type,
                "account_id": account_id,
                "funding_account_id": funding_account_id,
                "transfer_id": transfer_id,
                "origination_account_id": origination_account_id,
                "transfer_type": transfer_type,
                "transfer_amount": transfer_amount,
                "failure_reason": failure_reason,
                "sweep_id": sweep_id,
                "sweep_amount": sweep_amount,
                "refund_id": refund_id,
                "originator_client_id": originator_client_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    sweep_id: 'TransferSweepID'
    sweep_amount: 'TransferSweepAmount'
    failure_reason: 'TransferFailure'
    transfer_id: MetaOapg.properties.transfer_id
    refund_id: MetaOapg.properties.refund_id
    funding_account_id: 'TransferFundingAccountIDResponseNullable'
    originator_client_id: MetaOapg.properties.originator_client_id
    account_id: MetaOapg.properties.account_id
    event_id: MetaOapg.properties.event_id
    event_type: 'TransferEventType'
    transfer_amount: MetaOapg.properties.transfer_amount
    origination_account_id: MetaOapg.properties.origination_account_id
    transfer_type: 'TransferType'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sweep_id"]) -> 'TransferSweepID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sweep_amount"]) -> 'TransferSweepAmount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failure_reason"]) -> 'TransferFailure': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_id"]) -> MetaOapg.properties.transfer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refund_id"]) -> MetaOapg.properties.refund_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["funding_account_id"]) -> 'TransferFundingAccountIDResponseNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originator_client_id"]) -> MetaOapg.properties.originator_client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_id"]) -> MetaOapg.properties.event_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> 'TransferEventType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_amount"]) -> MetaOapg.properties.transfer_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_type"]) -> 'TransferType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sweep_id"], typing_extensions.Literal["sweep_amount"], typing_extensions.Literal["failure_reason"], typing_extensions.Literal["transfer_id"], typing_extensions.Literal["refund_id"], typing_extensions.Literal["funding_account_id"], typing_extensions.Literal["originator_client_id"], typing_extensions.Literal["account_id"], typing_extensions.Literal["event_id"], typing_extensions.Literal["event_type"], typing_extensions.Literal["transfer_amount"], typing_extensions.Literal["origination_account_id"], typing_extensions.Literal["transfer_type"], typing_extensions.Literal["timestamp"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sweep_id"]) -> 'TransferSweepID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sweep_amount"]) -> 'TransferSweepAmount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failure_reason"]) -> 'TransferFailure': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_id"]) -> MetaOapg.properties.transfer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refund_id"]) -> MetaOapg.properties.refund_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["funding_account_id"]) -> 'TransferFundingAccountIDResponseNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originator_client_id"]) -> MetaOapg.properties.originator_client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_id"]) -> MetaOapg.properties.event_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> 'TransferEventType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_amount"]) -> MetaOapg.properties.transfer_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_type"]) -> 'TransferType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sweep_id"], typing_extensions.Literal["sweep_amount"], typing_extensions.Literal["failure_reason"], typing_extensions.Literal["transfer_id"], typing_extensions.Literal["refund_id"], typing_extensions.Literal["funding_account_id"], typing_extensions.Literal["originator_client_id"], typing_extensions.Literal["account_id"], typing_extensions.Literal["event_id"], typing_extensions.Literal["event_type"], typing_extensions.Literal["transfer_amount"], typing_extensions.Literal["origination_account_id"], typing_extensions.Literal["transfer_type"], typing_extensions.Literal["timestamp"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        sweep_id: 'TransferSweepID',
        sweep_amount: 'TransferSweepAmount',
        failure_reason: 'TransferFailure',
        transfer_id: typing.Union[MetaOapg.properties.transfer_id, str, ],
        refund_id: typing.Union[MetaOapg.properties.refund_id, None, str, ],
        funding_account_id: 'TransferFundingAccountIDResponseNullable',
        originator_client_id: typing.Union[MetaOapg.properties.originator_client_id, None, str, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        event_id: typing.Union[MetaOapg.properties.event_id, decimal.Decimal, int, ],
        event_type: 'TransferEventType',
        transfer_amount: typing.Union[MetaOapg.properties.transfer_amount, str, ],
        origination_account_id: typing.Union[MetaOapg.properties.origination_account_id, None, str, ],
        transfer_type: 'TransferType',
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TransferEvent':
        return super().__new__(
            cls,
            *_args,
            sweep_id=sweep_id,
            sweep_amount=sweep_amount,
            failure_reason=failure_reason,
            transfer_id=transfer_id,
            refund_id=refund_id,
            funding_account_id=funding_account_id,
            originator_client_id=originator_client_id,
            account_id=account_id,
            event_id=event_id,
            event_type=event_type,
            transfer_amount=transfer_amount,
            origination_account_id=origination_account_id,
            transfer_type=transfer_type,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.transfer_event_type import TransferEventType
from plaid.model.transfer_failure import TransferFailure
from plaid.model.transfer_funding_account_id_response_nullable import TransferFundingAccountIDResponseNullable
from plaid.model.transfer_sweep_amount import TransferSweepAmount
from plaid.model.transfer_sweep_id import TransferSweepID
from plaid.model.transfer_type import TransferType
