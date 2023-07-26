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


class BankTransferStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of the transfer.
    """


    class MetaOapg:
        enum_value_to_name = {
            "pending": "PENDING",
            "posted": "POSTED",
            "cancelled": "CANCELLED",
            "failed": "FAILED",
            "reversed": "REVERSED",
        }
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending")
    
    @schemas.classproperty
    def POSTED(cls):
        return cls("posted")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("cancelled")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("failed")
    
    @schemas.classproperty
    def REVERSED(cls):
        return cls("reversed")
