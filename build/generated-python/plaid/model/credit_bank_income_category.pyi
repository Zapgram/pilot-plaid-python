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


class CreditBankIncomeCategory(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The income category. Note that the `CASH` value has been deprecated and is used only for existing legacy implementations. It has been replaced by the new categories `CASH_DEPOSIT` (representing cash or check deposits) and `TRANSFER_FROM_APPLICATION` (representing cash transfers originating from apps, such as Zelle or Venmo).
    """
    
    @schemas.classproperty
    def SALARY(cls):
        return cls("SALARY")
    
    @schemas.classproperty
    def UNEMPLOYMENT(cls):
        return cls("UNEMPLOYMENT")
    
    @schemas.classproperty
    def CASH(cls):
        return cls("CASH")
    
    @schemas.classproperty
    def GIG_ECONOMY(cls):
        return cls("GIG_ECONOMY")
    
    @schemas.classproperty
    def RENTAL(cls):
        return cls("RENTAL")
    
    @schemas.classproperty
    def CHILD_SUPPORT(cls):
        return cls("CHILD_SUPPORT")
    
    @schemas.classproperty
    def MILITARY(cls):
        return cls("MILITARY")
    
    @schemas.classproperty
    def RETIREMENT(cls):
        return cls("RETIREMENT")
    
    @schemas.classproperty
    def LONG_TERM_DISABILITY(cls):
        return cls("LONG_TERM_DISABILITY")
    
    @schemas.classproperty
    def BANK_INTEREST(cls):
        return cls("BANK_INTEREST")
    
    @schemas.classproperty
    def CASH_DEPOSIT(cls):
        return cls("CASH_DEPOSIT")
    
    @schemas.classproperty
    def TRANSFER_FROM_APPLICATION(cls):
        return cls("TRANSFER_FROM_APPLICATION")
    
    @schemas.classproperty
    def TAX_REFUND(cls):
        return cls("TAX_REFUND")
    
    @schemas.classproperty
    def BENEFIT_OTHER(cls):
        return cls("BENEFIT_OTHER")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("OTHER")
