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


class TransferRecurringListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Defines the response schema for `/transfer/recurring/list`
    """


    class MetaOapg:
        required = {
            "recurring_transfers",
            "request_id",
        }
        
        class properties:
            
            
            class recurring_transfers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RecurringTransfer']:
                        return RecurringTransfer
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RecurringTransfer'], typing.List['RecurringTransfer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'recurring_transfers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RecurringTransfer':
                    return super().__getitem__(i)
            request_id = schemas.StrSchema
            __annotations__ = {
                "recurring_transfers": recurring_transfers,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    recurring_transfers: MetaOapg.properties.recurring_transfers
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_transfers"]) -> MetaOapg.properties.recurring_transfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recurring_transfers"], typing_extensions.Literal["request_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_transfers"]) -> MetaOapg.properties.recurring_transfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recurring_transfers"], typing_extensions.Literal["request_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        recurring_transfers: typing.Union[MetaOapg.properties.recurring_transfers, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'TransferRecurringListResponse':
        return super().__new__(
            cls,
            *_args,
            recurring_transfers=recurring_transfers,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.recurring_transfer import RecurringTransfer
