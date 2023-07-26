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


class OverrideAccountType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    `investment:` Investment account.

`credit:` Credit card

`depository:` Depository account

`loan:` Loan account

`payroll:` Payroll account

`other:` Non-specified account type

See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.
    """


    class MetaOapg:
        enum_value_to_name = {
            "investment": "INVESTMENT",
            "credit": "CREDIT",
            "depository": "DEPOSITORY",
            "loan": "LOAN",
            "payroll": "PAYROLL",
            "other": "OTHER",
        }
    
    @schemas.classproperty
    def INVESTMENT(cls):
        return cls("investment")
    
    @schemas.classproperty
    def CREDIT(cls):
        return cls("credit")
    
    @schemas.classproperty
    def DEPOSITORY(cls):
        return cls("depository")
    
    @schemas.classproperty
    def LOAN(cls):
        return cls("loan")
    
    @schemas.classproperty
    def PAYROLL(cls):
        return cls("payroll")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("other")
