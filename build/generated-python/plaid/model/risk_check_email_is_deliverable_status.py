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


class RiskCheckEmailIsDeliverableStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    SMTP-MX check to confirm the email address exists if known.
    """


    class MetaOapg:
        enum_value_to_name = {
            "yes": "YES",
            "no": "NO",
            "no_data": "NO_DATA",
        }
    
    @schemas.classproperty
    def YES(cls):
        return cls("yes")
    
    @schemas.classproperty
    def NO(cls):
        return cls("no")
    
    @schemas.classproperty
    def NO_DATA(cls):
        return cls("no_data")
