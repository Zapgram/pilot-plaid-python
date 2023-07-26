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


class TransferRecurringStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of the recurring transfer.

`active`: The recurring transfer is currently active.
`cancelled`: The recurring transfer was cancelled by the client or Plaid.
`expired`: The recurring transfer has completed all originations according to its recurring schedule.
    """


    class MetaOapg:
        enum_value_to_name = {
            "active": "ACTIVE",
            "cancelled": "CANCELLED",
            "expired": "EXPIRED",
        }
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("active")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("cancelled")
    
    @schemas.classproperty
    def EXPIRED(cls):
        return cls("expired")