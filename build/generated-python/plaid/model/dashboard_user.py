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


class DashboardUser(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Account information associated with a team member with access to the Plaid dashboard.
    """


    class MetaOapg:
        required = {
            "email_address",
            "created_at",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            email_address = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['DashboardUserStatus']:
                return DashboardUserStatus
            __annotations__ = {
                "id": id,
                "created_at": created_at,
                "email_address": email_address,
                "status": status,
            }
        additional_properties = schemas.AnyTypeSchema
    
    email_address: MetaOapg.properties.email_address
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    status: 'DashboardUserStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> MetaOapg.properties.email_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'DashboardUserStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_address"], typing_extensions.Literal["created_at"], typing_extensions.Literal["id"], typing_extensions.Literal["status"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> MetaOapg.properties.email_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'DashboardUserStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_address"], typing_extensions.Literal["created_at"], typing_extensions.Literal["id"], typing_extensions.Literal["status"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        email_address: typing.Union[MetaOapg.properties.email_address, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: 'DashboardUserStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'DashboardUser':
        return super().__new__(
            cls,
            *_args,
            email_address=email_address,
            created_at=created_at,
            id=id,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.dashboard_user_status import DashboardUserStatus
