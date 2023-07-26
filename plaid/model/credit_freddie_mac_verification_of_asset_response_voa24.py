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


class CreditFreddieMacVerificationOfAssetResponseVOA24(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """


    class MetaOapg:
        required = {
            "ASSETS",
        }
        
        class properties:
        
            @staticmethod
            def ASSETS() -> typing.Type['CreditFreddieMacAssetsVOA24']:
                return CreditFreddieMacAssetsVOA24
            __annotations__ = {
                "ASSETS": ASSETS,
            }
        additional_properties = schemas.AnyTypeSchema
    
    ASSETS: 'CreditFreddieMacAssetsVOA24'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ASSETS"]) -> 'CreditFreddieMacAssetsVOA24': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ASSETS"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ASSETS"]) -> 'CreditFreddieMacAssetsVOA24': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ASSETS"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ASSETS: 'CreditFreddieMacAssetsVOA24',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreditFreddieMacVerificationOfAssetResponseVOA24':
        return super().__new__(
            cls,
            *_args,
            ASSETS=ASSETS,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.credit_freddie_mac_assets_voa24 import CreditFreddieMacAssetsVOA24