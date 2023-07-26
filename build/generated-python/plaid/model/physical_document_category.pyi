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


class PhysicalDocumentCategory(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of identity document detected in the images provided. Will always be one of the following values:

  `drivers_license` - A driver's license for the associated country

  `id_card` - A general national identification card, distinct from driver's licenses

  `passport` - A passport for the associated country

  `residence_permit_card` - An identity document permitting a foreign citizen to <em>temporarily</em> reside in the associated country

  `resident_card` - An identity document permitting a foreign citizen to <em>permanently</em> reside in the associated country

Note: This value may be different from the ID type that the user selects within Link. For example, if they select "Driver's License" but then submit a picture of a passport, this field will say `passport`
    """
    
    @schemas.classproperty
    def DRIVERS_LICENSE(cls):
        return cls("drivers_license")
    
    @schemas.classproperty
    def ID_CARD(cls):
        return cls("id_card")
    
    @schemas.classproperty
    def PASSPORT(cls):
        return cls("passport")
    
    @schemas.classproperty
    def RESIDENCE_PERMIT_CARD(cls):
        return cls("residence_permit_card")
    
    @schemas.classproperty
    def RESIDENT_CARD(cls):
        return cls("resident_card")
