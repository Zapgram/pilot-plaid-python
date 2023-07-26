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


class ClientProvidedTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A client-provided transaction for Plaid to enrich.
    """


    class MetaOapg:
        required = {
            "amount",
            "iso_currency_code",
            "description",
            "id",
            "direction",
        }
        
        class properties:
            id = schemas.StrSchema
            description = schemas.StrSchema
            amount = schemas.Float64Schema
        
            @staticmethod
            def direction() -> typing.Type['EnrichTransactionDirection']:
                return EnrichTransactionDirection
            iso_currency_code = schemas.StrSchema
            client_user_id = schemas.StrSchema
            client_account_id = schemas.StrSchema
            account_type = schemas.StrSchema
            account_subtype = schemas.StrSchema
        
            @staticmethod
            def location() -> typing.Type['ClientProvidedTransactionLocation']:
                return ClientProvidedTransactionLocation
            mcc = schemas.StrSchema
            date_posted = schemas.DateSchema
            __annotations__ = {
                "id": id,
                "description": description,
                "amount": amount,
                "direction": direction,
                "iso_currency_code": iso_currency_code,
                "client_user_id": client_user_id,
                "client_account_id": client_account_id,
                "account_type": account_type,
                "account_subtype": account_subtype,
                "location": location,
                "mcc": mcc,
                "date_posted": date_posted,
            }
        additional_properties = schemas.AnyTypeSchema
    
    amount: MetaOapg.properties.amount
    iso_currency_code: MetaOapg.properties.iso_currency_code
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    direction: 'EnrichTransactionDirection'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> 'EnrichTransactionDirection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_user_id"]) -> MetaOapg.properties.client_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_account_id"]) -> MetaOapg.properties.client_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_subtype"]) -> MetaOapg.properties.account_subtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> 'ClientProvidedTransactionLocation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mcc"]) -> MetaOapg.properties.mcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_posted"]) -> MetaOapg.properties.date_posted: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], typing_extensions.Literal["direction"], typing_extensions.Literal["client_user_id"], typing_extensions.Literal["client_account_id"], typing_extensions.Literal["account_type"], typing_extensions.Literal["account_subtype"], typing_extensions.Literal["location"], typing_extensions.Literal["mcc"], typing_extensions.Literal["date_posted"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iso_currency_code"]) -> MetaOapg.properties.iso_currency_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> 'EnrichTransactionDirection': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_user_id"]) -> typing.Union[MetaOapg.properties.client_user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_account_id"]) -> typing.Union[MetaOapg.properties.client_account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_type"]) -> typing.Union[MetaOapg.properties.account_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_subtype"]) -> typing.Union[MetaOapg.properties.account_subtype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union['ClientProvidedTransactionLocation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mcc"]) -> typing.Union[MetaOapg.properties.mcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_posted"]) -> typing.Union[MetaOapg.properties.date_posted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["iso_currency_code"], typing_extensions.Literal["description"], typing_extensions.Literal["id"], typing_extensions.Literal["direction"], typing_extensions.Literal["client_user_id"], typing_extensions.Literal["client_account_id"], typing_extensions.Literal["account_type"], typing_extensions.Literal["account_subtype"], typing_extensions.Literal["location"], typing_extensions.Literal["mcc"], typing_extensions.Literal["date_posted"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        iso_currency_code: typing.Union[MetaOapg.properties.iso_currency_code, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        direction: 'EnrichTransactionDirection',
        client_user_id: typing.Union[MetaOapg.properties.client_user_id, str, schemas.Unset] = schemas.unset,
        client_account_id: typing.Union[MetaOapg.properties.client_account_id, str, schemas.Unset] = schemas.unset,
        account_type: typing.Union[MetaOapg.properties.account_type, str, schemas.Unset] = schemas.unset,
        account_subtype: typing.Union[MetaOapg.properties.account_subtype, str, schemas.Unset] = schemas.unset,
        location: typing.Union['ClientProvidedTransactionLocation', schemas.Unset] = schemas.unset,
        mcc: typing.Union[MetaOapg.properties.mcc, str, schemas.Unset] = schemas.unset,
        date_posted: typing.Union[MetaOapg.properties.date_posted, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ClientProvidedTransaction':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            iso_currency_code=iso_currency_code,
            description=description,
            id=id,
            direction=direction,
            client_user_id=client_user_id,
            client_account_id=client_account_id,
            account_type=account_type,
            account_subtype=account_subtype,
            location=location,
            mcc=mcc,
            date_posted=date_posted,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.client_provided_transaction_location import ClientProvidedTransactionLocation
from plaid.model.enrich_transaction_direction import EnrichTransactionDirection