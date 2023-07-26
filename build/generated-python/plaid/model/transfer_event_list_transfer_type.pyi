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


class TransferEventListTransferType(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account.
    """


    class MetaOapg:
        enum_value_to_name = {
            "debit": "DEBIT",
            "credit": "CREDIT",
            schemas.NoneClass.NONE: "NONE",
        }
    
    @schemas.classproperty
    def DEBIT(cls):
        return cls("debit")
    
    @schemas.classproperty
    def CREDIT(cls):
        return cls("credit")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransferEventListTransferType':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
