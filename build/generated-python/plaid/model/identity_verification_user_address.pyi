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


class IdentityVerificationUserAddress(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:

Addresses from the United Kingdom will not include a region

Addresses from Hong Kong will not include postal code
    """


    class MetaOapg:
        required = {
            "country",
            "city",
            "street",
            "street2",
            "postal_code",
            "region",
        }
        
        class properties:
        
            @staticmethod
            def street() -> typing.Type['StreetNullable']:
                return StreetNullable
        
            @staticmethod
            def street2() -> typing.Type['Street2']:
                return Street2
        
            @staticmethod
            def city() -> typing.Type['CityNullable']:
                return CityNullable
        
            @staticmethod
            def region() -> typing.Type['Region']:
                return Region
        
            @staticmethod
            def postal_code() -> typing.Type['PostalCode']:
                return PostalCode
        
            @staticmethod
            def country() -> typing.Type['GenericCountryCode']:
                return GenericCountryCode
            __annotations__ = {
                "street": street,
                "street2": street2,
                "city": city,
                "region": region,
                "postal_code": postal_code,
                "country": country,
            }
        additional_properties = schemas.AnyTypeSchema

    
    country: 'GenericCountryCode'
    city: 'CityNullable'
    street: 'StreetNullable'
    street2: 'Street2'
    postal_code: 'PostalCode'
    region: 'Region'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'GenericCountryCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> 'CityNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street"]) -> 'StreetNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street2"]) -> 'Street2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postal_code"]) -> 'PostalCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> 'Region': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country"], typing_extensions.Literal["city"], typing_extensions.Literal["street"], typing_extensions.Literal["street2"], typing_extensions.Literal["postal_code"], typing_extensions.Literal["region"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> 'GenericCountryCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> 'CityNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street"]) -> 'StreetNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street2"]) -> 'Street2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postal_code"]) -> 'PostalCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> 'Region': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country"], typing_extensions.Literal["city"], typing_extensions.Literal["street"], typing_extensions.Literal["street2"], typing_extensions.Literal["postal_code"], typing_extensions.Literal["region"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'IdentityVerificationUserAddress':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.city_nullable import CityNullable
from plaid.model.generic_country_code import GenericCountryCode
from plaid.model.postal_code import PostalCode
from plaid.model.region import Region
from plaid.model.street2 import Street2
from plaid.model.street_nullable import StreetNullable
