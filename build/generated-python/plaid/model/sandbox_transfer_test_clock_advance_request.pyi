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


class SandboxTransferTestClockAdvanceRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Defines the request schema for `/sandbox/transfer/test_clock/advance`
    """


    class MetaOapg:
        required = {
            "test_clock_id",
            "new_virtual_time",
        }
        
        class properties:
            test_clock_id = schemas.StrSchema
            new_virtual_time = schemas.DateTimeSchema
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
            __annotations__ = {
                "test_clock_id": test_clock_id,
                "new_virtual_time": new_virtual_time,
                "client_id": client_id,
                "secret": secret,
            }
    
    test_clock_id: MetaOapg.properties.test_clock_id
    new_virtual_time: MetaOapg.properties.new_virtual_time
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["test_clock_id"]) -> MetaOapg.properties.test_clock_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_virtual_time"]) -> MetaOapg.properties.new_virtual_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["test_clock_id", "new_virtual_time", "client_id", "secret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["test_clock_id"]) -> MetaOapg.properties.test_clock_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_virtual_time"]) -> MetaOapg.properties.new_virtual_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["test_clock_id", "new_virtual_time", "client_id", "secret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        test_clock_id: typing.Union[MetaOapg.properties.test_clock_id, str, ],
        new_virtual_time: typing.Union[MetaOapg.properties.new_virtual_time, str, datetime, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SandboxTransferTestClockAdvanceRequest':
        return super().__new__(
            cls,
            *_args,
            test_clock_id=test_clock_id,
            new_virtual_time=new_virtual_time,
            client_id=client_id,
            secret=secret,
            _configuration=_configuration,
            **kwargs,
        )
