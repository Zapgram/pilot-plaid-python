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


class LiabilitiesObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object containing liability accounts
    """


    class MetaOapg:
        required = {
            "mortgage",
            "student",
            "credit",
        }
        
        class properties:
            
            
            class credit(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CreditCardLiability']:
                        return CreditCardLiability
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'credit':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class mortgage(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MortgageLiability']:
                        return MortgageLiability
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mortgage':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class student(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StudentLoan']:
                        return StudentLoan
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'student':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "credit": credit,
                "mortgage": mortgage,
                "student": student,
            }
        additional_properties = schemas.AnyTypeSchema
    
    mortgage: MetaOapg.properties.mortgage
    student: MetaOapg.properties.student
    credit: MetaOapg.properties.credit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mortgage"]) -> MetaOapg.properties.mortgage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["student"]) -> MetaOapg.properties.student: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credit"]) -> MetaOapg.properties.credit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mortgage"], typing_extensions.Literal["student"], typing_extensions.Literal["credit"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mortgage"]) -> MetaOapg.properties.mortgage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["student"]) -> MetaOapg.properties.student: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credit"]) -> MetaOapg.properties.credit: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mortgage"], typing_extensions.Literal["student"], typing_extensions.Literal["credit"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mortgage: typing.Union[MetaOapg.properties.mortgage, list, tuple, None, ],
        student: typing.Union[MetaOapg.properties.student, list, tuple, None, ],
        credit: typing.Union[MetaOapg.properties.credit, list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'LiabilitiesObject':
        return super().__new__(
            cls,
            *_args,
            mortgage=mortgage,
            student=student,
            credit=credit,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.credit_card_liability import CreditCardLiability
from plaid.model.mortgage_liability import MortgageLiability
from plaid.model.student_loan import StudentLoan
