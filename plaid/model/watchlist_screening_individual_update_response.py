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


class WatchlistScreeningIndividualUpdateResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The screening object allows you to represent a customer in your system, update their profile, and search for them on various watchlists. Note: Rejected customers will not receive new hits, regardless of program configuration.
    """


    class MetaOapg:
        required = {
            "search_terms",
            "audit_trail",
            "client_user_id",
            "assignee",
            "id",
            "request_id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def search_terms() -> typing.Type['WatchlistScreeningSearchTerms']:
                return WatchlistScreeningSearchTerms
        
            @staticmethod
            def assignee() -> typing.Type['DashboardUserIDNullable']:
                return DashboardUserIDNullable
        
            @staticmethod
            def status() -> typing.Type['WatchlistScreeningStatus']:
                return WatchlistScreeningStatus
        
            @staticmethod
            def client_user_id() -> typing.Type['ClientUserIDNullable']:
                return ClientUserIDNullable
        
            @staticmethod
            def audit_trail() -> typing.Type['WatchlistScreeningAuditTrail']:
                return WatchlistScreeningAuditTrail
            request_id = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "search_terms": search_terms,
                "assignee": assignee,
                "status": status,
                "client_user_id": client_user_id,
                "audit_trail": audit_trail,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    search_terms: 'WatchlistScreeningSearchTerms'
    audit_trail: 'WatchlistScreeningAuditTrail'
    client_user_id: 'ClientUserIDNullable'
    assignee: 'DashboardUserIDNullable'
    id: MetaOapg.properties.id
    request_id: MetaOapg.properties.request_id
    status: 'WatchlistScreeningStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["search_terms"]) -> 'WatchlistScreeningSearchTerms': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audit_trail"]) -> 'WatchlistScreeningAuditTrail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_user_id"]) -> 'ClientUserIDNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> 'DashboardUserIDNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'WatchlistScreeningStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["search_terms"], typing_extensions.Literal["audit_trail"], typing_extensions.Literal["client_user_id"], typing_extensions.Literal["assignee"], typing_extensions.Literal["id"], typing_extensions.Literal["request_id"], typing_extensions.Literal["status"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["search_terms"]) -> 'WatchlistScreeningSearchTerms': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audit_trail"]) -> 'WatchlistScreeningAuditTrail': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_user_id"]) -> 'ClientUserIDNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> 'DashboardUserIDNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'WatchlistScreeningStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["search_terms"], typing_extensions.Literal["audit_trail"], typing_extensions.Literal["client_user_id"], typing_extensions.Literal["assignee"], typing_extensions.Literal["id"], typing_extensions.Literal["request_id"], typing_extensions.Literal["status"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        search_terms: 'WatchlistScreeningSearchTerms',
        audit_trail: 'WatchlistScreeningAuditTrail',
        client_user_id: 'ClientUserIDNullable',
        assignee: 'DashboardUserIDNullable',
        id: typing.Union[MetaOapg.properties.id, str, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        status: 'WatchlistScreeningStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WatchlistScreeningIndividualUpdateResponse':
        return super().__new__(
            cls,
            *_args,
            search_terms=search_terms,
            audit_trail=audit_trail,
            client_user_id=client_user_id,
            assignee=assignee,
            id=id,
            request_id=request_id,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.client_user_id_nullable import ClientUserIDNullable
from plaid.model.dashboard_user_id_nullable import DashboardUserIDNullable
from plaid.model.watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
from plaid.model.watchlist_screening_search_terms import WatchlistScreeningSearchTerms
from plaid.model.watchlist_screening_status import WatchlistScreeningStatus