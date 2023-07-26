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


class PartnerEndCustomerOAuthStatusUpdatedValues(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The OAuth status of the update
    """


    class MetaOapg:
        enum_value_to_name = {
            "not-started": "NOTSTARTED",
            "processing": "PROCESSING",
            "approved": "APPROVED",
            "enabled": "ENABLED",
            "attention-required": "ATTENTIONREQUIRED",
        }
    
    @schemas.classproperty
    def NOTSTARTED(cls):
        return cls("not-started")
    
    @schemas.classproperty
    def PROCESSING(cls):
        return cls("processing")
    
    @schemas.classproperty
    def APPROVED(cls):
        return cls("approved")
    
    @schemas.classproperty
    def ENABLED(cls):
        return cls("enabled")
    
    @schemas.classproperty
    def ATTENTIONREQUIRED(cls):
        return cls("attention-required")
