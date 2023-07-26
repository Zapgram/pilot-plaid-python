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


class WatchlistScreeningIndividualHitListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Paginated list of individual watchlist screening hits
    """


    class MetaOapg:
        required = {
            "next_cursor",
            "watchlist_screening_hits",
            "request_id",
        }
        
        class properties:
            
            
            class watchlist_screening_hits(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WatchlistScreeningHit']:
                        return WatchlistScreeningHit
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WatchlistScreeningHit'], typing.List['WatchlistScreeningHit']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'watchlist_screening_hits':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WatchlistScreeningHit':
                    return super().__getitem__(i)
        
            @staticmethod
            def next_cursor() -> typing.Type['Cursor']:
                return Cursor
            request_id = schemas.StrSchema
            __annotations__ = {
                "watchlist_screening_hits": watchlist_screening_hits,
                "next_cursor": next_cursor,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    next_cursor: 'Cursor'
    watchlist_screening_hits: MetaOapg.properties.watchlist_screening_hits
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_cursor"]) -> 'Cursor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["watchlist_screening_hits"]) -> MetaOapg.properties.watchlist_screening_hits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["next_cursor"], typing_extensions.Literal["watchlist_screening_hits"], typing_extensions.Literal["request_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_cursor"]) -> 'Cursor': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["watchlist_screening_hits"]) -> MetaOapg.properties.watchlist_screening_hits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next_cursor"], typing_extensions.Literal["watchlist_screening_hits"], typing_extensions.Literal["request_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        next_cursor: 'Cursor',
        watchlist_screening_hits: typing.Union[MetaOapg.properties.watchlist_screening_hits, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WatchlistScreeningIndividualHitListResponse':
        return super().__new__(
            cls,
            *_args,
            next_cursor=next_cursor,
            watchlist_screening_hits=watchlist_screening_hits,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.cursor import Cursor
from plaid.model.watchlist_screening_hit import WatchlistScreeningHit