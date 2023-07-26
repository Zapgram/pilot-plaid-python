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


class LinkDeliveryWebhookCallbackType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of Link callback event
    """


    class MetaOapg:
        enum_value_to_name = {
            "ON_SUCCESS": "SUCCESS",
            "ON_EVENT": "EVENT",
            "ON_EXIT": "EXIT",
        }
    
    @schemas.classproperty
    def SUCCESS(cls):
        return cls("ON_SUCCESS")
    
    @schemas.classproperty
    def EVENT(cls):
        return cls("ON_EVENT")
    
    @schemas.classproperty
    def EXIT(cls):
        return cls("ON_EXIT")
