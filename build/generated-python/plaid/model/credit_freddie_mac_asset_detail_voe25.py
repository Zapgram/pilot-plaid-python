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


class CreditFreddieMacAssetDetailVOE25(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details about an asset.
    """


    class MetaOapg:
        required = {
            "AssetDaysRequestedCount",
            "AssetOwnershipType",
            "AssetType",
            "AssetAccountIdentifier",
            "AssetDescription",
            "AssetAsOfDate",
            "AssetUniqueIdentifier",
            "AssetTypeAdditionalDescription",
        }
        
        class properties:
            AssetUniqueIdentifier = schemas.StrSchema
            AssetAccountIdentifier = schemas.StrSchema
            AssetAsOfDate = schemas.StrSchema
            
            
            class AssetDescription(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AssetDescription':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def AssetType() -> typing.Type['AssetType']:
                return AssetType
            
            
            class AssetTypeAdditionalDescription(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AssetTypeAdditionalDescription':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            AssetDaysRequestedCount = schemas.IntSchema
            
            
            class AssetOwnershipType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AssetOwnershipType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "AssetUniqueIdentifier": AssetUniqueIdentifier,
                "AssetAccountIdentifier": AssetAccountIdentifier,
                "AssetAsOfDate": AssetAsOfDate,
                "AssetDescription": AssetDescription,
                "AssetType": AssetType,
                "AssetTypeAdditionalDescription": AssetTypeAdditionalDescription,
                "AssetDaysRequestedCount": AssetDaysRequestedCount,
                "AssetOwnershipType": AssetOwnershipType,
            }
        additional_properties = schemas.AnyTypeSchema
    
    AssetDaysRequestedCount: MetaOapg.properties.AssetDaysRequestedCount
    AssetOwnershipType: MetaOapg.properties.AssetOwnershipType
    AssetType: 'AssetType'
    AssetAccountIdentifier: MetaOapg.properties.AssetAccountIdentifier
    AssetDescription: MetaOapg.properties.AssetDescription
    AssetAsOfDate: MetaOapg.properties.AssetAsOfDate
    AssetUniqueIdentifier: MetaOapg.properties.AssetUniqueIdentifier
    AssetTypeAdditionalDescription: MetaOapg.properties.AssetTypeAdditionalDescription
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetDaysRequestedCount"]) -> MetaOapg.properties.AssetDaysRequestedCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetOwnershipType"]) -> MetaOapg.properties.AssetOwnershipType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetType"]) -> 'AssetType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetAccountIdentifier"]) -> MetaOapg.properties.AssetAccountIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetDescription"]) -> MetaOapg.properties.AssetDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetAsOfDate"]) -> MetaOapg.properties.AssetAsOfDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetUniqueIdentifier"]) -> MetaOapg.properties.AssetUniqueIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssetTypeAdditionalDescription"]) -> MetaOapg.properties.AssetTypeAdditionalDescription: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AssetDaysRequestedCount"], typing_extensions.Literal["AssetOwnershipType"], typing_extensions.Literal["AssetType"], typing_extensions.Literal["AssetAccountIdentifier"], typing_extensions.Literal["AssetDescription"], typing_extensions.Literal["AssetAsOfDate"], typing_extensions.Literal["AssetUniqueIdentifier"], typing_extensions.Literal["AssetTypeAdditionalDescription"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetDaysRequestedCount"]) -> MetaOapg.properties.AssetDaysRequestedCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetOwnershipType"]) -> MetaOapg.properties.AssetOwnershipType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetType"]) -> 'AssetType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetAccountIdentifier"]) -> MetaOapg.properties.AssetAccountIdentifier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetDescription"]) -> MetaOapg.properties.AssetDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetAsOfDate"]) -> MetaOapg.properties.AssetAsOfDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetUniqueIdentifier"]) -> MetaOapg.properties.AssetUniqueIdentifier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssetTypeAdditionalDescription"]) -> MetaOapg.properties.AssetTypeAdditionalDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AssetDaysRequestedCount"], typing_extensions.Literal["AssetOwnershipType"], typing_extensions.Literal["AssetType"], typing_extensions.Literal["AssetAccountIdentifier"], typing_extensions.Literal["AssetDescription"], typing_extensions.Literal["AssetAsOfDate"], typing_extensions.Literal["AssetUniqueIdentifier"], typing_extensions.Literal["AssetTypeAdditionalDescription"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        AssetDaysRequestedCount: typing.Union[MetaOapg.properties.AssetDaysRequestedCount, decimal.Decimal, int, ],
        AssetOwnershipType: typing.Union[MetaOapg.properties.AssetOwnershipType, None, str, ],
        AssetType: 'AssetType',
        AssetAccountIdentifier: typing.Union[MetaOapg.properties.AssetAccountIdentifier, str, ],
        AssetDescription: typing.Union[MetaOapg.properties.AssetDescription, None, str, ],
        AssetAsOfDate: typing.Union[MetaOapg.properties.AssetAsOfDate, str, ],
        AssetUniqueIdentifier: typing.Union[MetaOapg.properties.AssetUniqueIdentifier, str, ],
        AssetTypeAdditionalDescription: typing.Union[MetaOapg.properties.AssetTypeAdditionalDescription, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreditFreddieMacAssetDetailVOE25':
        return super().__new__(
            cls,
            *_args,
            AssetDaysRequestedCount=AssetDaysRequestedCount,
            AssetOwnershipType=AssetOwnershipType,
            AssetType=AssetType,
            AssetAccountIdentifier=AssetAccountIdentifier,
            AssetDescription=AssetDescription,
            AssetAsOfDate=AssetAsOfDate,
            AssetUniqueIdentifier=AssetUniqueIdentifier,
            AssetTypeAdditionalDescription=AssetTypeAdditionalDescription,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.asset_type import AssetType
