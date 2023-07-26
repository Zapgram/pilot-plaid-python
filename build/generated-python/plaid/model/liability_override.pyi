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


class LiabilityOverride(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Used to configure Sandbox test data for the Liabilities product
    """


    class MetaOapg:
        required = {
            "repayment_plan_description",
            "loan_status",
            "interest_capitalization_grace_period_months",
            "cash_apr",
            "payment_reference_number",
            "balance_transfer_apr",
            "repayment_plan_type",
            "repayment_model",
            "guarantor",
            "is_overdue",
            "type",
            "nominal_apr",
            "last_payment_amount",
            "expected_payoff_date",
            "principal",
            "sequence_number",
            "pslf_status",
            "origination_date",
            "special_apr",
            "is_federal",
            "servicer_address",
            "loan_name",
            "minimum_payment_amount",
            "purchase_apr",
        }
        
        class properties:
            type = schemas.StrSchema
            purchase_apr = schemas.Float64Schema
            cash_apr = schemas.Float64Schema
            balance_transfer_apr = schemas.Float64Schema
            special_apr = schemas.Float64Schema
            last_payment_amount = schemas.Float64Schema
            minimum_payment_amount = schemas.Float64Schema
            is_overdue = schemas.BoolSchema
            origination_date = schemas.DateSchema
            principal = schemas.Float64Schema
            nominal_apr = schemas.Float64Schema
            interest_capitalization_grace_period_months = schemas.NumberSchema
        
            @staticmethod
            def repayment_model() -> typing.Type['StudentLoanRepaymentModel']:
                return StudentLoanRepaymentModel
            expected_payoff_date = schemas.DateSchema
            guarantor = schemas.StrSchema
            is_federal = schemas.BoolSchema
            loan_name = schemas.StrSchema
        
            @staticmethod
            def loan_status() -> typing.Type['StudentLoanStatus']:
                return StudentLoanStatus
            payment_reference_number = schemas.StrSchema
        
            @staticmethod
            def pslf_status() -> typing.Type['PSLFStatus']:
                return PSLFStatus
            repayment_plan_description = schemas.StrSchema
            repayment_plan_type = schemas.StrSchema
            sequence_number = schemas.StrSchema
        
            @staticmethod
            def servicer_address() -> typing.Type['Address']:
                return Address
            __annotations__ = {
                "type": type,
                "purchase_apr": purchase_apr,
                "cash_apr": cash_apr,
                "balance_transfer_apr": balance_transfer_apr,
                "special_apr": special_apr,
                "last_payment_amount": last_payment_amount,
                "minimum_payment_amount": minimum_payment_amount,
                "is_overdue": is_overdue,
                "origination_date": origination_date,
                "principal": principal,
                "nominal_apr": nominal_apr,
                "interest_capitalization_grace_period_months": interest_capitalization_grace_period_months,
                "repayment_model": repayment_model,
                "expected_payoff_date": expected_payoff_date,
                "guarantor": guarantor,
                "is_federal": is_federal,
                "loan_name": loan_name,
                "loan_status": loan_status,
                "payment_reference_number": payment_reference_number,
                "pslf_status": pslf_status,
                "repayment_plan_description": repayment_plan_description,
                "repayment_plan_type": repayment_plan_type,
                "sequence_number": sequence_number,
                "servicer_address": servicer_address,
            }
        additional_properties = schemas.AnyTypeSchema
    
    repayment_plan_description: MetaOapg.properties.repayment_plan_description
    loan_status: 'StudentLoanStatus'
    interest_capitalization_grace_period_months: MetaOapg.properties.interest_capitalization_grace_period_months
    cash_apr: MetaOapg.properties.cash_apr
    payment_reference_number: MetaOapg.properties.payment_reference_number
    balance_transfer_apr: MetaOapg.properties.balance_transfer_apr
    repayment_plan_type: MetaOapg.properties.repayment_plan_type
    repayment_model: 'StudentLoanRepaymentModel'
    guarantor: MetaOapg.properties.guarantor
    is_overdue: MetaOapg.properties.is_overdue
    type: MetaOapg.properties.type
    nominal_apr: MetaOapg.properties.nominal_apr
    last_payment_amount: MetaOapg.properties.last_payment_amount
    expected_payoff_date: MetaOapg.properties.expected_payoff_date
    principal: MetaOapg.properties.principal
    sequence_number: MetaOapg.properties.sequence_number
    pslf_status: 'PSLFStatus'
    origination_date: MetaOapg.properties.origination_date
    special_apr: MetaOapg.properties.special_apr
    is_federal: MetaOapg.properties.is_federal
    servicer_address: 'Address'
    loan_name: MetaOapg.properties.loan_name
    minimum_payment_amount: MetaOapg.properties.minimum_payment_amount
    purchase_apr: MetaOapg.properties.purchase_apr
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repayment_plan_description"]) -> MetaOapg.properties.repayment_plan_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loan_status"]) -> 'StudentLoanStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interest_capitalization_grace_period_months"]) -> MetaOapg.properties.interest_capitalization_grace_period_months: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cash_apr"]) -> MetaOapg.properties.cash_apr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_reference_number"]) -> MetaOapg.properties.payment_reference_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance_transfer_apr"]) -> MetaOapg.properties.balance_transfer_apr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repayment_plan_type"]) -> MetaOapg.properties.repayment_plan_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repayment_model"]) -> 'StudentLoanRepaymentModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guarantor"]) -> MetaOapg.properties.guarantor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_overdue"]) -> MetaOapg.properties.is_overdue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nominal_apr"]) -> MetaOapg.properties.nominal_apr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_payment_amount"]) -> MetaOapg.properties.last_payment_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expected_payoff_date"]) -> MetaOapg.properties.expected_payoff_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["principal"]) -> MetaOapg.properties.principal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence_number"]) -> MetaOapg.properties.sequence_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pslf_status"]) -> 'PSLFStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origination_date"]) -> MetaOapg.properties.origination_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["special_apr"]) -> MetaOapg.properties.special_apr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_federal"]) -> MetaOapg.properties.is_federal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["servicer_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loan_name"]) -> MetaOapg.properties.loan_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_payment_amount"]) -> MetaOapg.properties.minimum_payment_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_apr"]) -> MetaOapg.properties.purchase_apr: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["repayment_plan_description"], typing_extensions.Literal["loan_status"], typing_extensions.Literal["interest_capitalization_grace_period_months"], typing_extensions.Literal["cash_apr"], typing_extensions.Literal["payment_reference_number"], typing_extensions.Literal["balance_transfer_apr"], typing_extensions.Literal["repayment_plan_type"], typing_extensions.Literal["repayment_model"], typing_extensions.Literal["guarantor"], typing_extensions.Literal["is_overdue"], typing_extensions.Literal["type"], typing_extensions.Literal["nominal_apr"], typing_extensions.Literal["last_payment_amount"], typing_extensions.Literal["expected_payoff_date"], typing_extensions.Literal["principal"], typing_extensions.Literal["sequence_number"], typing_extensions.Literal["pslf_status"], typing_extensions.Literal["origination_date"], typing_extensions.Literal["special_apr"], typing_extensions.Literal["is_federal"], typing_extensions.Literal["servicer_address"], typing_extensions.Literal["loan_name"], typing_extensions.Literal["minimum_payment_amount"], typing_extensions.Literal["purchase_apr"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repayment_plan_description"]) -> MetaOapg.properties.repayment_plan_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loan_status"]) -> 'StudentLoanStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interest_capitalization_grace_period_months"]) -> MetaOapg.properties.interest_capitalization_grace_period_months: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cash_apr"]) -> MetaOapg.properties.cash_apr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_reference_number"]) -> MetaOapg.properties.payment_reference_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance_transfer_apr"]) -> MetaOapg.properties.balance_transfer_apr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repayment_plan_type"]) -> MetaOapg.properties.repayment_plan_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repayment_model"]) -> 'StudentLoanRepaymentModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guarantor"]) -> MetaOapg.properties.guarantor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_overdue"]) -> MetaOapg.properties.is_overdue: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nominal_apr"]) -> MetaOapg.properties.nominal_apr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_payment_amount"]) -> MetaOapg.properties.last_payment_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expected_payoff_date"]) -> MetaOapg.properties.expected_payoff_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["principal"]) -> MetaOapg.properties.principal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence_number"]) -> MetaOapg.properties.sequence_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pslf_status"]) -> 'PSLFStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origination_date"]) -> MetaOapg.properties.origination_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["special_apr"]) -> MetaOapg.properties.special_apr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_federal"]) -> MetaOapg.properties.is_federal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["servicer_address"]) -> 'Address': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loan_name"]) -> MetaOapg.properties.loan_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_payment_amount"]) -> MetaOapg.properties.minimum_payment_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_apr"]) -> MetaOapg.properties.purchase_apr: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["repayment_plan_description"], typing_extensions.Literal["loan_status"], typing_extensions.Literal["interest_capitalization_grace_period_months"], typing_extensions.Literal["cash_apr"], typing_extensions.Literal["payment_reference_number"], typing_extensions.Literal["balance_transfer_apr"], typing_extensions.Literal["repayment_plan_type"], typing_extensions.Literal["repayment_model"], typing_extensions.Literal["guarantor"], typing_extensions.Literal["is_overdue"], typing_extensions.Literal["type"], typing_extensions.Literal["nominal_apr"], typing_extensions.Literal["last_payment_amount"], typing_extensions.Literal["expected_payoff_date"], typing_extensions.Literal["principal"], typing_extensions.Literal["sequence_number"], typing_extensions.Literal["pslf_status"], typing_extensions.Literal["origination_date"], typing_extensions.Literal["special_apr"], typing_extensions.Literal["is_federal"], typing_extensions.Literal["servicer_address"], typing_extensions.Literal["loan_name"], typing_extensions.Literal["minimum_payment_amount"], typing_extensions.Literal["purchase_apr"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        repayment_plan_description: typing.Union[MetaOapg.properties.repayment_plan_description, str, ],
        loan_status: 'StudentLoanStatus',
        interest_capitalization_grace_period_months: typing.Union[MetaOapg.properties.interest_capitalization_grace_period_months, decimal.Decimal, int, float, ],
        cash_apr: typing.Union[MetaOapg.properties.cash_apr, decimal.Decimal, int, float, ],
        payment_reference_number: typing.Union[MetaOapg.properties.payment_reference_number, str, ],
        balance_transfer_apr: typing.Union[MetaOapg.properties.balance_transfer_apr, decimal.Decimal, int, float, ],
        repayment_plan_type: typing.Union[MetaOapg.properties.repayment_plan_type, str, ],
        repayment_model: 'StudentLoanRepaymentModel',
        guarantor: typing.Union[MetaOapg.properties.guarantor, str, ],
        is_overdue: typing.Union[MetaOapg.properties.is_overdue, bool, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        nominal_apr: typing.Union[MetaOapg.properties.nominal_apr, decimal.Decimal, int, float, ],
        last_payment_amount: typing.Union[MetaOapg.properties.last_payment_amount, decimal.Decimal, int, float, ],
        expected_payoff_date: typing.Union[MetaOapg.properties.expected_payoff_date, str, date, ],
        principal: typing.Union[MetaOapg.properties.principal, decimal.Decimal, int, float, ],
        sequence_number: typing.Union[MetaOapg.properties.sequence_number, str, ],
        pslf_status: 'PSLFStatus',
        origination_date: typing.Union[MetaOapg.properties.origination_date, str, date, ],
        special_apr: typing.Union[MetaOapg.properties.special_apr, decimal.Decimal, int, float, ],
        is_federal: typing.Union[MetaOapg.properties.is_federal, bool, ],
        servicer_address: 'Address',
        loan_name: typing.Union[MetaOapg.properties.loan_name, str, ],
        minimum_payment_amount: typing.Union[MetaOapg.properties.minimum_payment_amount, decimal.Decimal, int, float, ],
        purchase_apr: typing.Union[MetaOapg.properties.purchase_apr, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'LiabilityOverride':
        return super().__new__(
            cls,
            *_args,
            repayment_plan_description=repayment_plan_description,
            loan_status=loan_status,
            interest_capitalization_grace_period_months=interest_capitalization_grace_period_months,
            cash_apr=cash_apr,
            payment_reference_number=payment_reference_number,
            balance_transfer_apr=balance_transfer_apr,
            repayment_plan_type=repayment_plan_type,
            repayment_model=repayment_model,
            guarantor=guarantor,
            is_overdue=is_overdue,
            type=type,
            nominal_apr=nominal_apr,
            last_payment_amount=last_payment_amount,
            expected_payoff_date=expected_payoff_date,
            principal=principal,
            sequence_number=sequence_number,
            pslf_status=pslf_status,
            origination_date=origination_date,
            special_apr=special_apr,
            is_federal=is_federal,
            servicer_address=servicer_address,
            loan_name=loan_name,
            minimum_payment_amount=minimum_payment_amount,
            purchase_apr=purchase_apr,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.address import Address
from plaid.model.pslf_status import PSLFStatus
from plaid.model.student_loan_repayment_model import StudentLoanRepaymentModel
from plaid.model.student_loan_status import StudentLoanStatus
