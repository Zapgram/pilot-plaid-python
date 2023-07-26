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


class RecurringTransfer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a recurring transfer within the Transfers API.
    """


    class MetaOapg:
        required = {
            "amount",
            "transfer_ids",
            "created",
            "description",
            "type",
            "network",
            "funding_account_id",
            "schedule",
            "account_id",
            "next_origination_date",
            "iso_currency_code",
            "origination_account_id",
            "recurring_transfer_id",
            "user",
            "status",
        }
        
        class properties:
            recurring_transfer_id = schemas.StrSchema
            created = schemas.DateTimeSchema
            
            
            class next_origination_date(
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
                ) -> 'next_origination_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def type() -> typing.Type['TransferType']:
                return TransferType
            amount = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['TransferRecurringStatus']:
                return TransferRecurringStatus
        
            @staticmethod
            def network() -> typing.Type['TransferNetwork']:
                return TransferNetwork
            origination_account_id = schemas.StrSchema
            account_id = schemas.StrSchema
            funding_account_id = schemas.StrSchema
            iso_currency_code = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class transfer_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transfer_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def user() -> typing.Type['TransferUserInResponse']:
                return TransferUserInResponse
        
            @staticmethod
            def schedule() -> typing.Type['TransferRecurringSchedule']:
                return TransferRecurringSchedule
            
            
            class test_clock_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'test_clock_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def ach_class() -> typing.Type['ACHClass']:
                return ACHClass
            __annotations__ = {
                "recurring_transfer_id": recurring_transfer_id,
                "created": created,
                "next_origination_date": next_origination_date,
                "type": type,
                "amount": amount,
                "status": status,
                "network": network,
                "origination_account_id": origination_account_id,
                "account_id": account_id,
                "funding_account_id": funding_account_id,
                "iso_currency_code": iso_currency_code,
                "description": description,
                "transfer_ids": transfer_ids,
                "user": user,
                "schedule": schedule,
                "test_clock_id": test_clock_id,
                "ach_class": ach_class,
            }
        additional_properties = schemas.AnyTypeSchema
    
    amount: MetaOapg.properties.amount
    transfer_ids: MetaOapg.properties.transfer_ids
    created: MetaOapg.properties.created
    description: MetaOapg.properties.description
    type: 'TransferType'
    network: 'TransferNetwork'
    funding_account_id: MetaOapg.properties.funding_account_id
    schedule: 'TransferRecurringSchedule'
    account_id: MetaOapg.properties.account_id
    next_origination_date: MetaOapg.properties.next_origination_date
    iso_currency_code: MetaOapg.properties.iso_currency_code
    origination_account_id: MetaOapg.properties.origination_account_id
    recurring_transfer_id: MetaOapg.properties.recurring_transfer_id
    user: 'TransferUserInResponse'
    status: 'TransferRecurringStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_ids"]) -> MetaOapg.properties.transfer_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TransferType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'TransferNetwork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["funding_account_id"]) -> MetaOapg.properties.funding_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'TransferRecurringSchedule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_origination_date"]) -> MetaOapg.properties.next_origination_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_transfer_id"]) -> MetaOapg.properties.recurring_transfer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'TransferUserInResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'TransferRecurringStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["test_clock_id"]) -> MetaOapg.properties.test_clock_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach_class"]) -> 'ACHClass': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["transfer_ids"], typing_extensions.Literal["created"], typing_extensions.Literal["description"], typing_extensions.Literal["type"], typing_extensions.Literal["network"], typing_extensions.Literal["funding_account_id"], typing_extensions.Literal["schedule"], typing_extensions.Literal["account_id"], typing_extensions.Literal["next_origination_date"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["origination_account_id"], typing_extensions.Literal["recurring_transfer_id"], typing_extensions.Literal["user"], typing_extensions.Literal["status"], typing_extensions.Literal["test_clock_id"], typing_extensions.Literal["ach_class"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_ids"]) -> MetaOapg.properties.transfer_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TransferType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> 'TransferNetwork': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["funding_account_id"]) -> MetaOapg.properties.funding_account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> 'TransferRecurringSchedule': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_origination_date"]) -> MetaOapg.properties.next_origination_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origination_account_id"]) -> MetaOapg.properties.origination_account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_transfer_id"]) -> MetaOapg.properties.recurring_transfer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'TransferUserInResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'TransferRecurringStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["test_clock_id"]) -> typing.Union[MetaOapg.properties.test_clock_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach_class"]) -> typing.Union['ACHClass', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["transfer_ids"], typing_extensions.Literal["created"], typing_extensions.Literal["description"], typing_extensions.Literal["type"], typing_extensions.Literal["network"], typing_extensions.Literal["funding_account_id"], typing_extensions.Literal["schedule"], typing_extensions.Literal["account_id"], typing_extensions.Literal["next_origination_date"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["origination_account_id"], typing_extensions.Literal["recurring_transfer_id"], typing_extensions.Literal["user"], typing_extensions.Literal["status"], typing_extensions.Literal["test_clock_id"], typing_extensions.Literal["ach_class"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        transfer_ids: typing.Union[MetaOapg.properties.transfer_ids, list, tuple, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        type: 'TransferType',
        network: 'TransferNetwork',
        funding_account_id: typing.Union[MetaOapg.properties.funding_account_id, str, ],
        schedule: 'TransferRecurringSchedule',
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        next_origination_date: typing.Union[MetaOapg.properties.next_origination_date, None, str, date, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        origination_account_id: typing.Union[MetaOapg.properties.origination_account_id, str, ],
        recurring_transfer_id: typing.Union[MetaOapg.properties.recurring_transfer_id, str, ],
        user: 'TransferUserInResponse',
        status: 'TransferRecurringStatus',
        test_clock_id: typing.Union[MetaOapg.properties.test_clock_id, None, str, schemas.Unset] = schemas.unset,
        ach_class: typing.Union['ACHClass', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'RecurringTransfer':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            transfer_ids=transfer_ids,
            created=created,
            description=description,
            type=type,
            network=network,
            funding_account_id=funding_account_id,
            schedule=schedule,
            account_id=account_id,
            next_origination_date=next_origination_date,
            iso_currency_code=iso_currency_code,
            origination_account_id=origination_account_id,
            recurring_transfer_id=recurring_transfer_id,
            user=user,
            status=status,
            test_clock_id=test_clock_id,
            ach_class=ach_class,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.ach_class import ACHClass
from plaid.model.transfer_network import TransferNetwork
from plaid.model.transfer_recurring_schedule import TransferRecurringSchedule
from plaid.model.transfer_recurring_status import TransferRecurringStatus
from plaid.model.transfer_type import TransferType
from plaid.model.transfer_user_in_response import TransferUserInResponse
