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


class AddressPurposeLabel(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Field describing whether the associated address is being used for commercial or residential purposes.

Note: This value will be `no_data` when Plaid does not have sufficient data to determine the address's use.
    """


    class MetaOapg:
        enum_value_to_name = {
            "residential": "RESIDENTIAL",
            "commercial": "COMMERCIAL",
            "no_data": "NO_DATA",
        }
    
    @schemas.classproperty
    def RESIDENTIAL(cls):
        return cls("residential")
    
    @schemas.classproperty
    def COMMERCIAL(cls):
        return cls("commercial")
    
    @schemas.classproperty
    def NO_DATA(cls):
        return cls("no_data")