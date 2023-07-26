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


class LoanAccountSubtypes(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). 
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['LoanAccountSubtype']:
            return LoanAccountSubtype

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['LoanAccountSubtype'], typing.List['LoanAccountSubtype']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LoanAccountSubtypes':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'LoanAccountSubtype':
        return super().__getitem__(i)

from plaid.model.loan_account_subtype import LoanAccountSubtype
