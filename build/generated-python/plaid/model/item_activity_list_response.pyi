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


class ItemActivityListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Describes a historical log of user consent events.
    """


    class MetaOapg:
        required = {
            "activities",
            "last_data_access_times",
            "request_id",
        }
        
        class properties:
            request_id = schemas.StrSchema
            
            
            class activities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Activity']:
                        return Activity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Activity'], typing.List['Activity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'activities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Activity':
                    return super().__getitem__(i)
            
            
            class last_data_access_times(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LastDataAccessTimes']:
                        return LastDataAccessTimes
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['LastDataAccessTimes'], typing.List['LastDataAccessTimes']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'last_data_access_times':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LastDataAccessTimes':
                    return super().__getitem__(i)
            cursor = schemas.StrSchema
            __annotations__ = {
                "request_id": request_id,
                "activities": activities,
                "last_data_access_times": last_data_access_times,
                "cursor": cursor,
            }
        additional_properties = schemas.AnyTypeSchema
    
    activities: MetaOapg.properties.activities
    last_data_access_times: MetaOapg.properties.last_data_access_times
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activities"]) -> MetaOapg.properties.activities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_data_access_times"]) -> MetaOapg.properties.last_data_access_times: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activities"], typing_extensions.Literal["last_data_access_times"], typing_extensions.Literal["request_id"], typing_extensions.Literal["cursor"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activities"]) -> MetaOapg.properties.activities: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_data_access_times"]) -> MetaOapg.properties.last_data_access_times: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cursor"]) -> typing.Union[MetaOapg.properties.cursor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activities"], typing_extensions.Literal["last_data_access_times"], typing_extensions.Literal["request_id"], typing_extensions.Literal["cursor"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        activities: typing.Union[MetaOapg.properties.activities, list, tuple, ],
        last_data_access_times: typing.Union[MetaOapg.properties.last_data_access_times, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        cursor: typing.Union[MetaOapg.properties.cursor, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ItemActivityListResponse':
        return super().__new__(
            cls,
            *_args,
            activities=activities,
            last_data_access_times=last_data_access_times,
            request_id=request_id,
            cursor=cursor,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.activity import Activity
from plaid.model.last_data_access_times import LastDataAccessTimes