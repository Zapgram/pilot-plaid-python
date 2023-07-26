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


class LinkDeliveryMetadata(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Information related to the related to the delivery of the link session to users
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def communication_method() -> typing.Type['LinkDeliveryWebhookCommunicationMethod']:
                return LinkDeliveryWebhookCommunicationMethod
        
            @staticmethod
            def delivery_status() -> typing.Type['LinkDeliveryWebhookDeliveryStatus']:
                return LinkDeliveryWebhookDeliveryStatus
            __annotations__ = {
                "communication_method": communication_method,
                "delivery_status": delivery_status,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["communication_method"]) -> 'LinkDeliveryWebhookCommunicationMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery_status"]) -> 'LinkDeliveryWebhookDeliveryStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["communication_method"], typing_extensions.Literal["delivery_status"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["communication_method"]) -> typing.Union['LinkDeliveryWebhookCommunicationMethod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery_status"]) -> typing.Union['LinkDeliveryWebhookDeliveryStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["communication_method"], typing_extensions.Literal["delivery_status"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        communication_method: typing.Union['LinkDeliveryWebhookCommunicationMethod', schemas.Unset] = schemas.unset,
        delivery_status: typing.Union['LinkDeliveryWebhookDeliveryStatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'LinkDeliveryMetadata':
        return super().__new__(
            cls,
            *_args,
            communication_method=communication_method,
            delivery_status=delivery_status,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.link_delivery_webhook_communication_method import LinkDeliveryWebhookCommunicationMethod
from plaid.model.link_delivery_webhook_delivery_status import LinkDeliveryWebhookDeliveryStatus
