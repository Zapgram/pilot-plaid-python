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


class ActivityType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Types of consent activities
    """
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
    
    @schemas.classproperty
    def ITEM_CREATE(cls):
        return cls("ITEM_CREATE")
    
    @schemas.classproperty
    def ITEM_IMPORT(cls):
        return cls("ITEM_IMPORT")
    
    @schemas.classproperty
    def ITEM_UPDATE(cls):
        return cls("ITEM_UPDATE")
    
    @schemas.classproperty
    def ITEM_UNLINK(cls):
        return cls("ITEM_UNLINK")
    
    @schemas.classproperty
    def PORTAL_UNLINK(cls):
        return cls("PORTAL_UNLINK")
    
    @schemas.classproperty
    def PORTAL_ITEMS_DELETE(cls):
        return cls("PORTAL_ITEMS_DELETE")
    
    @schemas.classproperty
    def ITEM_REMOVE(cls):
        return cls("ITEM_REMOVE")
    
    @schemas.classproperty
    def INVARIANT_CHECKER_DELETION(cls):
        return cls("INVARIANT_CHECKER_DELETION")
    
    @schemas.classproperty
    def SCOPES_UPDATE(cls):
        return cls("SCOPES_UPDATE")
