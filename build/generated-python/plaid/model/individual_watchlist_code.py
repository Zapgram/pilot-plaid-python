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


class IndividualWatchlistCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Shorthand identifier for a specific screening list for individuals.
    """


    class MetaOapg:
        enum_value_to_name = {
            "AU_CON": "AU_CON",
            "CA_CON": "CA_CON",
            "EU_CON": "EU_CON",
            "IZ_CIA": "IZ_CIA",
            "IZ_IPL": "IZ_IPL",
            "IZ_PEP": "IZ_PEP",
            "IZ_UNC": "IZ_UNC",
            "IZ_WBK": "IZ_WBK",
            "UK_HMC": "UK_HMC",
            "US_DPL": "US_DPL",
            "US_DTC": "US_DTC",
            "US_FBI": "US_FBI",
            "US_FSE": "US_FSE",
            "US_ISN": "US_ISN",
            "US_MBS": "US_MBS",
            "US_PLC": "US_PLC",
            "US_SDN": "US_SDN",
            "US_SSI": "US_SSI",
            "SG_SOF": "SG_SOF",
            "TR_TWL": "TR_TWL",
            "TR_DFD": "TR_DFD",
            "TR_FOR": "TR_FOR",
            "TR_WMD": "TR_WMD",
            "TR_CMB": "TR_CMB",
        }
    
    @schemas.classproperty
    def AU_CON(cls):
        return cls("AU_CON")
    
    @schemas.classproperty
    def CA_CON(cls):
        return cls("CA_CON")
    
    @schemas.classproperty
    def EU_CON(cls):
        return cls("EU_CON")
    
    @schemas.classproperty
    def IZ_CIA(cls):
        return cls("IZ_CIA")
    
    @schemas.classproperty
    def IZ_IPL(cls):
        return cls("IZ_IPL")
    
    @schemas.classproperty
    def IZ_PEP(cls):
        return cls("IZ_PEP")
    
    @schemas.classproperty
    def IZ_UNC(cls):
        return cls("IZ_UNC")
    
    @schemas.classproperty
    def IZ_WBK(cls):
        return cls("IZ_WBK")
    
    @schemas.classproperty
    def UK_HMC(cls):
        return cls("UK_HMC")
    
    @schemas.classproperty
    def US_DPL(cls):
        return cls("US_DPL")
    
    @schemas.classproperty
    def US_DTC(cls):
        return cls("US_DTC")
    
    @schemas.classproperty
    def US_FBI(cls):
        return cls("US_FBI")
    
    @schemas.classproperty
    def US_FSE(cls):
        return cls("US_FSE")
    
    @schemas.classproperty
    def US_ISN(cls):
        return cls("US_ISN")
    
    @schemas.classproperty
    def US_MBS(cls):
        return cls("US_MBS")
    
    @schemas.classproperty
    def US_PLC(cls):
        return cls("US_PLC")
    
    @schemas.classproperty
    def US_SDN(cls):
        return cls("US_SDN")
    
    @schemas.classproperty
    def US_SSI(cls):
        return cls("US_SSI")
    
    @schemas.classproperty
    def SG_SOF(cls):
        return cls("SG_SOF")
    
    @schemas.classproperty
    def TR_TWL(cls):
        return cls("TR_TWL")
    
    @schemas.classproperty
    def TR_DFD(cls):
        return cls("TR_DFD")
    
    @schemas.classproperty
    def TR_FOR(cls):
        return cls("TR_FOR")
    
    @schemas.classproperty
    def TR_WMD(cls):
        return cls("TR_WMD")
    
    @schemas.classproperty
    def TR_CMB(cls):
        return cls("TR_CMB")