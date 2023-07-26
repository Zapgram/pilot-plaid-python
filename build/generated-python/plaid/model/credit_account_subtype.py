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


class CreditAccountSubtype(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Valid account subtypes for credit accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-credit).
    """


    class MetaOapg:
        enum_value_to_name = {
            "credit card": "CREDIT_CARD",
            "paypal": "PAYPAL",
            "all": "ALL",
        }
    
    @schemas.classproperty
    def CREDIT_CARD(cls):
        return cls("credit card")
    
    @schemas.classproperty
    def PAYPAL(cls):
        return cls("paypal")
    
    @schemas.classproperty
    def ALL(cls):
        return cls("all")
