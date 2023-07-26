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


class InvestmentsAuthGetResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    InvestmentsAuthGetResponse defines the response schema for `/investments/auth/get`
    """


    class MetaOapg:
        required = {
            "item",
            "numbers",
            "owners",
            "accounts",
            "holdings",
            "request_id",
            "securities",
        }
        
        class properties:
            
            
            class accounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccountBase']:
                        return AccountBase
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AccountBase'], typing.List['AccountBase']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccountBase':
                    return super().__getitem__(i)
            
            
            class holdings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Holding']:
                        return Holding
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Holding'], typing.List['Holding']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'holdings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Holding':
                    return super().__getitem__(i)
            
            
            class securities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Security']:
                        return Security
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Security'], typing.List['Security']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'securities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Security':
                    return super().__getitem__(i)
            
            
            class owners(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['InvestmentsAuthOwner']:
                        return InvestmentsAuthOwner
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['InvestmentsAuthOwner'], typing.List['InvestmentsAuthOwner']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'owners':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'InvestmentsAuthOwner':
                    return super().__getitem__(i)
        
            @staticmethod
            def numbers() -> typing.Type['InvestmentsAuthGetNumbers']:
                return InvestmentsAuthGetNumbers
        
            @staticmethod
            def item() -> typing.Type['Item']:
                return Item
            request_id = schemas.StrSchema
            __annotations__ = {
                "accounts": accounts,
                "holdings": holdings,
                "securities": securities,
                "owners": owners,
                "numbers": numbers,
                "item": item,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    item: 'Item'
    numbers: 'InvestmentsAuthGetNumbers'
    owners: MetaOapg.properties.owners
    accounts: MetaOapg.properties.accounts
    holdings: MetaOapg.properties.holdings
    request_id: MetaOapg.properties.request_id
    securities: MetaOapg.properties.securities
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item"]) -> 'Item': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numbers"]) -> 'InvestmentsAuthGetNumbers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holdings"]) -> MetaOapg.properties.holdings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securities"]) -> MetaOapg.properties.securities: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["item"], typing_extensions.Literal["numbers"], typing_extensions.Literal["owners"], typing_extensions.Literal["accounts"], typing_extensions.Literal["holdings"], typing_extensions.Literal["request_id"], typing_extensions.Literal["securities"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item"]) -> 'Item': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numbers"]) -> 'InvestmentsAuthGetNumbers': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holdings"]) -> MetaOapg.properties.holdings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securities"]) -> MetaOapg.properties.securities: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["item"], typing_extensions.Literal["numbers"], typing_extensions.Literal["owners"], typing_extensions.Literal["accounts"], typing_extensions.Literal["holdings"], typing_extensions.Literal["request_id"], typing_extensions.Literal["securities"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        item: 'Item',
        numbers: 'InvestmentsAuthGetNumbers',
        owners: typing.Union[MetaOapg.properties.owners, list, tuple, ],
        accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, ],
        holdings: typing.Union[MetaOapg.properties.holdings, list, tuple, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        securities: typing.Union[MetaOapg.properties.securities, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'InvestmentsAuthGetResponse':
        return super().__new__(
            cls,
            *_args,
            item=item,
            numbers=numbers,
            owners=owners,
            accounts=accounts,
            holdings=holdings,
            request_id=request_id,
            securities=securities,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.account_base import AccountBase
from plaid.model.holding import Holding
from plaid.model.investments_auth_get_numbers import InvestmentsAuthGetNumbers
from plaid.model.investments_auth_owner import InvestmentsAuthOwner
from plaid.model.item import Item
from plaid.model.security import Security