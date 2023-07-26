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


class FDXPartyType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Identifies the type of a party
    """


    class MetaOapg:
        enum_value_to_name = {
            "DATA_ACCESS_PLATFORM": "DATA_ACCESS_PLATFORM",
            "DATA_PROVIDER": "DATA_PROVIDER",
            "DATA_RECIPIENT": "DATA_RECIPIENT",
            "INDIVIDUAL": "INDIVIDUAL",
            "MERCHANT": "MERCHANT",
            "VENDOR": "VENDOR",
        }
    
    @schemas.classproperty
    def DATA_ACCESS_PLATFORM(cls):
        return cls("DATA_ACCESS_PLATFORM")
    
    @schemas.classproperty
    def DATA_PROVIDER(cls):
        return cls("DATA_PROVIDER")
    
    @schemas.classproperty
    def DATA_RECIPIENT(cls):
        return cls("DATA_RECIPIENT")
    
    @schemas.classproperty
    def INDIVIDUAL(cls):
        return cls("INDIVIDUAL")
    
    @schemas.classproperty
    def MERCHANT(cls):
        return cls("MERCHANT")
    
    @schemas.classproperty
    def VENDOR(cls):
        return cls("VENDOR")
