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


class DepositSwitchGetResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    DepositSwitchGetResponse defines the response schema for `/deposit_switch/get`
    """


    class MetaOapg:
        required = {
            "is_allocated_remainder",
            "percent_allocated",
            "date_created",
            "target_account_id",
            "account_has_multiple_allocations",
            "date_completed",
            "state",
            "target_item_id",
            "amount_allocated",
            "deposit_switch_id",
            "request_id",
        }
        
        class properties:
            deposit_switch_id = schemas.StrSchema
            
            
            class target_account_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'target_account_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class target_item_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'target_item_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INITIALIZED(cls):
                    return cls("initialized")
                
                @schemas.classproperty
                def PROCESSING(cls):
                    return cls("processing")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("completed")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("error")
            
            
            class account_has_multiple_allocations(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_has_multiple_allocations':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class is_allocated_remainder(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_allocated_remainder':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class percent_allocated(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'percent_allocated':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class amount_allocated(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'amount_allocated':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            date_created = schemas.DateSchema
            
            
            class date_completed(
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
                ) -> 'date_completed':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            request_id = schemas.StrSchema
            
            
            class switch_method(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "instant": "INSTANT",
                        "mail": "MAIL",
                        "pdf": "PDF",
                        schemas.NoneClass.NONE: "NONE",
                    }
                
                @schemas.classproperty
                def INSTANT(cls):
                    return cls("instant")
                
                @schemas.classproperty
                def MAIL(cls):
                    return cls("mail")
                
                @schemas.classproperty
                def PDF(cls):
                    return cls("pdf")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'switch_method':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class employer_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employer_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class employer_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employer_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class institution_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'institution_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class institution_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'institution_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "deposit_switch_id": deposit_switch_id,
                "target_account_id": target_account_id,
                "target_item_id": target_item_id,
                "state": state,
                "account_has_multiple_allocations": account_has_multiple_allocations,
                "is_allocated_remainder": is_allocated_remainder,
                "percent_allocated": percent_allocated,
                "amount_allocated": amount_allocated,
                "date_created": date_created,
                "date_completed": date_completed,
                "request_id": request_id,
                "switch_method": switch_method,
                "employer_name": employer_name,
                "employer_id": employer_id,
                "institution_name": institution_name,
                "institution_id": institution_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    is_allocated_remainder: MetaOapg.properties.is_allocated_remainder
    percent_allocated: MetaOapg.properties.percent_allocated
    date_created: MetaOapg.properties.date_created
    target_account_id: MetaOapg.properties.target_account_id
    account_has_multiple_allocations: MetaOapg.properties.account_has_multiple_allocations
    date_completed: MetaOapg.properties.date_completed
    state: MetaOapg.properties.state
    target_item_id: MetaOapg.properties.target_item_id
    amount_allocated: MetaOapg.properties.amount_allocated
    deposit_switch_id: MetaOapg.properties.deposit_switch_id
    request_id: MetaOapg.properties.request_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_allocated_remainder"]) -> MetaOapg.properties.is_allocated_remainder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percent_allocated"]) -> MetaOapg.properties.percent_allocated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_account_id"]) -> MetaOapg.properties.target_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_has_multiple_allocations"]) -> MetaOapg.properties.account_has_multiple_allocations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_completed"]) -> MetaOapg.properties.date_completed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_item_id"]) -> MetaOapg.properties.target_item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_allocated"]) -> MetaOapg.properties.amount_allocated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deposit_switch_id"]) -> MetaOapg.properties.deposit_switch_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["switch_method"]) -> MetaOapg.properties.switch_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer_name"]) -> MetaOapg.properties.employer_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer_id"]) -> MetaOapg.properties.employer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution_name"]) -> MetaOapg.properties.institution_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution_id"]) -> MetaOapg.properties.institution_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_allocated_remainder"], typing_extensions.Literal["percent_allocated"], typing_extensions.Literal["date_created"], typing_extensions.Literal["target_account_id"], typing_extensions.Literal["account_has_multiple_allocations"], typing_extensions.Literal["date_completed"], typing_extensions.Literal["state"], typing_extensions.Literal["target_item_id"], typing_extensions.Literal["amount_allocated"], typing_extensions.Literal["deposit_switch_id"], typing_extensions.Literal["request_id"], typing_extensions.Literal["switch_method"], typing_extensions.Literal["employer_name"], typing_extensions.Literal["employer_id"], typing_extensions.Literal["institution_name"], typing_extensions.Literal["institution_id"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_allocated_remainder"]) -> MetaOapg.properties.is_allocated_remainder: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percent_allocated"]) -> MetaOapg.properties.percent_allocated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_account_id"]) -> MetaOapg.properties.target_account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_has_multiple_allocations"]) -> MetaOapg.properties.account_has_multiple_allocations: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_completed"]) -> MetaOapg.properties.date_completed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_item_id"]) -> MetaOapg.properties.target_item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_allocated"]) -> MetaOapg.properties.amount_allocated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deposit_switch_id"]) -> MetaOapg.properties.deposit_switch_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["switch_method"]) -> typing.Union[MetaOapg.properties.switch_method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer_name"]) -> typing.Union[MetaOapg.properties.employer_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer_id"]) -> typing.Union[MetaOapg.properties.employer_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution_name"]) -> typing.Union[MetaOapg.properties.institution_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution_id"]) -> typing.Union[MetaOapg.properties.institution_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_allocated_remainder"], typing_extensions.Literal["percent_allocated"], typing_extensions.Literal["date_created"], typing_extensions.Literal["target_account_id"], typing_extensions.Literal["account_has_multiple_allocations"], typing_extensions.Literal["date_completed"], typing_extensions.Literal["state"], typing_extensions.Literal["target_item_id"], typing_extensions.Literal["amount_allocated"], typing_extensions.Literal["deposit_switch_id"], typing_extensions.Literal["request_id"], typing_extensions.Literal["switch_method"], typing_extensions.Literal["employer_name"], typing_extensions.Literal["employer_id"], typing_extensions.Literal["institution_name"], typing_extensions.Literal["institution_id"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_allocated_remainder: typing.Union[MetaOapg.properties.is_allocated_remainder, None, bool, ],
        percent_allocated: typing.Union[MetaOapg.properties.percent_allocated, None, decimal.Decimal, int, float, ],
        date_created: typing.Union[MetaOapg.properties.date_created, str, date, ],
        target_account_id: typing.Union[MetaOapg.properties.target_account_id, None, str, ],
        account_has_multiple_allocations: typing.Union[MetaOapg.properties.account_has_multiple_allocations, None, bool, ],
        date_completed: typing.Union[MetaOapg.properties.date_completed, None, str, date, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        target_item_id: typing.Union[MetaOapg.properties.target_item_id, None, str, ],
        amount_allocated: typing.Union[MetaOapg.properties.amount_allocated, None, decimal.Decimal, int, float, ],
        deposit_switch_id: typing.Union[MetaOapg.properties.deposit_switch_id, str, ],
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        switch_method: typing.Union[MetaOapg.properties.switch_method, None, str, schemas.Unset] = schemas.unset,
        employer_name: typing.Union[MetaOapg.properties.employer_name, None, str, schemas.Unset] = schemas.unset,
        employer_id: typing.Union[MetaOapg.properties.employer_id, None, str, schemas.Unset] = schemas.unset,
        institution_name: typing.Union[MetaOapg.properties.institution_name, None, str, schemas.Unset] = schemas.unset,
        institution_id: typing.Union[MetaOapg.properties.institution_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'DepositSwitchGetResponse':
        return super().__new__(
            cls,
            *_args,
            is_allocated_remainder=is_allocated_remainder,
            percent_allocated=percent_allocated,
            date_created=date_created,
            target_account_id=target_account_id,
            account_has_multiple_allocations=account_has_multiple_allocations,
            date_completed=date_completed,
            state=state,
            target_item_id=target_item_id,
            amount_allocated=amount_allocated,
            deposit_switch_id=deposit_switch_id,
            request_id=request_id,
            switch_method=switch_method,
            employer_name=employer_name,
            employer_id=employer_id,
            institution_name=institution_name,
            institution_id=institution_id,
            _configuration=_configuration,
            **kwargs,
        )
