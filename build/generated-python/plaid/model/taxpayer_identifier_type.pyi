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


class TaxpayerIdentifierType(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A value from a MISMO prescribed list that classifies identification numbers used by the Internal Revenue Service (IRS) in the administration of tax laws. A Social Security number (SSN) is issued by the SSA; all other taxpayer identification numbers are issued by the IRS.
    """


    class MetaOapg:
        enum_value_to_name = {
            "IndividualTaxpayerIdentificationNumber": "INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER",
            "SocialSecurityNumber": "SOCIAL_SECURITY_NUMBER",
        }
    
    @schemas.classproperty
    def INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER(cls):
        return cls("IndividualTaxpayerIdentificationNumber")
    
    @schemas.classproperty
    def SOCIAL_SECURITY_NUMBER(cls):
        return cls("SocialSecurityNumber")


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TaxpayerIdentifierType':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
