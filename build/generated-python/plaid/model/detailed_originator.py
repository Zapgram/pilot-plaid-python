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


class DetailedOriginator(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Originator and their status.
    """


    class MetaOapg:
        required = {
            "transfer_diligence_status",
            "company_name",
            "client_id",
        }
        
        class properties:
            client_id = schemas.StrSchema
        
            @staticmethod
            def transfer_diligence_status() -> typing.Type['TransferDiligenceStatus']:
                return TransferDiligenceStatus
            company_name = schemas.StrSchema
            __annotations__ = {
                "client_id": client_id,
                "transfer_diligence_status": transfer_diligence_status,
                "company_name": company_name,
            }
        additional_properties = schemas.AnyTypeSchema
    
    transfer_diligence_status: 'TransferDiligenceStatus'
    company_name: MetaOapg.properties.company_name
    client_id: MetaOapg.properties.client_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_diligence_status"]) -> 'TransferDiligenceStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_name"]) -> MetaOapg.properties.company_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transfer_diligence_status"], typing_extensions.Literal["company_name"], typing_extensions.Literal["client_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_diligence_status"]) -> 'TransferDiligenceStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_name"]) -> MetaOapg.properties.company_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transfer_diligence_status"], typing_extensions.Literal["company_name"], typing_extensions.Literal["client_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        transfer_diligence_status: 'TransferDiligenceStatus',
        company_name: typing.Union[MetaOapg.properties.company_name, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'DetailedOriginator':
        return super().__new__(
            cls,
            *_args,
            transfer_diligence_status=transfer_diligence_status,
            company_name=company_name,
            client_id=client_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.transfer_diligence_status import TransferDiligenceStatus
