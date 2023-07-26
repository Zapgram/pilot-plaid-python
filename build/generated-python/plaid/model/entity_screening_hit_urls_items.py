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


class EntityScreeningHitUrlsItems(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Analyzed URLs for the associated hit
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def analysis() -> typing.Type['MatchSummary']:
                return MatchSummary
        
            @staticmethod
            def data() -> typing.Type['EntityScreeningHitUrls']:
                return EntityScreeningHitUrls
            __annotations__ = {
                "analysis": analysis,
                "data": data,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysis"]) -> 'MatchSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'EntityScreeningHitUrls': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analysis"], typing_extensions.Literal["data"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysis"]) -> typing.Union['MatchSummary', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['EntityScreeningHitUrls', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analysis"], typing_extensions.Literal["data"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        analysis: typing.Union['MatchSummary', schemas.Unset] = schemas.unset,
        data: typing.Union['EntityScreeningHitUrls', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'EntityScreeningHitUrlsItems':
        return super().__new__(
            cls,
            *_args,
            analysis=analysis,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.entity_screening_hit_urls import EntityScreeningHitUrls
from plaid.model.match_summary import MatchSummary
