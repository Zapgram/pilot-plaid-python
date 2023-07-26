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


class WatchlistScreeningEntityHistoryListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Paginated list of entity watchlist screenings
    """


    class MetaOapg:
        required = {
            "next_cursor",
            "entity_watchlist_screenings",
            "request_id",
        }
        
        class properties:
            
            
            class entity_watchlist_screenings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EntityWatchlistScreening']:
                        return EntityWatchlistScreening
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['EntityWatchlistScreening'], typing.List['EntityWatchlistScreening']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entity_watchlist_screenings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EntityWatchlistScreening':
                    return super().__getitem__(i)
        
            @staticmethod
            def next_cursor() -> typing.Type['Cursor']:
                return Cursor
            request_id = schemas.StrSchema
            __annotations__ = {
                "entity_watchlist_screenings": entity_watchlist_screenings,
                "next_cursor": next_cursor,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    next_cursor: 'Cursor'
    entity_watchlist_screenings: MetaOapg.properties.entity_watchlist_screenings
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_cursor"]) -> 'Cursor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_watchlist_screenings"]) -> MetaOapg.properties.entity_watchlist_screenings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["next_cursor"], typing_extensions.Literal["entity_watchlist_screenings"], typing_extensions.Literal["request_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_cursor"]) -> 'Cursor': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_watchlist_screenings"]) -> MetaOapg.properties.entity_watchlist_screenings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next_cursor"], typing_extensions.Literal["entity_watchlist_screenings"], typing_extensions.Literal["request_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        next_cursor: 'Cursor',
        entity_watchlist_screenings: typing.Union[MetaOapg.properties.entity_watchlist_screenings, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WatchlistScreeningEntityHistoryListResponse':
        return super().__new__(
            cls,
            *_args,
            next_cursor=next_cursor,
            entity_watchlist_screenings=entity_watchlist_screenings,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.cursor import Cursor
from plaid.model.entity_watchlist_screening import EntityWatchlistScreening
