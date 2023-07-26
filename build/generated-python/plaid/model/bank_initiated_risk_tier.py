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


class BankInitiatedRiskTier(
    schemas.IntSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    In the `bank_initiated_return_risk` object, there are eight risk tiers corresponding to the scores:
  1: Predicted bank-initiated return incidence rate between 0.0% - 0.5%
  2: Predicted bank-initiated return incidence rate between 0.5% - 1.5%
  3: Predicted bank-initiated return incidence rate between 1.5% - 3%
  4: Predicted bank-initiated return incidence rate between 3% - 5%
  5: Predicted bank-initiated return incidence rate between 5% - 10%
  6: Predicted bank-initiated return incidence rate between 10% - 15%
  7: Predicted bank-initiated return incidence rate between 15% and 50%
  8: Predicted bank-initiated return incidence rate greater than 50%

    """


    class MetaOapg:
        inclusive_maximum = 8
        inclusive_minimum = 1
