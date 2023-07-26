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


class CreditFreddieMacPartyVOA24(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider.
    """


    class MetaOapg:
        required = {
            "TAXPAYER_IDENTIFIERS",
            "ROLES",
            "INDIVIDUAL",
        }
        
        class properties:
        
            @staticmethod
            def INDIVIDUAL() -> typing.Type['CreditFreddieMacPartyIndividualVOA24']:
                return CreditFreddieMacPartyIndividualVOA24
        
            @staticmethod
            def ROLES() -> typing.Type['Roles']:
                return Roles
        
            @staticmethod
            def TAXPAYER_IDENTIFIERS() -> typing.Type['TaxpayerIdentifiers']:
                return TaxpayerIdentifiers
            __annotations__ = {
                "INDIVIDUAL": INDIVIDUAL,
                "ROLES": ROLES,
                "TAXPAYER_IDENTIFIERS": TAXPAYER_IDENTIFIERS,
            }
        additional_properties = schemas.AnyTypeSchema
    
    TAXPAYER_IDENTIFIERS: 'TaxpayerIdentifiers'
    ROLES: 'Roles'
    INDIVIDUAL: 'CreditFreddieMacPartyIndividualVOA24'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TAXPAYER_IDENTIFIERS"]) -> 'TaxpayerIdentifiers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ROLES"]) -> 'Roles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["INDIVIDUAL"]) -> 'CreditFreddieMacPartyIndividualVOA24': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TAXPAYER_IDENTIFIERS"], typing_extensions.Literal["ROLES"], typing_extensions.Literal["INDIVIDUAL"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TAXPAYER_IDENTIFIERS"]) -> 'TaxpayerIdentifiers': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ROLES"]) -> 'Roles': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["INDIVIDUAL"]) -> 'CreditFreddieMacPartyIndividualVOA24': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TAXPAYER_IDENTIFIERS"], typing_extensions.Literal["ROLES"], typing_extensions.Literal["INDIVIDUAL"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        TAXPAYER_IDENTIFIERS: 'TaxpayerIdentifiers',
        ROLES: 'Roles',
        INDIVIDUAL: 'CreditFreddieMacPartyIndividualVOA24',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreditFreddieMacPartyVOA24':
        return super().__new__(
            cls,
            *_args,
            TAXPAYER_IDENTIFIERS=TAXPAYER_IDENTIFIERS,
            ROLES=ROLES,
            INDIVIDUAL=INDIVIDUAL,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.credit_freddie_mac_party_individual_voa24 import CreditFreddieMacPartyIndividualVOA24
from plaid.model.roles import Roles
from plaid.model.taxpayer_identifiers import TaxpayerIdentifiers
