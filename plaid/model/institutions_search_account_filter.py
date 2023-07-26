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


class InstitutionsSearchAccountFilter(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An account filter to apply to institutions search requests
    """


    class MetaOapg:
        
        class properties:
            
            
            class loan(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccountSubtype']:
                        return AccountSubtype
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AccountSubtype'], typing.List['AccountSubtype']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loan':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccountSubtype':
                    return super().__getitem__(i)
            
            
            class depository(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccountSubtype']:
                        return AccountSubtype
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AccountSubtype'], typing.List['AccountSubtype']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'depository':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccountSubtype':
                    return super().__getitem__(i)
            
            
            class credit(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccountSubtype']:
                        return AccountSubtype
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AccountSubtype'], typing.List['AccountSubtype']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'credit':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccountSubtype':
                    return super().__getitem__(i)
            
            
            class investment(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccountSubtype']:
                        return AccountSubtype
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AccountSubtype'], typing.List['AccountSubtype']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'investment':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccountSubtype':
                    return super().__getitem__(i)
            __annotations__ = {
                "loan": loan,
                "depository": depository,
                "credit": credit,
                "investment": investment,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loan"]) -> MetaOapg.properties.loan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depository"]) -> MetaOapg.properties.depository: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credit"]) -> MetaOapg.properties.credit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investment"]) -> MetaOapg.properties.investment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["loan"], typing_extensions.Literal["depository"], typing_extensions.Literal["credit"], typing_extensions.Literal["investment"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loan"]) -> typing.Union[MetaOapg.properties.loan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depository"]) -> typing.Union[MetaOapg.properties.depository, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credit"]) -> typing.Union[MetaOapg.properties.credit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investment"]) -> typing.Union[MetaOapg.properties.investment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["loan"], typing_extensions.Literal["depository"], typing_extensions.Literal["credit"], typing_extensions.Literal["investment"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        loan: typing.Union[MetaOapg.properties.loan, list, tuple, schemas.Unset] = schemas.unset,
        depository: typing.Union[MetaOapg.properties.depository, list, tuple, schemas.Unset] = schemas.unset,
        credit: typing.Union[MetaOapg.properties.credit, list, tuple, schemas.Unset] = schemas.unset,
        investment: typing.Union[MetaOapg.properties.investment, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'InstitutionsSearchAccountFilter':
        return super().__new__(
            cls,
            *_args,
            loan=loan,
            depository=depository,
            credit=credit,
            investment=investment,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.account_subtype import AccountSubtype