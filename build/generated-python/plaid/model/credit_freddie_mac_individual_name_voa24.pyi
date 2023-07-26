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


class CreditFreddieMacIndividualNameVOA24(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """


    class MetaOapg:
        required = {
            "FirstName",
            "LastName",
            "MiddleName",
        }
        
        class properties:
            FirstName = schemas.StrSchema
            LastName = schemas.StrSchema
            MiddleName = schemas.StrSchema
            __annotations__ = {
                "FirstName": FirstName,
                "LastName": LastName,
                "MiddleName": MiddleName,
            }
        additional_properties = schemas.AnyTypeSchema
    
    FirstName: MetaOapg.properties.FirstName
    LastName: MetaOapg.properties.LastName
    MiddleName: MetaOapg.properties.MiddleName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MiddleName"]) -> MetaOapg.properties.MiddleName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FirstName"], typing_extensions.Literal["LastName"], typing_extensions.Literal["MiddleName"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MiddleName"]) -> MetaOapg.properties.MiddleName: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FirstName"], typing_extensions.Literal["LastName"], typing_extensions.Literal["MiddleName"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        FirstName: typing.Union[MetaOapg.properties.FirstName, str, ],
        LastName: typing.Union[MetaOapg.properties.LastName, str, ],
        MiddleName: typing.Union[MetaOapg.properties.MiddleName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreditFreddieMacIndividualNameVOA24':
        return super().__new__(
            cls,
            *_args,
            FirstName=FirstName,
            LastName=LastName,
            MiddleName=MiddleName,
            _configuration=_configuration,
            **kwargs,
        )