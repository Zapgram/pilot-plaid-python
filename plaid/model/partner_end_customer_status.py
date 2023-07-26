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


class PartnerEndCustomerStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of the given end customer.

`UNDER_REVIEW`: The end customer has been created and enabled in the non-Production environments. The end customer must be manually reviewed by the Plaid team before it can be enabled in production, at which point its status will automatically transition to `PENDING_ENABLEMENT` or `DENIED`.

`PENDING_ENABLEMENT`: The end customer is ready to be enabled in the Production environment. Call the `/partner/customer/enable` endpoint to enable the end customer in Production.

`ACTIVE`: The end customer has been enabled in all environments.

`DENIED`: The end customer has been created and enabled in the non-Production environments, but it did not pass review by the Plaid team and therefore cannot be enabled in the Production environment. Talk to your Account Manager for more information.
    """


    class MetaOapg:
        enum_value_to_name = {
            "UNDER_REVIEW": "UNDER_REVIEW",
            "PENDING_ENABLEMENT": "PENDING_ENABLEMENT",
            "ACTIVE": "ACTIVE",
            "DENIED": "DENIED",
        }
    
    @schemas.classproperty
    def UNDER_REVIEW(cls):
        return cls("UNDER_REVIEW")
    
    @schemas.classproperty
    def PENDING_ENABLEMENT(cls):
        return cls("PENDING_ENABLEMENT")
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("ACTIVE")
    
    @schemas.classproperty
    def DENIED(cls):
        return cls("DENIED")