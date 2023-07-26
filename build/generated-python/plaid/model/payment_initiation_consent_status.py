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


class PaymentInitiationConsentStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of the payment consent.

`UNAUTHORISED`: Consent created, but requires user authorisation.

`REJECTED`: Consent authorisation was rejected by the user and/or the bank.

`AUTHORISED`: Consent is active and ready to be used.

`REVOKED`: Consent has been revoked and can no longer be used.

`EXPIRED`: Consent is no longer valid.
    """


    class MetaOapg:
        enum_value_to_name = {
            "UNAUTHORISED": "UNAUTHORISED",
            "AUTHORISED": "AUTHORISED",
            "REVOKED": "REVOKED",
            "REJECTED": "REJECTED",
            "EXPIRED": "EXPIRED",
        }
    
    @schemas.classproperty
    def UNAUTHORISED(cls):
        return cls("UNAUTHORISED")
    
    @schemas.classproperty
    def AUTHORISED(cls):
        return cls("AUTHORISED")
    
    @schemas.classproperty
    def REVOKED(cls):
        return cls("REVOKED")
    
    @schemas.classproperty
    def REJECTED(cls):
        return cls("REJECTED")
    
    @schemas.classproperty
    def EXPIRED(cls):
        return cls("EXPIRED")
