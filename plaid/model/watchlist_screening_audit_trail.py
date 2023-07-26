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


class WatchlistScreeningAuditTrail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Information about the last change made to the parent object specifying what caused the change as well as when it occurred.
    """


    class MetaOapg:
        required = {
            "source",
            "dashboard_user_id",
            "timestamp",
        }
        
        class properties:
        
            @staticmethod
            def source() -> typing.Type['Source']:
                return Source
        
            @staticmethod
            def dashboard_user_id() -> typing.Type['DashboardUserIDNullable']:
                return DashboardUserIDNullable
            timestamp = schemas.DateTimeSchema
            __annotations__ = {
                "source": source,
                "dashboard_user_id": dashboard_user_id,
                "timestamp": timestamp,
            }
        additional_properties = schemas.AnyTypeSchema
    
    source: 'Source'
    dashboard_user_id: 'DashboardUserIDNullable'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'Source': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dashboard_user_id"]) -> 'DashboardUserIDNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["source"], typing_extensions.Literal["dashboard_user_id"], typing_extensions.Literal["timestamp"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> 'Source': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dashboard_user_id"]) -> 'DashboardUserIDNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["source"], typing_extensions.Literal["dashboard_user_id"], typing_extensions.Literal["timestamp"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        source: 'Source',
        dashboard_user_id: 'DashboardUserIDNullable',
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WatchlistScreeningAuditTrail':
        return super().__new__(
            cls,
            *_args,
            source=source,
            dashboard_user_id=dashboard_user_id,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.dashboard_user_id_nullable import DashboardUserIDNullable
from plaid.model.source import Source