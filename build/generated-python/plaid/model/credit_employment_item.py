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


class CreditEmploymentItem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The object containing employment items.
    """


    class MetaOapg:
        required = {
            "item_id",
            "employments",
        }
        
        class properties:
            item_id = schemas.StrSchema
            
            
            class employments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CreditEmploymentVerification']:
                        return CreditEmploymentVerification
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CreditEmploymentVerification'], typing.List['CreditEmploymentVerification']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employments':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CreditEmploymentVerification':
                    return super().__getitem__(i)
            employment_report_token = schemas.StrSchema
            __annotations__ = {
                "item_id": item_id,
                "employments": employments,
                "employment_report_token": employment_report_token,
            }
        additional_properties = schemas.AnyTypeSchema
    
    item_id: MetaOapg.properties.item_id
    employments: MetaOapg.properties.employments
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employments"]) -> MetaOapg.properties.employments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_report_token"]) -> MetaOapg.properties.employment_report_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["item_id"], typing_extensions.Literal["employments"], typing_extensions.Literal["employment_report_token"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employments"]) -> MetaOapg.properties.employments: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_report_token"]) -> typing.Union[MetaOapg.properties.employment_report_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["item_id"], typing_extensions.Literal["employments"], typing_extensions.Literal["employment_report_token"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        item_id: typing.Union[MetaOapg.properties.item_id, str, ],
        employments: typing.Union[MetaOapg.properties.employments, list, tuple, ],
        employment_report_token: typing.Union[MetaOapg.properties.employment_report_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreditEmploymentItem':
        return super().__new__(
            cls,
            *_args,
            item_id=item_id,
            employments=employments,
            employment_report_token=employment_report_token,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.credit_employment_verification import CreditEmploymentVerification