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


class WatchlistScreeningEntityReviewCreateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request input for creating a review for an entity screening
    """


    class MetaOapg:
        required = {
            "dismissed_hits",
            "entity_watchlist_screening_id",
            "confirmed_hits",
        }
        
        class properties:
            
            
            class confirmed_hits(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'confirmed_hits':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class dismissed_hits(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dismissed_hits':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            entity_watchlist_screening_id = schemas.StrSchema
        
            @staticmethod
            def comment() -> typing.Type['ReviewComment']:
                return ReviewComment
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
            __annotations__ = {
                "confirmed_hits": confirmed_hits,
                "dismissed_hits": dismissed_hits,
                "entity_watchlist_screening_id": entity_watchlist_screening_id,
                "comment": comment,
                "client_id": client_id,
                "secret": secret,
            }
    
    dismissed_hits: MetaOapg.properties.dismissed_hits
    entity_watchlist_screening_id: MetaOapg.properties.entity_watchlist_screening_id
    confirmed_hits: MetaOapg.properties.confirmed_hits
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confirmed_hits"]) -> MetaOapg.properties.confirmed_hits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dismissed_hits"]) -> MetaOapg.properties.dismissed_hits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_watchlist_screening_id"]) -> MetaOapg.properties.entity_watchlist_screening_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> 'ReviewComment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["confirmed_hits", "dismissed_hits", "entity_watchlist_screening_id", "comment", "client_id", "secret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confirmed_hits"]) -> MetaOapg.properties.confirmed_hits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dismissed_hits"]) -> MetaOapg.properties.dismissed_hits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_watchlist_screening_id"]) -> MetaOapg.properties.entity_watchlist_screening_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union['ReviewComment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["confirmed_hits", "dismissed_hits", "entity_watchlist_screening_id", "comment", "client_id", "secret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dismissed_hits: typing.Union[MetaOapg.properties.dismissed_hits, list, tuple, ],
        entity_watchlist_screening_id: typing.Union[MetaOapg.properties.entity_watchlist_screening_id, str, ],
        confirmed_hits: typing.Union[MetaOapg.properties.confirmed_hits, list, tuple, ],
        comment: typing.Union['ReviewComment', schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WatchlistScreeningEntityReviewCreateRequest':
        return super().__new__(
            cls,
            *_args,
            dismissed_hits=dismissed_hits,
            entity_watchlist_screening_id=entity_watchlist_screening_id,
            confirmed_hits=confirmed_hits,
            comment=comment,
            client_id=client_id,
            secret=secret,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.review_comment import ReviewComment
