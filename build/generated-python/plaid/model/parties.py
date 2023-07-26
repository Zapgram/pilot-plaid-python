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


class Parties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A collection of objects that define specific parties to a deal. This includes the direct participating parties, such as borrower and seller and the indirect parties such as the credit report provider.
    """


    class MetaOapg:
        required = {
            "PARTY",
        }
        
        class properties:
            
            
            class PARTY(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Party']:
                        return Party
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Party'], typing.List['Party']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PARTY':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Party':
                    return super().__getitem__(i)
            __annotations__ = {
                "PARTY": PARTY,
            }
        additional_properties = schemas.AnyTypeSchema
    
    PARTY: MetaOapg.properties.PARTY
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PARTY"]) -> MetaOapg.properties.PARTY: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["PARTY"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PARTY"]) -> MetaOapg.properties.PARTY: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["PARTY"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        PARTY: typing.Union[MetaOapg.properties.PARTY, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'Parties':
        return super().__new__(
            cls,
            *_args,
            PARTY=PARTY,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.party import Party
