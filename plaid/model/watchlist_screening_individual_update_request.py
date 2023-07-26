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


class WatchlistScreeningIndividualUpdateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request input for editing an individual watchlist screening
    """


    class MetaOapg:
        required = {
            "watchlist_screening_id",
        }
        
        class properties:
            watchlist_screening_id = schemas.StrSchema
        
            @staticmethod
            def search_terms() -> typing.Type['UpdateIndividualScreeningRequestSearchTerms']:
                return UpdateIndividualScreeningRequestSearchTerms
            assignee = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['WatchlistScreeningStatus']:
                return WatchlistScreeningStatus
        
            @staticmethod
            def client_user_id() -> typing.Type['ClientUserID']:
                return ClientUserID
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
        
            @staticmethod
            def reset_fields() -> typing.Type['WatchlistScreeningIndividualUpdateRequestResettableFieldList']:
                return WatchlistScreeningIndividualUpdateRequestResettableFieldList
            __annotations__ = {
                "watchlist_screening_id": watchlist_screening_id,
                "search_terms": search_terms,
                "assignee": assignee,
                "status": status,
                "client_user_id": client_user_id,
                "client_id": client_id,
                "secret": secret,
                "reset_fields": reset_fields,
            }
    
    watchlist_screening_id: MetaOapg.properties.watchlist_screening_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["watchlist_screening_id"]) -> MetaOapg.properties.watchlist_screening_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["search_terms"]) -> 'UpdateIndividualScreeningRequestSearchTerms': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'WatchlistScreeningStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_user_id"]) -> 'ClientUserID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reset_fields"]) -> 'WatchlistScreeningIndividualUpdateRequestResettableFieldList': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["watchlist_screening_id", "search_terms", "assignee", "status", "client_user_id", "client_id", "secret", "reset_fields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["watchlist_screening_id"]) -> MetaOapg.properties.watchlist_screening_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["search_terms"]) -> typing.Union['UpdateIndividualScreeningRequestSearchTerms', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> typing.Union[MetaOapg.properties.assignee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['WatchlistScreeningStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_user_id"]) -> typing.Union['ClientUserID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reset_fields"]) -> typing.Union['WatchlistScreeningIndividualUpdateRequestResettableFieldList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["watchlist_screening_id", "search_terms", "assignee", "status", "client_user_id", "client_id", "secret", "reset_fields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        watchlist_screening_id: typing.Union[MetaOapg.properties.watchlist_screening_id, str, ],
        search_terms: typing.Union['UpdateIndividualScreeningRequestSearchTerms', schemas.Unset] = schemas.unset,
        assignee: typing.Union[MetaOapg.properties.assignee, str, schemas.Unset] = schemas.unset,
        status: typing.Union['WatchlistScreeningStatus', schemas.Unset] = schemas.unset,
        client_user_id: typing.Union['ClientUserID', schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        reset_fields: typing.Union['WatchlistScreeningIndividualUpdateRequestResettableFieldList', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WatchlistScreeningIndividualUpdateRequest':
        return super().__new__(
            cls,
            *_args,
            watchlist_screening_id=watchlist_screening_id,
            search_terms=search_terms,
            assignee=assignee,
            status=status,
            client_user_id=client_user_id,
            client_id=client_id,
            secret=secret,
            reset_fields=reset_fields,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.client_user_id import ClientUserID
from plaid.model.update_individual_screening_request_search_terms import UpdateIndividualScreeningRequestSearchTerms
from plaid.model.watchlist_screening_individual_update_request_resettable_field_list import WatchlistScreeningIndividualUpdateRequestResettableFieldList
from plaid.model.watchlist_screening_status import WatchlistScreeningStatus