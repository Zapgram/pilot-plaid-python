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


class LinkTokenGetMetadataResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object specifying the arguments originally provided to the `/link/token/create` call.
    """


    class MetaOapg:
        required = {
            "webhook",
            "country_codes",
            "language",
            "redirect_uri",
            "initial_products",
            "client_name",
        }
        
        class properties:
            
            
            class initial_products(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Products']:
                        return Products
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Products'], typing.List['Products']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'initial_products':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Products':
                    return super().__getitem__(i)
            
            
            class webhook(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'webhook':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class country_codes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CountryCode']:
                        return CountryCode
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CountryCode'], typing.List['CountryCode']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country_codes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CountryCode':
                    return super().__getitem__(i)
            
            
            class language(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'language':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class redirect_uri(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'redirect_uri':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class client_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'client_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def institution_data() -> typing.Type['LinkTokenCreateInstitutionData']:
                return LinkTokenCreateInstitutionData
        
            @staticmethod
            def account_filters() -> typing.Type['AccountFiltersResponse']:
                return AccountFiltersResponse
            __annotations__ = {
                "initial_products": initial_products,
                "webhook": webhook,
                "country_codes": country_codes,
                "language": language,
                "redirect_uri": redirect_uri,
                "client_name": client_name,
                "institution_data": institution_data,
                "account_filters": account_filters,
            }
        additional_properties = schemas.AnyTypeSchema
    
    webhook: MetaOapg.properties.webhook
    country_codes: MetaOapg.properties.country_codes
    language: MetaOapg.properties.language
    redirect_uri: MetaOapg.properties.redirect_uri
    initial_products: MetaOapg.properties.initial_products
    client_name: MetaOapg.properties.client_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> MetaOapg.properties.webhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_codes"]) -> MetaOapg.properties.country_codes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initial_products"]) -> MetaOapg.properties.initial_products: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_name"]) -> MetaOapg.properties.client_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution_data"]) -> 'LinkTokenCreateInstitutionData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_filters"]) -> 'AccountFiltersResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["webhook"], typing_extensions.Literal["country_codes"], typing_extensions.Literal["language"], typing_extensions.Literal["redirect_uri"], typing_extensions.Literal["initial_products"], typing_extensions.Literal["client_name"], typing_extensions.Literal["institution_data"], typing_extensions.Literal["account_filters"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> MetaOapg.properties.webhook: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_codes"]) -> MetaOapg.properties.country_codes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initial_products"]) -> MetaOapg.properties.initial_products: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_name"]) -> MetaOapg.properties.client_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution_data"]) -> typing.Union['LinkTokenCreateInstitutionData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_filters"]) -> typing.Union['AccountFiltersResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["webhook"], typing_extensions.Literal["country_codes"], typing_extensions.Literal["language"], typing_extensions.Literal["redirect_uri"], typing_extensions.Literal["initial_products"], typing_extensions.Literal["client_name"], typing_extensions.Literal["institution_data"], typing_extensions.Literal["account_filters"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        webhook: typing.Union[MetaOapg.properties.webhook, None, str, ],
        country_codes: typing.Union[MetaOapg.properties.country_codes, list, tuple, ],
        language: typing.Union[MetaOapg.properties.language, None, str, ],
        redirect_uri: typing.Union[MetaOapg.properties.redirect_uri, None, str, ],
        initial_products: typing.Union[MetaOapg.properties.initial_products, list, tuple, ],
        client_name: typing.Union[MetaOapg.properties.client_name, None, str, ],
        institution_data: typing.Union['LinkTokenCreateInstitutionData', schemas.Unset] = schemas.unset,
        account_filters: typing.Union['AccountFiltersResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'LinkTokenGetMetadataResponse':
        return super().__new__(
            cls,
            *_args,
            webhook=webhook,
            country_codes=country_codes,
            language=language,
            redirect_uri=redirect_uri,
            initial_products=initial_products,
            client_name=client_name,
            institution_data=institution_data,
            account_filters=account_filters,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.account_filters_response import AccountFiltersResponse
from plaid.model.country_code import CountryCode
from plaid.model.link_token_create_institution_data import LinkTokenCreateInstitutionData
from plaid.model.products import Products