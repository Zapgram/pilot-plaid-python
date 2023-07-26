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


class CreditBankIncomeErrorType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A broad categorization of the error. Safe for programmatic use.
    """
    
    @schemas.classproperty
    def INTERNAL_SERVER_ERROR(cls):
        return cls("INTERNAL_SERVER_ERROR")
    
    @schemas.classproperty
    def INSUFFICIENT_CREDENTIALS(cls):
        return cls("INSUFFICIENT_CREDENTIALS")
    
    @schemas.classproperty
    def ITEM_LOCKED(cls):
        return cls("ITEM_LOCKED")
    
    @schemas.classproperty
    def USER_SETUP_REQUIRED(cls):
        return cls("USER_SETUP_REQUIRED")
    
    @schemas.classproperty
    def COUNTRY_NOT_SUPPORTED(cls):
        return cls("COUNTRY_NOT_SUPPORTED")
    
    @schemas.classproperty
    def INSTITUTION_DOWN(cls):
        return cls("INSTITUTION_DOWN")
    
    @schemas.classproperty
    def INSTITUTION_NO_LONGER_SUPPORTED(cls):
        return cls("INSTITUTION_NO_LONGER_SUPPORTED")
    
    @schemas.classproperty
    def INSTITUTION_NOT_RESPONDING(cls):
        return cls("INSTITUTION_NOT_RESPONDING")
    
    @schemas.classproperty
    def INVALID_CREDENTIALS(cls):
        return cls("INVALID_CREDENTIALS")
    
    @schemas.classproperty
    def INVALID_MFA(cls):
        return cls("INVALID_MFA")
    
    @schemas.classproperty
    def INVALID_SEND_METHOD(cls):
        return cls("INVALID_SEND_METHOD")
    
    @schemas.classproperty
    def ITEM_LOGIN_REQUIRED(cls):
        return cls("ITEM_LOGIN_REQUIRED")
    
    @schemas.classproperty
    def MFA_NOT_SUPPORTED(cls):
        return cls("MFA_NOT_SUPPORTED")
    
    @schemas.classproperty
    def NO_ACCOUNTS(cls):
        return cls("NO_ACCOUNTS")
    
    @schemas.classproperty
    def ITEM_NOT_SUPPORTED(cls):
        return cls("ITEM_NOT_SUPPORTED")
    
    @schemas.classproperty
    def ACCESS_NOT_GRANTED(cls):
        return cls("ACCESS_NOT_GRANTED")
