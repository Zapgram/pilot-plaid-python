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


class InvestmentTransactionSubtype(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).
    """


    class MetaOapg:
        enum_value_to_name = {
            "account fee": "ACCOUNT_FEE",
            "adjustment": "ADJUSTMENT",
            "assignment": "ASSIGNMENT",
            "buy": "BUY",
            "buy to cover": "BUY_TO_COVER",
            "contribution": "CONTRIBUTION",
            "deposit": "DEPOSIT",
            "distribution": "DISTRIBUTION",
            "dividend": "DIVIDEND",
            "dividend reinvestment": "DIVIDEND_REINVESTMENT",
            "exercise": "EXERCISE",
            "expire": "EXPIRE",
            "fund fee": "FUND_FEE",
            "interest": "INTEREST",
            "interest receivable": "INTEREST_RECEIVABLE",
            "interest reinvestment": "INTEREST_REINVESTMENT",
            "legal fee": "LEGAL_FEE",
            "loan payment": "LOAN_PAYMENT",
            "long-term capital gain": "LONGTERM_CAPITAL_GAIN",
            "long-term capital gain reinvestment": "LONGTERM_CAPITAL_GAIN_REINVESTMENT",
            "management fee": "MANAGEMENT_FEE",
            "margin expense": "MARGIN_EXPENSE",
            "merger": "MERGER",
            "miscellaneous fee": "MISCELLANEOUS_FEE",
            "non-qualified dividend": "NONQUALIFIED_DIVIDEND",
            "non-resident tax": "NONRESIDENT_TAX",
            "pending credit": "PENDING_CREDIT",
            "pending debit": "PENDING_DEBIT",
            "qualified dividend": "QUALIFIED_DIVIDEND",
            "rebalance": "REBALANCE",
            "return of principal": "RETURN_OF_PRINCIPAL",
            "request": "REQUEST",
            "sell": "SELL",
            "sell short": "SELL_SHORT",
            "send": "SEND",
            "short-term capital gain": "SHORTTERM_CAPITAL_GAIN",
            "short-term capital gain reinvestment": "SHORTTERM_CAPITAL_GAIN_REINVESTMENT",
            "spin off": "SPIN_OFF",
            "split": "SPLIT",
            "stock distribution": "STOCK_DISTRIBUTION",
            "tax": "TAX",
            "tax withheld": "TAX_WITHHELD",
            "trade": "TRADE",
            "transfer": "TRANSFER",
            "transfer fee": "TRANSFER_FEE",
            "trust fee": "TRUST_FEE",
            "unqualified gain": "UNQUALIFIED_GAIN",
            "withdrawal": "WITHDRAWAL",
        }
    
    @schemas.classproperty
    def ACCOUNT_FEE(cls):
        return cls("account fee")
    
    @schemas.classproperty
    def ADJUSTMENT(cls):
        return cls("adjustment")
    
    @schemas.classproperty
    def ASSIGNMENT(cls):
        return cls("assignment")
    
    @schemas.classproperty
    def BUY(cls):
        return cls("buy")
    
    @schemas.classproperty
    def BUY_TO_COVER(cls):
        return cls("buy to cover")
    
    @schemas.classproperty
    def CONTRIBUTION(cls):
        return cls("contribution")
    
    @schemas.classproperty
    def DEPOSIT(cls):
        return cls("deposit")
    
    @schemas.classproperty
    def DISTRIBUTION(cls):
        return cls("distribution")
    
    @schemas.classproperty
    def DIVIDEND(cls):
        return cls("dividend")
    
    @schemas.classproperty
    def DIVIDEND_REINVESTMENT(cls):
        return cls("dividend reinvestment")
    
    @schemas.classproperty
    def EXERCISE(cls):
        return cls("exercise")
    
    @schemas.classproperty
    def EXPIRE(cls):
        return cls("expire")
    
    @schemas.classproperty
    def FUND_FEE(cls):
        return cls("fund fee")
    
    @schemas.classproperty
    def INTEREST(cls):
        return cls("interest")
    
    @schemas.classproperty
    def INTEREST_RECEIVABLE(cls):
        return cls("interest receivable")
    
    @schemas.classproperty
    def INTEREST_REINVESTMENT(cls):
        return cls("interest reinvestment")
    
    @schemas.classproperty
    def LEGAL_FEE(cls):
        return cls("legal fee")
    
    @schemas.classproperty
    def LOAN_PAYMENT(cls):
        return cls("loan payment")
    
    @schemas.classproperty
    def LONGTERM_CAPITAL_GAIN(cls):
        return cls("long-term capital gain")
    
    @schemas.classproperty
    def LONGTERM_CAPITAL_GAIN_REINVESTMENT(cls):
        return cls("long-term capital gain reinvestment")
    
    @schemas.classproperty
    def MANAGEMENT_FEE(cls):
        return cls("management fee")
    
    @schemas.classproperty
    def MARGIN_EXPENSE(cls):
        return cls("margin expense")
    
    @schemas.classproperty
    def MERGER(cls):
        return cls("merger")
    
    @schemas.classproperty
    def MISCELLANEOUS_FEE(cls):
        return cls("miscellaneous fee")
    
    @schemas.classproperty
    def NONQUALIFIED_DIVIDEND(cls):
        return cls("non-qualified dividend")
    
    @schemas.classproperty
    def NONRESIDENT_TAX(cls):
        return cls("non-resident tax")
    
    @schemas.classproperty
    def PENDING_CREDIT(cls):
        return cls("pending credit")
    
    @schemas.classproperty
    def PENDING_DEBIT(cls):
        return cls("pending debit")
    
    @schemas.classproperty
    def QUALIFIED_DIVIDEND(cls):
        return cls("qualified dividend")
    
    @schemas.classproperty
    def REBALANCE(cls):
        return cls("rebalance")
    
    @schemas.classproperty
    def RETURN_OF_PRINCIPAL(cls):
        return cls("return of principal")
    
    @schemas.classproperty
    def REQUEST(cls):
        return cls("request")
    
    @schemas.classproperty
    def SELL(cls):
        return cls("sell")
    
    @schemas.classproperty
    def SELL_SHORT(cls):
        return cls("sell short")
    
    @schemas.classproperty
    def SEND(cls):
        return cls("send")
    
    @schemas.classproperty
    def SHORTTERM_CAPITAL_GAIN(cls):
        return cls("short-term capital gain")
    
    @schemas.classproperty
    def SHORTTERM_CAPITAL_GAIN_REINVESTMENT(cls):
        return cls("short-term capital gain reinvestment")
    
    @schemas.classproperty
    def SPIN_OFF(cls):
        return cls("spin off")
    
    @schemas.classproperty
    def SPLIT(cls):
        return cls("split")
    
    @schemas.classproperty
    def STOCK_DISTRIBUTION(cls):
        return cls("stock distribution")
    
    @schemas.classproperty
    def TAX(cls):
        return cls("tax")
    
    @schemas.classproperty
    def TAX_WITHHELD(cls):
        return cls("tax withheld")
    
    @schemas.classproperty
    def TRADE(cls):
        return cls("trade")
    
    @schemas.classproperty
    def TRANSFER(cls):
        return cls("transfer")
    
    @schemas.classproperty
    def TRANSFER_FEE(cls):
        return cls("transfer fee")
    
    @schemas.classproperty
    def TRUST_FEE(cls):
        return cls("trust fee")
    
    @schemas.classproperty
    def UNQUALIFIED_GAIN(cls):
        return cls("unqualified gain")
    
    @schemas.classproperty
    def WITHDRAWAL(cls):
        return cls("withdrawal")