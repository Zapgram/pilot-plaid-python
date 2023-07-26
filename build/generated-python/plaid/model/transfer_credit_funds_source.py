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


class TransferCreditFundsSource(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies the source of funds for the transfer. Only valid for `credit` transfers, and defaults to `sweep` if not specified. This field is not specified for `debit` transfers.

`sweep` - Sweep funds from your funding account
`prefunded_rtp_credits` - Use your prefunded RTP credit balance with Plaid
`prefunded_ach_credits` - Use your prefunded ACH credit balance with Plaid
    """


    class MetaOapg:
        enum_value_to_name = {
            "sweep": "SWEEP",
            "prefunded_rtp_credits": "PREFUNDED_RTP_CREDITS",
            "prefunded_ach_credits": "PREFUNDED_ACH_CREDITS",
            schemas.NoneClass.NONE: "NONE",
        }
    
    @schemas.classproperty
    def SWEEP(cls):
        return cls("sweep")
    
    @schemas.classproperty
    def PREFUNDED_RTP_CREDITS(cls):
        return cls("prefunded_rtp_credits")
    
    @schemas.classproperty
    def PREFUNDED_ACH_CREDITS(cls):
        return cls("prefunded_ach_credits")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransferCreditFundsSource':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )