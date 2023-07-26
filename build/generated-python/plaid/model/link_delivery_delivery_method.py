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


class LinkDeliveryDeliveryMethod(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The delivery method to be used to deliver the Hosted Link session URL.

`SMS`: The URL will be delivered through SMS

`EMAIL`: The URL will be delivered through email
    """


    class MetaOapg:
        enum_value_to_name = {
            "SMS": "SMS",
            "EMAIL": "EMAIL",
        }
    
    @schemas.classproperty
    def SMS(cls):
        return cls("SMS")
    
    @schemas.classproperty
    def EMAIL(cls):
        return cls("EMAIL")
