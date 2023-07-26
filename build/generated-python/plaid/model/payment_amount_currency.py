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


class PaymentAmountCurrency(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The ISO-4217 currency code of the payment. For standing orders and payment consents, `"GBP"` must be used. For Poland, Denmark, Sweden and Norway, only the local currency is currently supported.
    """


    class MetaOapg:
        max_length = 3
        min_length = 3
        enum_value_to_name = {
            "GBP": "GBP",
            "EUR": "EUR",
            "PLN": "PLN",
            "SEK": "SEK",
            "DKK": "DKK",
            "NOK": "NOK",
        }
    
    @schemas.classproperty
    def GBP(cls):
        return cls("GBP")
    
    @schemas.classproperty
    def EUR(cls):
        return cls("EUR")
    
    @schemas.classproperty
    def PLN(cls):
        return cls("PLN")
    
    @schemas.classproperty
    def SEK(cls):
        return cls("SEK")
    
    @schemas.classproperty
    def DKK(cls):
        return cls("DKK")
    
    @schemas.classproperty
    def NOK(cls):
        return cls("NOK")
