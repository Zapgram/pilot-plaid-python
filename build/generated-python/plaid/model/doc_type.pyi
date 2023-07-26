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


class DocType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of document.

`DOCUMENT_TYPE_PAYSTUB`: A paystub.

`DOCUMENT_TYPE_BANK_STATEMENT`: A bank statement.

`DOCUMENT_TYPE_US_TAX_W2`: A W-2 wage and tax statement provided by a US employer reflecting wages earned by the employee.

`DOCUMENT_TYPE_US_MILITARY_ERAS`: An electronic Retirement Account Statement (eRAS) issued by the US military.

`DOCUMENT_TYPE_US_MILITARY_LES`: A Leave and Earnings Statement (LES) issued by the US military.

`DOCUMENT_TYPE_US_MILITARY_CLES`: A Civilian Leave and Earnings Statement (CLES) issued by the US military.

`DOCUMENT_TYPE_GIG`: Used to indicate that the income is related to gig work. Does not necessarily correspond to a specific document type.

`DOCUMENT_TYPE_NONE`: Used to indicate that there is no underlying document for the data.

`DOCUMENT_TYPE_PLAID_GENERATED_PAYSTUB_PDF`: Used to indicate that the PDF for the paystub was generated by Plaid.

`UNKNOWN`: Document type could not be determined.
    """
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_PAYSTUB(cls):
        return cls("DOCUMENT_TYPE_PAYSTUB")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_BANK_STATEMENT(cls):
        return cls("DOCUMENT_TYPE_BANK_STATEMENT")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_US_TAX_W2(cls):
        return cls("DOCUMENT_TYPE_US_TAX_W2")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_US_MILITARY_ERAS(cls):
        return cls("DOCUMENT_TYPE_US_MILITARY_ERAS")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_US_MILITARY_LES(cls):
        return cls("DOCUMENT_TYPE_US_MILITARY_LES")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_US_MILITARY_CLES(cls):
        return cls("DOCUMENT_TYPE_US_MILITARY_CLES")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_GIG(cls):
        return cls("DOCUMENT_TYPE_GIG")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_NONE(cls):
        return cls("DOCUMENT_TYPE_NONE")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_US_TAX_1099_MISC(cls):
        return cls("DOCUMENT_TYPE_US_TAX_1099_MISC")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_US_TAX_1099_K(cls):
        return cls("DOCUMENT_TYPE_US_TAX_1099_K")
    
    @schemas.classproperty
    def DOCUMENT_TYPE_PLAID_GENERATED_PAYSTUB_PDF(cls):
        return cls("DOCUMENT_TYPE_PLAID_GENERATED_PAYSTUB_PDF")
