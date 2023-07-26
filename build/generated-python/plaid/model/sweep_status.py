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


class SweepStatus(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of a sweep transfer

`"pending"` - The sweep is currently pending
`"posted"` - The sweep has been posted
`"settled"` - The sweep has settled
`"returned"` - The sweep has been returned
`"failed"` - The sweep has failed
    """


    class MetaOapg:
        enum_value_to_name = {
            "pending": "PENDING",
            "posted": "POSTED",
            "settled": "SETTLED",
            "returned": "RETURNED",
            "failed": "FAILED",
            schemas.NoneClass.NONE: "NONE",
        }
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending")
    
    @schemas.classproperty
    def POSTED(cls):
        return cls("posted")
    
    @schemas.classproperty
    def SETTLED(cls):
        return cls("settled")
    
    @schemas.classproperty
    def RETURNED(cls):
        return cls("returned")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("failed")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SweepStatus':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
