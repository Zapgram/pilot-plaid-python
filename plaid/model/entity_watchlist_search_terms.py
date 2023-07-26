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


class EntityWatchlistSearchTerms(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Search inputs for creating an entity watchlist screening
    """


    class MetaOapg:
        required = {
            "entity_watchlist_program_id",
            "legal_name",
        }
        
        class properties:
            entity_watchlist_program_id = schemas.StrSchema
        
            @staticmethod
            def legal_name() -> typing.Type['EntityWatchlistScreeningName']:
                return EntityWatchlistScreeningName
        
            @staticmethod
            def document_number() -> typing.Type['WatchlistScreeningDocumentValueNullable']:
                return WatchlistScreeningDocumentValueNullable
        
            @staticmethod
            def email_address() -> typing.Type['EmailAddressNullable']:
                return EmailAddressNullable
        
            @staticmethod
            def country() -> typing.Type['GenericCountryCodeNullable']:
                return GenericCountryCodeNullable
        
            @staticmethod
            def phone_number() -> typing.Type['WatchlistScreeningPhoneNumberNullable']:
                return WatchlistScreeningPhoneNumberNullable
        
            @staticmethod
            def url() -> typing.Type['URLNullable']:
                return URLNullable
            __annotations__ = {
                "entity_watchlist_program_id": entity_watchlist_program_id,
                "legal_name": legal_name,
                "document_number": document_number,
                "email_address": email_address,
                "country": country,
                "phone_number": phone_number,
                "url": url,
            }
    
    entity_watchlist_program_id: MetaOapg.properties.entity_watchlist_program_id
    legal_name: 'EntityWatchlistScreeningName'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_watchlist_program_id"]) -> MetaOapg.properties.entity_watchlist_program_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal_name"]) -> 'EntityWatchlistScreeningName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["document_number"]) -> 'WatchlistScreeningDocumentValueNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> 'EmailAddressNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'GenericCountryCodeNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> 'WatchlistScreeningPhoneNumberNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> 'URLNullable': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["entity_watchlist_program_id", "legal_name", "document_number", "email_address", "country", "phone_number", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_watchlist_program_id"]) -> MetaOapg.properties.entity_watchlist_program_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal_name"]) -> 'EntityWatchlistScreeningName': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["document_number"]) -> typing.Union['WatchlistScreeningDocumentValueNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> typing.Union['EmailAddressNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union['GenericCountryCodeNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union['WatchlistScreeningPhoneNumberNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union['URLNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["entity_watchlist_program_id", "legal_name", "document_number", "email_address", "country", "phone_number", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        entity_watchlist_program_id: typing.Union[MetaOapg.properties.entity_watchlist_program_id, str, ],
        legal_name: 'EntityWatchlistScreeningName',
        document_number: typing.Union['WatchlistScreeningDocumentValueNullable', schemas.Unset] = schemas.unset,
        email_address: typing.Union['EmailAddressNullable', schemas.Unset] = schemas.unset,
        country: typing.Union['GenericCountryCodeNullable', schemas.Unset] = schemas.unset,
        phone_number: typing.Union['WatchlistScreeningPhoneNumberNullable', schemas.Unset] = schemas.unset,
        url: typing.Union['URLNullable', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EntityWatchlistSearchTerms':
        return super().__new__(
            cls,
            *_args,
            entity_watchlist_program_id=entity_watchlist_program_id,
            legal_name=legal_name,
            document_number=document_number,
            email_address=email_address,
            country=country,
            phone_number=phone_number,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.email_address_nullable import EmailAddressNullable
from plaid.model.entity_watchlist_screening_name import EntityWatchlistScreeningName
from plaid.model.generic_country_code_nullable import GenericCountryCodeNullable
from plaid.model.url_nullable import URLNullable
from plaid.model.watchlist_screening_document_value_nullable import WatchlistScreeningDocumentValueNullable
from plaid.model.watchlist_screening_phone_number_nullable import WatchlistScreeningPhoneNumberNullable