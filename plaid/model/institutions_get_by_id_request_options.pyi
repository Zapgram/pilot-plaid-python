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


class InstitutionsGetByIdRequestOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies optional parameters for `/institutions/get_by_id`. If provided, must not be `null`.
    """


    class MetaOapg:
        
        class properties:
            include_optional_metadata = schemas.BoolSchema
            include_status = schemas.BoolSchema
            include_auth_metadata = schemas.BoolSchema
            include_payment_initiation_metadata = schemas.BoolSchema
            __annotations__ = {
                "include_optional_metadata": include_optional_metadata,
                "include_status": include_status,
                "include_auth_metadata": include_auth_metadata,
                "include_payment_initiation_metadata": include_payment_initiation_metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_optional_metadata"]) -> MetaOapg.properties.include_optional_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_status"]) -> MetaOapg.properties.include_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_auth_metadata"]) -> MetaOapg.properties.include_auth_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_payment_initiation_metadata"]) -> MetaOapg.properties.include_payment_initiation_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["include_optional_metadata", "include_status", "include_auth_metadata", "include_payment_initiation_metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_optional_metadata"]) -> typing.Union[MetaOapg.properties.include_optional_metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_status"]) -> typing.Union[MetaOapg.properties.include_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_auth_metadata"]) -> typing.Union[MetaOapg.properties.include_auth_metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_payment_initiation_metadata"]) -> typing.Union[MetaOapg.properties.include_payment_initiation_metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["include_optional_metadata", "include_status", "include_auth_metadata", "include_payment_initiation_metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        include_optional_metadata: typing.Union[MetaOapg.properties.include_optional_metadata, bool, schemas.Unset] = schemas.unset,
        include_status: typing.Union[MetaOapg.properties.include_status, bool, schemas.Unset] = schemas.unset,
        include_auth_metadata: typing.Union[MetaOapg.properties.include_auth_metadata, bool, schemas.Unset] = schemas.unset,
        include_payment_initiation_metadata: typing.Union[MetaOapg.properties.include_payment_initiation_metadata, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstitutionsGetByIdRequestOptions':
        return super().__new__(
            cls,
            *_args,
            include_optional_metadata=include_optional_metadata,
            include_status=include_status,
            include_auth_metadata=include_auth_metadata,
            include_payment_initiation_metadata=include_payment_initiation_metadata,
            _configuration=_configuration,
            **kwargs,
        )