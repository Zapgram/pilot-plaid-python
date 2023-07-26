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


class StudentRepaymentPlan(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object representing the repayment plan for the student loan
    """


    class MetaOapg:
        required = {
            "description",
            "type",
        }
        
        class properties:
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "extended graduated": "EXTENDED_GRADUATED",
                        "extended standard": "EXTENDED_STANDARD",
                        "graduated": "GRADUATED",
                        "income-contingent repayment": "INCOMECONTINGENT_REPAYMENT",
                        "income-based repayment": "INCOMEBASED_REPAYMENT",
                        "interest-only": "INTERESTONLY",
                        "other": "OTHER",
                        "pay as you earn": "PAY_AS_YOU_EARN",
                        "revised pay as you earn": "REVISED_PAY_AS_YOU_EARN",
                        "standard": "STANDARD",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def EXTENDED_GRADUATED(cls):
                    return cls("extended graduated")
                
                @schemas.classproperty
                def EXTENDED_STANDARD(cls):
                    return cls("extended standard")
                
                @schemas.classproperty
                def GRADUATED(cls):
                    return cls("graduated")
                
                @schemas.classproperty
                def INCOMECONTINGENT_REPAYMENT(cls):
                    return cls("income-contingent repayment")
                
                @schemas.classproperty
                def INCOMEBASED_REPAYMENT(cls):
                    return cls("income-based repayment")
                
                @schemas.classproperty
                def INTERESTONLY(cls):
                    return cls("interest-only")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
                
                @schemas.classproperty
                def PAY_AS_YOU_EARN(cls):
                    return cls("pay as you earn")
                
                @schemas.classproperty
                def REVISED_PAY_AS_YOU_EARN(cls):
                    return cls("revised pay as you earn")
                
                @schemas.classproperty
                def STANDARD(cls):
                    return cls("standard")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "description": description,
                "type": type,
            }
        additional_properties = schemas.AnyTypeSchema
    
    description: MetaOapg.properties.description
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description"], typing_extensions.Literal["type"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description"], typing_extensions.Literal["type"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, None, str, ],
        type: typing.Union[MetaOapg.properties.type, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'StudentRepaymentPlan':
        return super().__new__(
            cls,
            *_args,
            description=description,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )