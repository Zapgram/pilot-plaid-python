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


class InstitutionsGetRequestOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An optional object to filter `/institutions/get` results.
    """


    class MetaOapg:
        
        class properties:
            
            
            class products(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Products']:
                        return Products
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'products':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class routing_numbers(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'routing_numbers':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class oauth(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'oauth':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            include_optional_metadata = schemas.BoolSchema
            include_auth_metadata = schemas.BoolSchema
            include_payment_initiation_metadata = schemas.BoolSchema
            __annotations__ = {
                "products": products,
                "routing_numbers": routing_numbers,
                "oauth": oauth,
                "include_optional_metadata": include_optional_metadata,
                "include_auth_metadata": include_auth_metadata,
                "include_payment_initiation_metadata": include_payment_initiation_metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["products"]) -> MetaOapg.properties.products: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routing_numbers"]) -> MetaOapg.properties.routing_numbers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oauth"]) -> MetaOapg.properties.oauth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_optional_metadata"]) -> MetaOapg.properties.include_optional_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_auth_metadata"]) -> MetaOapg.properties.include_auth_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_payment_initiation_metadata"]) -> MetaOapg.properties.include_payment_initiation_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["products", "routing_numbers", "oauth", "include_optional_metadata", "include_auth_metadata", "include_payment_initiation_metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["products"]) -> typing.Union[MetaOapg.properties.products, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routing_numbers"]) -> typing.Union[MetaOapg.properties.routing_numbers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oauth"]) -> typing.Union[MetaOapg.properties.oauth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_optional_metadata"]) -> typing.Union[MetaOapg.properties.include_optional_metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_auth_metadata"]) -> typing.Union[MetaOapg.properties.include_auth_metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_payment_initiation_metadata"]) -> typing.Union[MetaOapg.properties.include_payment_initiation_metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["products", "routing_numbers", "oauth", "include_optional_metadata", "include_auth_metadata", "include_payment_initiation_metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        products: typing.Union[MetaOapg.properties.products, list, tuple, None, schemas.Unset] = schemas.unset,
        routing_numbers: typing.Union[MetaOapg.properties.routing_numbers, list, tuple, None, schemas.Unset] = schemas.unset,
        oauth: typing.Union[MetaOapg.properties.oauth, None, bool, schemas.Unset] = schemas.unset,
        include_optional_metadata: typing.Union[MetaOapg.properties.include_optional_metadata, bool, schemas.Unset] = schemas.unset,
        include_auth_metadata: typing.Union[MetaOapg.properties.include_auth_metadata, bool, schemas.Unset] = schemas.unset,
        include_payment_initiation_metadata: typing.Union[MetaOapg.properties.include_payment_initiation_metadata, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstitutionsGetRequestOptions':
        return super().__new__(
            cls,
            *_args,
            products=products,
            routing_numbers=routing_numbers,
            oauth=oauth,
            include_optional_metadata=include_optional_metadata,
            include_auth_metadata=include_auth_metadata,
            include_payment_initiation_metadata=include_payment_initiation_metadata,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.products import Products
