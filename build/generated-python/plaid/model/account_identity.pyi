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


class AccountIdentity(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Identity information about an account
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "owners",
                }
                
                class properties:
                    
                    
                    class owners(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Owner']:
                                return Owner
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['Owner'], typing.List['Owner']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'owners':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Owner':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "owners": owners,
                    }
                additional_properties = schemas.AnyTypeSchema
            
            owners: MetaOapg.properties.owners
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["owners"], str, ]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["owners"]) -> MetaOapg.properties.owners: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["owners"], str, ]):
                return super().get_item_oapg(name)
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                owners: typing.Union[MetaOapg.properties.owners, list, tuple, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    owners=owners,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                AccountBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountIdentity':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.account_base import AccountBase
from plaid.model.owner import Owner