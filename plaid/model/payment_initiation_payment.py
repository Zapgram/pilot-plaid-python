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


class PaymentInitiationPayment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PaymentInitiationPayment defines a payment initiation payment
    """


    class MetaOapg:
        required = {
            "reference",
            "bacs",
            "amount",
            "payment_id",
            "iban",
            "last_status_update",
            "recipient_id",
            "status",
        }
        
        class properties:
            payment_id = schemas.StrSchema
        
            @staticmethod
            def amount() -> typing.Type['PaymentAmount']:
                return PaymentAmount
        
            @staticmethod
            def status() -> typing.Type['PaymentInitiationPaymentStatus']:
                return PaymentInitiationPaymentStatus
            recipient_id = schemas.StrSchema
            reference = schemas.StrSchema
            last_status_update = schemas.DateTimeSchema
        
            @staticmethod
            def bacs() -> typing.Type['SenderBACSNullable']:
                return SenderBACSNullable
            
            
            class iban(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iban':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class adjusted_reference(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'adjusted_reference':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def schedule() -> typing.Type['ExternalPaymentScheduleGet']:
                return ExternalPaymentScheduleGet
        
            @staticmethod
            def refund_details() -> typing.Type['ExternalPaymentRefundDetails']:
                return ExternalPaymentRefundDetails
            
            
            class refund_ids(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refund_ids':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def amount_refunded() -> typing.Type['PaymentAmountRefunded']:
                return PaymentAmountRefunded
            
            
            class wallet_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wallet_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def scheme() -> typing.Type['PaymentScheme']:
                return PaymentScheme
        
            @staticmethod
            def adjusted_scheme() -> typing.Type['PaymentScheme']:
                return PaymentScheme
            
            
            class consent_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'consent_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class transaction_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transaction_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "payment_id": payment_id,
                "amount": amount,
                "status": status,
                "recipient_id": recipient_id,
                "reference": reference,
                "last_status_update": last_status_update,
                "bacs": bacs,
                "iban": iban,
                "adjusted_reference": adjusted_reference,
                "schedule": schedule,
                "refund_details": refund_details,
                "refund_ids": refund_ids,
                "amount_refunded": amount_refunded,
                "wallet_id": wallet_id,
                "scheme": scheme,
                "adjusted_scheme": adjusted_scheme,
                "consent_id": consent_id,
                "transaction_id": transaction_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    reference: MetaOapg.properties.reference
    bacs: 'SenderBACSNullable'
    amount: 'PaymentAmount'
    payment_id: MetaOapg.properties.payment_id
    iban: MetaOapg.properties.iban
    last_status_update: MetaOapg.properties.last_status_update
    recipient_id: MetaOapg.properties.recipient_id
    status: 'PaymentInitiationPaymentStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bacs"]) -> 'SenderBACSNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'PaymentAmount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_id"]) -> MetaOapg.properties.payment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_status_update"]) -> MetaOapg.properties.last_status_update: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient_id"]) -> MetaOapg.properties.recipient_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'PaymentInitiationPaymentStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adjusted_reference"]) -> MetaOapg.properties.adjusted_reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'ExternalPaymentScheduleGet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refund_details"]) -> 'ExternalPaymentRefundDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refund_ids"]) -> MetaOapg.properties.refund_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_refunded"]) -> 'PaymentAmountRefunded': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wallet_id"]) -> MetaOapg.properties.wallet_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheme"]) -> 'PaymentScheme': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adjusted_scheme"]) -> 'PaymentScheme': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consent_id"]) -> MetaOapg.properties.consent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_id"]) -> MetaOapg.properties.transaction_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["reference"], typing_extensions.Literal["bacs"], typing_extensions.Literal["amount"], typing_extensions.Literal["payment_id"], typing_extensions.Literal["iban"], typing_extensions.Literal["last_status_update"], typing_extensions.Literal["recipient_id"], typing_extensions.Literal["status"], typing_extensions.Literal["adjusted_reference"], typing_extensions.Literal["schedule"], typing_extensions.Literal["refund_details"], typing_extensions.Literal["refund_ids"], typing_extensions.Literal["amount_refunded"], typing_extensions.Literal["wallet_id"], typing_extensions.Literal["scheme"], typing_extensions.Literal["adjusted_scheme"], typing_extensions.Literal["consent_id"], typing_extensions.Literal["transaction_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bacs"]) -> 'SenderBACSNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'PaymentAmount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_id"]) -> MetaOapg.properties.payment_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_status_update"]) -> MetaOapg.properties.last_status_update: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient_id"]) -> MetaOapg.properties.recipient_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'PaymentInitiationPaymentStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adjusted_reference"]) -> typing.Union[MetaOapg.properties.adjusted_reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union['ExternalPaymentScheduleGet', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refund_details"]) -> typing.Union['ExternalPaymentRefundDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refund_ids"]) -> typing.Union[MetaOapg.properties.refund_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_refunded"]) -> typing.Union['PaymentAmountRefunded', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wallet_id"]) -> typing.Union[MetaOapg.properties.wallet_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheme"]) -> typing.Union['PaymentScheme', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adjusted_scheme"]) -> typing.Union['PaymentScheme', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consent_id"]) -> typing.Union[MetaOapg.properties.consent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_id"]) -> typing.Union[MetaOapg.properties.transaction_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reference"], typing_extensions.Literal["bacs"], typing_extensions.Literal["amount"], typing_extensions.Literal["payment_id"], typing_extensions.Literal["iban"], typing_extensions.Literal["last_status_update"], typing_extensions.Literal["recipient_id"], typing_extensions.Literal["status"], typing_extensions.Literal["adjusted_reference"], typing_extensions.Literal["schedule"], typing_extensions.Literal["refund_details"], typing_extensions.Literal["refund_ids"], typing_extensions.Literal["amount_refunded"], typing_extensions.Literal["wallet_id"], typing_extensions.Literal["scheme"], typing_extensions.Literal["adjusted_scheme"], typing_extensions.Literal["consent_id"], typing_extensions.Literal["transaction_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        reference: typing.Union[MetaOapg.properties.reference, str, ],
        bacs: 'SenderBACSNullable',
        amount: 'PaymentAmount',
        payment_id: typing.Union[MetaOapg.properties.payment_id, str, ],
        iban: typing.Union[MetaOapg.properties.iban, None, str, ],
        last_status_update: typing.Union[MetaOapg.properties.last_status_update, str, datetime, ],
        recipient_id: typing.Union[MetaOapg.properties.recipient_id, str, ],
        status: 'PaymentInitiationPaymentStatus',
        adjusted_reference: typing.Union[MetaOapg.properties.adjusted_reference, None, str, schemas.Unset] = schemas.unset,
        schedule: typing.Union['ExternalPaymentScheduleGet', schemas.Unset] = schemas.unset,
        refund_details: typing.Union['ExternalPaymentRefundDetails', schemas.Unset] = schemas.unset,
        refund_ids: typing.Union[MetaOapg.properties.refund_ids, list, tuple, None, schemas.Unset] = schemas.unset,
        amount_refunded: typing.Union['PaymentAmountRefunded', schemas.Unset] = schemas.unset,
        wallet_id: typing.Union[MetaOapg.properties.wallet_id, None, str, schemas.Unset] = schemas.unset,
        scheme: typing.Union['PaymentScheme', schemas.Unset] = schemas.unset,
        adjusted_scheme: typing.Union['PaymentScheme', schemas.Unset] = schemas.unset,
        consent_id: typing.Union[MetaOapg.properties.consent_id, None, str, schemas.Unset] = schemas.unset,
        transaction_id: typing.Union[MetaOapg.properties.transaction_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'PaymentInitiationPayment':
        return super().__new__(
            cls,
            *_args,
            reference=reference,
            bacs=bacs,
            amount=amount,
            payment_id=payment_id,
            iban=iban,
            last_status_update=last_status_update,
            recipient_id=recipient_id,
            status=status,
            adjusted_reference=adjusted_reference,
            schedule=schedule,
            refund_details=refund_details,
            refund_ids=refund_ids,
            amount_refunded=amount_refunded,
            wallet_id=wallet_id,
            scheme=scheme,
            adjusted_scheme=adjusted_scheme,
            consent_id=consent_id,
            transaction_id=transaction_id,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.external_payment_refund_details import ExternalPaymentRefundDetails
from plaid.model.external_payment_schedule_get import ExternalPaymentScheduleGet
from plaid.model.payment_amount import PaymentAmount
from plaid.model.payment_amount_refunded import PaymentAmountRefunded
from plaid.model.payment_initiation_payment_status import PaymentInitiationPaymentStatus
from plaid.model.payment_scheme import PaymentScheme
from plaid.model.sender_bacs_nullable import SenderBACSNullable