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


class TransactionsGetRequestOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An optional object to be used with the request. If specified, `options` must not be `null`.
    """


    class MetaOapg:
        
        class properties:
            
            
            class account_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class count(
                schemas.IntSchema
            ):
                pass
            
            
            class offset(
                schemas.IntSchema
            ):
                pass
            
            
            class include_original_description(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'include_original_description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            include_personal_finance_category_beta = schemas.BoolSchema
            include_personal_finance_category = schemas.BoolSchema
            include_logo_and_counterparty_beta = schemas.BoolSchema
            __annotations__ = {
                "account_ids": account_ids,
                "count": count,
                "offset": offset,
                "include_original_description": include_original_description,
                "include_personal_finance_category_beta": include_personal_finance_category_beta,
                "include_personal_finance_category": include_personal_finance_category,
                "include_logo_and_counterparty_beta": include_logo_and_counterparty_beta,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_ids"]) -> MetaOapg.properties.account_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_original_description"]) -> MetaOapg.properties.include_original_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_personal_finance_category_beta"]) -> MetaOapg.properties.include_personal_finance_category_beta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_personal_finance_category"]) -> MetaOapg.properties.include_personal_finance_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_logo_and_counterparty_beta"]) -> MetaOapg.properties.include_logo_and_counterparty_beta: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_ids", "count", "offset", "include_original_description", "include_personal_finance_category_beta", "include_personal_finance_category", "include_logo_and_counterparty_beta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_ids"]) -> typing.Union[MetaOapg.properties.account_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> typing.Union[MetaOapg.properties.offset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_original_description"]) -> typing.Union[MetaOapg.properties.include_original_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_personal_finance_category_beta"]) -> typing.Union[MetaOapg.properties.include_personal_finance_category_beta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_personal_finance_category"]) -> typing.Union[MetaOapg.properties.include_personal_finance_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_logo_and_counterparty_beta"]) -> typing.Union[MetaOapg.properties.include_logo_and_counterparty_beta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_ids", "count", "offset", "include_original_description", "include_personal_finance_category_beta", "include_personal_finance_category", "include_logo_and_counterparty_beta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        account_ids: typing.Union[MetaOapg.properties.account_ids, list, tuple, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        include_original_description: typing.Union[MetaOapg.properties.include_original_description, None, bool, schemas.Unset] = schemas.unset,
        include_personal_finance_category_beta: typing.Union[MetaOapg.properties.include_personal_finance_category_beta, bool, schemas.Unset] = schemas.unset,
        include_personal_finance_category: typing.Union[MetaOapg.properties.include_personal_finance_category, bool, schemas.Unset] = schemas.unset,
        include_logo_and_counterparty_beta: typing.Union[MetaOapg.properties.include_logo_and_counterparty_beta, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionsGetRequestOptions':
        return super().__new__(
            cls,
            *_args,
            account_ids=account_ids,
            count=count,
            offset=offset,
            include_original_description=include_original_description,
            include_personal_finance_category_beta=include_personal_finance_category_beta,
            include_personal_finance_category=include_personal_finance_category,
            include_logo_and_counterparty_beta=include_logo_and_counterparty_beta,
            _configuration=_configuration,
            **kwargs,
        )
