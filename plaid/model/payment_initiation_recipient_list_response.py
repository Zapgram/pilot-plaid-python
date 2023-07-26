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


class PaymentInitiationRecipientListResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PaymentInitiationRecipientListResponse defines the response schema for `/payment_initiation/recipient/list`
    """


    class MetaOapg:
        required = {
            "recipients",
            "request_id",
        }
        
        class properties:
            
            
            class recipients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentInitiationRecipient']:
                        return PaymentInitiationRecipient
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PaymentInitiationRecipient'], typing.List['PaymentInitiationRecipient']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'recipients':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PaymentInitiationRecipient':
                    return super().__getitem__(i)
            request_id = schemas.StrSchema
            __annotations__ = {
                "recipients": recipients,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    recipients: MetaOapg.properties.recipients
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipients"]) -> MetaOapg.properties.recipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recipients"], typing_extensions.Literal["request_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipients"]) -> MetaOapg.properties.recipients: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recipients"], typing_extensions.Literal["request_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        recipients: typing.Union[MetaOapg.properties.recipients, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PaymentInitiationRecipientListResponse':
        return super().__new__(
            cls,
            *_args,
            recipients=recipients,
            request_id=request_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.payment_initiation_recipient import PaymentInitiationRecipient