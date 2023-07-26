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


class AuthGetNumbers(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object containing identifying numbers used for making electronic transfers to and from the `accounts`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any `accounts` for which data has been requested, the array for that type will be empty.
    """


    class MetaOapg:
        required = {
            "bacs",
            "eft",
            "ach",
            "international",
        }
        
        class properties:
            
            
            class ach(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NumbersACH']:
                        return NumbersACH
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NumbersACH'], typing.List['NumbersACH']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ach':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NumbersACH':
                    return super().__getitem__(i)
            
            
            class eft(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NumbersEFT']:
                        return NumbersEFT
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NumbersEFT'], typing.List['NumbersEFT']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'eft':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NumbersEFT':
                    return super().__getitem__(i)
            
            
            class international(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NumbersInternational']:
                        return NumbersInternational
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NumbersInternational'], typing.List['NumbersInternational']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'international':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NumbersInternational':
                    return super().__getitem__(i)
            
            
            class bacs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NumbersBACS']:
                        return NumbersBACS
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NumbersBACS'], typing.List['NumbersBACS']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bacs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NumbersBACS':
                    return super().__getitem__(i)
            __annotations__ = {
                "ach": ach,
                "eft": eft,
                "international": international,
                "bacs": bacs,
            }
        additional_properties = schemas.AnyTypeSchema
    
    bacs: MetaOapg.properties.bacs
    eft: MetaOapg.properties.eft
    ach: MetaOapg.properties.ach
    international: MetaOapg.properties.international
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bacs"]) -> MetaOapg.properties.bacs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eft"]) -> MetaOapg.properties.eft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach"]) -> MetaOapg.properties.ach: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["international"]) -> MetaOapg.properties.international: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bacs"], typing_extensions.Literal["eft"], typing_extensions.Literal["ach"], typing_extensions.Literal["international"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bacs"]) -> MetaOapg.properties.bacs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eft"]) -> MetaOapg.properties.eft: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach"]) -> MetaOapg.properties.ach: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["international"]) -> MetaOapg.properties.international: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bacs"], typing_extensions.Literal["eft"], typing_extensions.Literal["ach"], typing_extensions.Literal["international"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bacs: typing.Union[MetaOapg.properties.bacs, list, tuple, ],
        eft: typing.Union[MetaOapg.properties.eft, list, tuple, ],
        ach: typing.Union[MetaOapg.properties.ach, list, tuple, ],
        international: typing.Union[MetaOapg.properties.international, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'AuthGetNumbers':
        return super().__new__(
            cls,
            *_args,
            bacs=bacs,
            eft=eft,
            ach=ach,
            international=international,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.numbers_ach import NumbersACH
from plaid.model.numbers_bacs import NumbersBACS
from plaid.model.numbers_eft import NumbersEFT
from plaid.model.numbers_international import NumbersInternational
