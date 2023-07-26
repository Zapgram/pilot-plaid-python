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


class PaymentInitiationPaymentStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The status of the payment.

`PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.

`PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution. For successful payments, this is a potential terminal status. Further status transitions can be to REJECTED and, when supported by the institution, to EXECUTED.

`PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.

`PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error may be caused by transient system outages and is retryable once the root cause is resolved.

`PAYMENT_STATUS_BLOCKED`: The payment has been blocked by Plaid. This can occur, for example, due to Plaid flagging the payment as potentially risky. This is a retryable error.

`PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.

`PAYMENT_STATUS_CANCELLED`: The payment was cancelled (typically by the end user) during authorisation.

`PAYMENT_STATUS_EXECUTED`: The funds have successfully left the payer account and payment is considered complete. Not all institutions support this status: support is more common in the UK, and less common in the EU. For institutions where this status is not supported, the terminal status for a successful payment will be `PAYMENT_STATUS_INITIATED`.

`PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. A payment will typically settle within seconds to several days, depending on which payment rail is used. This status is only available to customers using [Plaid Virtual Accounts](https://plaid.com/docs/virtual-accounts/).

`PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.

`PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.

Deprecated:
These statuses will be removed in a future release.

`PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.

`PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.

`PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.
    """


    class MetaOapg:
        enum_value_to_name = {
            "PAYMENT_STATUS_INPUT_NEEDED": "INPUT_NEEDED",
            "PAYMENT_STATUS_PROCESSING": "PROCESSING",
            "PAYMENT_STATUS_INITIATED": "INITIATED",
            "PAYMENT_STATUS_COMPLETED": "COMPLETED",
            "PAYMENT_STATUS_INSUFFICIENT_FUNDS": "INSUFFICIENT_FUNDS",
            "PAYMENT_STATUS_FAILED": "FAILED",
            "PAYMENT_STATUS_BLOCKED": "BLOCKED",
            "PAYMENT_STATUS_UNKNOWN": "UNKNOWN",
            "PAYMENT_STATUS_EXECUTED": "EXECUTED",
            "PAYMENT_STATUS_SETTLED": "SETTLED",
            "PAYMENT_STATUS_AUTHORISING": "AUTHORISING",
            "PAYMENT_STATUS_CANCELLED": "CANCELLED",
            "PAYMENT_STATUS_ESTABLISHED": "ESTABLISHED",
            "PAYMENT_STATUS_REJECTED": "REJECTED",
        }
    
    @schemas.classproperty
    def INPUT_NEEDED(cls):
        return cls("PAYMENT_STATUS_INPUT_NEEDED")
    
    @schemas.classproperty
    def PROCESSING(cls):
        return cls("PAYMENT_STATUS_PROCESSING")
    
    @schemas.classproperty
    def INITIATED(cls):
        return cls("PAYMENT_STATUS_INITIATED")
    
    @schemas.classproperty
    def COMPLETED(cls):
        return cls("PAYMENT_STATUS_COMPLETED")
    
    @schemas.classproperty
    def INSUFFICIENT_FUNDS(cls):
        return cls("PAYMENT_STATUS_INSUFFICIENT_FUNDS")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("PAYMENT_STATUS_FAILED")
    
    @schemas.classproperty
    def BLOCKED(cls):
        return cls("PAYMENT_STATUS_BLOCKED")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("PAYMENT_STATUS_UNKNOWN")
    
    @schemas.classproperty
    def EXECUTED(cls):
        return cls("PAYMENT_STATUS_EXECUTED")
    
    @schemas.classproperty
    def SETTLED(cls):
        return cls("PAYMENT_STATUS_SETTLED")
    
    @schemas.classproperty
    def AUTHORISING(cls):
        return cls("PAYMENT_STATUS_AUTHORISING")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("PAYMENT_STATUS_CANCELLED")
    
    @schemas.classproperty
    def ESTABLISHED(cls):
        return cls("PAYMENT_STATUS_ESTABLISHED")
    
    @schemas.classproperty
    def REJECTED(cls):
        return cls("PAYMENT_STATUS_REJECTED")
