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


class LinkTokenCreateRequestUser(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object specifying information about the end user who will be linking their account.
    """


    class MetaOapg:
        required = {
            "client_user_id",
        }
        
        class properties:
            client_user_id = schemas.StrSchema
            legal_name = schemas.StrSchema
            
            
            class name(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
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
                            IdentityVerificationRequestUserName,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            phone_number = schemas.StrSchema
            
            
            class phone_number_verified_time(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phone_number_verified_time':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            email_address = schemas.StrSchema
            
            
            class email_address_verified_time(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email_address_verified_time':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            ssn = schemas.StrSchema
            
            
            class date_of_birth(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'date_of_birth':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class address(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
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
                            UserAddress,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'address':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class id_number(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
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
                            UserIDNumber,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'id_number':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "client_user_id": client_user_id,
                "legal_name": legal_name,
                "name": name,
                "phone_number": phone_number,
                "phone_number_verified_time": phone_number_verified_time,
                "email_address": email_address,
                "email_address_verified_time": email_address_verified_time,
                "ssn": ssn,
                "date_of_birth": date_of_birth,
                "address": address,
                "id_number": id_number,
            }
    
    client_user_id: MetaOapg.properties.client_user_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_user_id"]) -> MetaOapg.properties.client_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legal_name"]) -> MetaOapg.properties.legal_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number_verified_time"]) -> MetaOapg.properties.phone_number_verified_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> MetaOapg.properties.email_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address_verified_time"]) -> MetaOapg.properties.email_address_verified_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_of_birth"]) -> MetaOapg.properties.date_of_birth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id_number"]) -> MetaOapg.properties.id_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_user_id", "legal_name", "name", "phone_number", "phone_number_verified_time", "email_address", "email_address_verified_time", "ssn", "date_of_birth", "address", "id_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_user_id"]) -> MetaOapg.properties.client_user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legal_name"]) -> typing.Union[MetaOapg.properties.legal_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number_verified_time"]) -> typing.Union[MetaOapg.properties.phone_number_verified_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> typing.Union[MetaOapg.properties.email_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address_verified_time"]) -> typing.Union[MetaOapg.properties.email_address_verified_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> typing.Union[MetaOapg.properties.ssn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_of_birth"]) -> typing.Union[MetaOapg.properties.date_of_birth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id_number"]) -> typing.Union[MetaOapg.properties.id_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_user_id", "legal_name", "name", "phone_number", "phone_number_verified_time", "email_address", "email_address_verified_time", "ssn", "date_of_birth", "address", "id_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        client_user_id: typing.Union[MetaOapg.properties.client_user_id, str, ],
        legal_name: typing.Union[MetaOapg.properties.legal_name, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
        phone_number_verified_time: typing.Union[MetaOapg.properties.phone_number_verified_time, None, str, datetime, schemas.Unset] = schemas.unset,
        email_address: typing.Union[MetaOapg.properties.email_address, str, schemas.Unset] = schemas.unset,
        email_address_verified_time: typing.Union[MetaOapg.properties.email_address_verified_time, None, str, datetime, schemas.Unset] = schemas.unset,
        ssn: typing.Union[MetaOapg.properties.ssn, str, schemas.Unset] = schemas.unset,
        date_of_birth: typing.Union[MetaOapg.properties.date_of_birth, None, str, date, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        id_number: typing.Union[MetaOapg.properties.id_number, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LinkTokenCreateRequestUser':
        return super().__new__(
            cls,
            *_args,
            client_user_id=client_user_id,
            legal_name=legal_name,
            name=name,
            phone_number=phone_number,
            phone_number_verified_time=phone_number_verified_time,
            email_address=email_address,
            email_address_verified_time=email_address_verified_time,
            ssn=ssn,
            date_of_birth=date_of_birth,
            address=address,
            id_number=id_number,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.identity_verification_request_user_name import IdentityVerificationRequestUserName
from plaid.model.user_address import UserAddress
from plaid.model.user_id_number import UserIDNumber