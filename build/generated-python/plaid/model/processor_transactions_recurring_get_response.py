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


class ProcessorTransactionsRecurringGetResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ProcessorTransactionsRecurringGetResponse defines the response schema for `/processor/transactions/recurring/get`
    """


    class MetaOapg:
        required = {
            "inflow_streams",
            "updated_datetime",
            "request_id",
            "outflow_streams",
        }
        
        class properties:
            
            
            class inflow_streams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionStream']:
                        return TransactionStream
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TransactionStream'], typing.List['TransactionStream']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'inflow_streams':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransactionStream':
                    return super().__getitem__(i)
            
            
            class outflow_streams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionStream']:
                        return TransactionStream
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TransactionStream'], typing.List['TransactionStream']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'outflow_streams':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransactionStream':
                    return super().__getitem__(i)
            updated_datetime = schemas.DateTimeSchema
            request_id = schemas.StrSchema
            __annotations__ = {
                "inflow_streams": inflow_streams,
                "outflow_streams": outflow_streams,
                "updated_datetime": updated_datetime,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    inflow_streams: MetaOapg.properties.inflow_streams
    updated_datetime: MetaOapg.properties.updated_datetime
    request_id: MetaOapg.properties.request_id
    outflow_streams: MetaOapg.properties.outflow_streams
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inflow_streams"]) -> MetaOapg.properties.inflow_streams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_datetime"]) -> MetaOapg.properties.updated_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outflow_streams"]) -> MetaOapg.properties.outflow_streams: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["inflow_streams"], typing_extensions.Literal["updated_datetime"], typing_extensions.Literal["request_id"], typing_extensions.Literal["outflow_streams"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inflow_streams"]) -> MetaOapg.properties.inflow_streams: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_datetime"]) -> MetaOapg.properties.updated_datetime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outflow_streams"]) -> MetaOapg.properties.outflow_streams: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inflow_streams"], typing_extensions.Literal["updated_datetime"], typing_extensions.Literal["request_id"], typing_extensions.Literal["outflow_streams"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        inflow_streams: typing.Union[MetaOapg.properties.inflow_streams, list, tuple, ],
        updated_datetime: typing.Union[MetaOapg.properties.updated_datetime, str, datetime, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        outflow_streams: typing.Union[MetaOapg.properties.outflow_streams, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ProcessorTransactionsRecurringGetResponse':
        return super().__new__(
            cls,
            *_args,
            inflow_streams=inflow_streams,
            updated_datetime=updated_datetime,
            request_id=request_id,
            outflow_streams=outflow_streams,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.transaction_stream import TransactionStream
