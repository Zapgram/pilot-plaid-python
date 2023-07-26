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


class TransferAuthorizationGuaranteeDecisionRationaleCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A code representing the reason Plaid declined to guarantee this transfer:

`RETURN_BANK`: The risk of a bank-initiated return (for example, an R01/NSF) is too high to guarantee this transfer.

`RETURN_CUSTOMER`: The risk of a customer-initiated return (for example, a R10/Unauthorized) is too high to guarantee this transfer.

`GUARANTEE_LIMIT_REACHED`: This transfer is low-risk, but Guarantee has exhausted an internal limit on the number or rate of guarantees that applies to this transfer.

`RISK_ESTIMATE_UNAVAILABLE`: A risk estimate is unavailable for this Item.

`REQUIRED_PARAM_MISSING`: Required fields are missing.
    """


    class MetaOapg:
        enum_value_to_name = {
            "RETURN_BANK": "RETURN_BANK",
            "RETURN_CUSTOMER": "RETURN_CUSTOMER",
            "GUARANTEE_LIMIT_REACHED": "GUARANTEE_LIMIT_REACHED",
            "RISK_ESTIMATE_UNAVAILABLE": "RISK_ESTIMATE_UNAVAILABLE",
            "REQUIRED_PARAM_MISSING": "REQUIRED_PARAM_MISSING",
        }
    
    @schemas.classproperty
    def RETURN_BANK(cls):
        return cls("RETURN_BANK")
    
    @schemas.classproperty
    def RETURN_CUSTOMER(cls):
        return cls("RETURN_CUSTOMER")
    
    @schemas.classproperty
    def GUARANTEE_LIMIT_REACHED(cls):
        return cls("GUARANTEE_LIMIT_REACHED")
    
    @schemas.classproperty
    def RISK_ESTIMATE_UNAVAILABLE(cls):
        return cls("RISK_ESTIMATE_UNAVAILABLE")
    
    @schemas.classproperty
    def REQUIRED_PARAM_MISSING(cls):
        return cls("REQUIRED_PARAM_MISSING")
