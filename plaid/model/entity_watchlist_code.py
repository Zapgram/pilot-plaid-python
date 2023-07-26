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


class EntityWatchlistCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Shorthand identifier for a specific screening list for entities.
    """


    class MetaOapg:
        enum_value_to_name = {
            "CA_CON": "CA_CON",
            "EU_CON": "EU_CON",
            "IZ_SOE": "IZ_SOE",
            "IZ_UNC": "IZ_UNC",
            "IZ_WBK": "IZ_WBK",
            "US_CAP": "US_CAP",
            "US_FSE": "US_FSE",
            "US_MBS": "US_MBS",
            "US_SDN": "US_SDN",
            "US_SSI": "US_SSI",
            "US_CMC": "US_CMC",
            "US_UVL": "US_UVL",
            "AU_CON": "AU_CON",
            "UK_HMC": "UK_HMC",
        }
    
    @schemas.classproperty
    def CA_CON(cls):
        return cls("CA_CON")
    
    @schemas.classproperty
    def EU_CON(cls):
        return cls("EU_CON")
    
    @schemas.classproperty
    def IZ_SOE(cls):
        return cls("IZ_SOE")
    
    @schemas.classproperty
    def IZ_UNC(cls):
        return cls("IZ_UNC")
    
    @schemas.classproperty
    def IZ_WBK(cls):
        return cls("IZ_WBK")
    
    @schemas.classproperty
    def US_CAP(cls):
        return cls("US_CAP")
    
    @schemas.classproperty
    def US_FSE(cls):
        return cls("US_FSE")
    
    @schemas.classproperty
    def US_MBS(cls):
        return cls("US_MBS")
    
    @schemas.classproperty
    def US_SDN(cls):
        return cls("US_SDN")
    
    @schemas.classproperty
    def US_SSI(cls):
        return cls("US_SSI")
    
    @schemas.classproperty
    def US_CMC(cls):
        return cls("US_CMC")
    
    @schemas.classproperty
    def US_UVL(cls):
        return cls("US_UVL")
    
    @schemas.classproperty
    def AU_CON(cls):
        return cls("AU_CON")
    
    @schemas.classproperty
    def UK_HMC(cls):
        return cls("UK_HMC")