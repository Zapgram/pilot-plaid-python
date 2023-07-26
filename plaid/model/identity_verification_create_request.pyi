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


class IdentityVerificationCreateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request schema for '/identity_verification/create'
    """


    class MetaOapg:
        required = {
            "gave_consent",
            "is_shareable",
            "template_id",
        }
        
        class properties:
            is_shareable = schemas.BoolSchema
            template_id = schemas.StrSchema
            gave_consent = schemas.BoolSchema
        
            @staticmethod
            def client_user_id() -> typing.Type['ClientUserID']:
                return ClientUserID
        
            @staticmethod
            def user() -> typing.Type['IdentityVerificationCreateRequestUser']:
                return IdentityVerificationCreateRequestUser
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
        
            @staticmethod
            def is_idempotent() -> typing.Type['IdempotencyFlag']:
                return IdempotencyFlag
            __annotations__ = {
                "is_shareable": is_shareable,
                "template_id": template_id,
                "gave_consent": gave_consent,
                "client_user_id": client_user_id,
                "user": user,
                "client_id": client_id,
                "secret": secret,
                "is_idempotent": is_idempotent,
            }
    
    gave_consent: MetaOapg.properties.gave_consent
    is_shareable: MetaOapg.properties.is_shareable
    template_id: MetaOapg.properties.template_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_shareable"]) -> MetaOapg.properties.is_shareable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_id"]) -> MetaOapg.properties.template_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gave_consent"]) -> MetaOapg.properties.gave_consent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_user_id"]) -> 'ClientUserID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'IdentityVerificationCreateRequestUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_idempotent"]) -> 'IdempotencyFlag': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_shareable", "template_id", "gave_consent", "client_user_id", "user", "client_id", "secret", "is_idempotent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_shareable"]) -> MetaOapg.properties.is_shareable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_id"]) -> MetaOapg.properties.template_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gave_consent"]) -> MetaOapg.properties.gave_consent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_user_id"]) -> typing.Union['ClientUserID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['IdentityVerificationCreateRequestUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_idempotent"]) -> typing.Union['IdempotencyFlag', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_shareable", "template_id", "gave_consent", "client_user_id", "user", "client_id", "secret", "is_idempotent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gave_consent: typing.Union[MetaOapg.properties.gave_consent, bool, ],
        is_shareable: typing.Union[MetaOapg.properties.is_shareable, bool, ],
        template_id: typing.Union[MetaOapg.properties.template_id, str, ],
        client_user_id: typing.Union['ClientUserID', schemas.Unset] = schemas.unset,
        user: typing.Union['IdentityVerificationCreateRequestUser', schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        is_idempotent: typing.Union['IdempotencyFlag', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IdentityVerificationCreateRequest':
        return super().__new__(
            cls,
            *_args,
            gave_consent=gave_consent,
            is_shareable=is_shareable,
            template_id=template_id,
            client_user_id=client_user_id,
            user=user,
            client_id=client_id,
            secret=secret,
            is_idempotent=is_idempotent,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.client_user_id import ClientUserID
from plaid.model.idempotency_flag import IdempotencyFlag
from plaid.model.identity_verification_create_request_user import IdentityVerificationCreateRequestUser