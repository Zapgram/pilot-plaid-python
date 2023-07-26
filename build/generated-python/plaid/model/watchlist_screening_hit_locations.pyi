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


class WatchlistScreeningHitLocations(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Location information for the associated individual watchlist hit
    """


    class MetaOapg:
        required = {
            "country",
            "full",
        }
        
        class properties:
            full = schemas.StrSchema
        
            @staticmethod
            def country() -> typing.Type['GenericCountryCode']:
                return GenericCountryCode
            __annotations__ = {
                "full": full,
                "country": country,
            }
        additional_properties = schemas.AnyTypeSchema
    
    country: 'GenericCountryCode'
    full: MetaOapg.properties.full
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'GenericCountryCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full"]) -> MetaOapg.properties.full: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country"], typing_extensions.Literal["full"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> 'GenericCountryCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full"]) -> MetaOapg.properties.full: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country"], typing_extensions.Literal["full"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        country: 'GenericCountryCode',
        full: typing.Union[MetaOapg.properties.full, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WatchlistScreeningHitLocations':
        return super().__new__(
            cls,
            *_args,
            country=country,
            full=full,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.generic_country_code import GenericCountryCode
