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


class Products(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A list of products that an institution can support. All Items must be initialized with at least one product. The Balance product is always available and does not need to be specified during initialization.
    """


    class MetaOapg:
        enum_value_to_name = {
            "assets": "ASSETS",
            "auth": "AUTH",
            "balance": "BALANCE",
            "identity": "IDENTITY",
            "investments": "INVESTMENTS",
            "investments_auth": "INVESTMENTS_AUTH",
            "liabilities": "LIABILITIES",
            "payment_initiation": "PAYMENT_INITIATION",
            "identity_verification": "IDENTITY_VERIFICATION",
            "transactions": "TRANSACTIONS",
            "credit_details": "CREDIT_DETAILS",
            "income": "INCOME",
            "income_verification": "INCOME_VERIFICATION",
            "deposit_switch": "DEPOSIT_SWITCH",
            "standing_orders": "STANDING_ORDERS",
            "transfer": "TRANSFER",
            "employment": "EMPLOYMENT",
            "recurring_transactions": "RECURRING_TRANSACTIONS",
            "signal": "SIGNAL",
        }
    
    @schemas.classproperty
    def ASSETS(cls):
        return cls("assets")
    
    @schemas.classproperty
    def AUTH(cls):
        return cls("auth")
    
    @schemas.classproperty
    def BALANCE(cls):
        return cls("balance")
    
    @schemas.classproperty
    def IDENTITY(cls):
        return cls("identity")
    
    @schemas.classproperty
    def INVESTMENTS(cls):
        return cls("investments")
    
    @schemas.classproperty
    def INVESTMENTS_AUTH(cls):
        return cls("investments_auth")
    
    @schemas.classproperty
    def LIABILITIES(cls):
        return cls("liabilities")
    
    @schemas.classproperty
    def PAYMENT_INITIATION(cls):
        return cls("payment_initiation")
    
    @schemas.classproperty
    def IDENTITY_VERIFICATION(cls):
        return cls("identity_verification")
    
    @schemas.classproperty
    def TRANSACTIONS(cls):
        return cls("transactions")
    
    @schemas.classproperty
    def CREDIT_DETAILS(cls):
        return cls("credit_details")
    
    @schemas.classproperty
    def INCOME(cls):
        return cls("income")
    
    @schemas.classproperty
    def INCOME_VERIFICATION(cls):
        return cls("income_verification")
    
    @schemas.classproperty
    def DEPOSIT_SWITCH(cls):
        return cls("deposit_switch")
    
    @schemas.classproperty
    def STANDING_ORDERS(cls):
        return cls("standing_orders")
    
    @schemas.classproperty
    def TRANSFER(cls):
        return cls("transfer")
    
    @schemas.classproperty
    def EMPLOYMENT(cls):
        return cls("employment")
    
    @schemas.classproperty
    def RECURRING_TRANSACTIONS(cls):
        return cls("recurring_transactions")
    
    @schemas.classproperty
    def SIGNAL(cls):
        return cls("signal")