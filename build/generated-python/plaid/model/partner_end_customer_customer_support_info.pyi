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


class PartnerEndCustomerCustomerSupportInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This information is public. Users of your app will see this information when managing connections between your app and their bank accounts in Plaid Portal. Defaults to partner's customer support info if omitted.
    """


    class MetaOapg:
        
        class properties:
            email = schemas.StrSchema
            phone_number = schemas.StrSchema
            contact_url = schemas.StrSchema
            link_update_url = schemas.StrSchema
            __annotations__ = {
                "email": email,
                "phone_number": phone_number,
                "contact_url": contact_url,
                "link_update_url": link_update_url,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_url"]) -> MetaOapg.properties.contact_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_update_url"]) -> MetaOapg.properties.link_update_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email"], typing_extensions.Literal["phone_number"], typing_extensions.Literal["contact_url"], typing_extensions.Literal["link_update_url"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_url"]) -> typing.Union[MetaOapg.properties.contact_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_update_url"]) -> typing.Union[MetaOapg.properties.link_update_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email"], typing_extensions.Literal["phone_number"], typing_extensions.Literal["contact_url"], typing_extensions.Literal["link_update_url"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
        contact_url: typing.Union[MetaOapg.properties.contact_url, str, schemas.Unset] = schemas.unset,
        link_update_url: typing.Union[MetaOapg.properties.link_update_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PartnerEndCustomerCustomerSupportInfo':
        return super().__new__(
            cls,
            *_args,
            email=email,
            phone_number=phone_number,
            contact_url=contact_url,
            link_update_url=link_update_url,
            _configuration=_configuration,
            **kwargs,
        )
