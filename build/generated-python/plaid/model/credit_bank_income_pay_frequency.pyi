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


class CreditBankIncomePayFrequency(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The income pay frequency.
    """
    
    @schemas.classproperty
    def WEEKLY(cls):
        return cls("WEEKLY")
    
    @schemas.classproperty
    def BIWEEKLY(cls):
        return cls("BIWEEKLY")
    
    @schemas.classproperty
    def SEMI_MONTHLY(cls):
        return cls("SEMI_MONTHLY")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("MONTHLY")
    
    @schemas.classproperty
    def DAILY(cls):
        return cls("DAILY")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
