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


class Enrichments(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A grouping of the Plaid produced transaction enrichment fields.
    """


    class MetaOapg:
        required = {
            "personal_finance_category_icon_url",
            "website",
            "logo_url",
            "payment_channel",
            "merchant_name",
            "location",
            "counterparties",
            "personal_finance_category",
        }
        
        class properties:
            
            
            class counterparties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Counterparty']:
                        return Counterparty
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Counterparty'], typing.List['Counterparty']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'counterparties':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Counterparty':
                    return super().__getitem__(i)
        
            @staticmethod
            def location() -> typing.Type['Location']:
                return Location
            
            
            class logo_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'logo_url':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class merchant_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'merchant_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def payment_channel() -> typing.Type['PaymentChannel']:
                return PaymentChannel
        
            @staticmethod
            def personal_finance_category() -> typing.Type['PersonalFinanceCategory']:
                return PersonalFinanceCategory
            personal_finance_category_icon_url = schemas.StrSchema
            
            
            class website(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'website':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class check_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'check_number':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class entity_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entity_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class legacy_category_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'legacy_category_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class legacy_category(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'legacy_category':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def recurrence() -> typing.Type['Recurrence']:
                return Recurrence
            __annotations__ = {
                "counterparties": counterparties,
                "location": location,
                "logo_url": logo_url,
                "merchant_name": merchant_name,
                "payment_channel": payment_channel,
                "personal_finance_category": personal_finance_category,
                "personal_finance_category_icon_url": personal_finance_category_icon_url,
                "website": website,
                "check_number": check_number,
                "entity_id": entity_id,
                "legacy_category_id": legacy_category_id,
                "legacy_category": legacy_category,
                "recurrence": recurrence,
            }
        additional_properties = schemas.AnyTypeSchema
    
    personal_finance_category_icon_url: MetaOapg.properties.personal_finance_category_icon_url
    website: MetaOapg.properties.website
    logo_url: MetaOapg.properties.logo_url
    payment_channel: 'PaymentChannel'
    merchant_name: MetaOapg.properties.merchant_name
    location: 'Location'
    counterparties: MetaOapg.properties.counterparties
    personal_finance_category: 'PersonalFinanceCategory'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_finance_category_icon_url"]) -> MetaOapg.properties.personal_finance_category_icon_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_url"]) -> MetaOapg.properties.logo_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_channel"]) -> 'PaymentChannel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_name"]) -> MetaOapg.properties.merchant_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> 'Location': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["counterparties"]) -> MetaOapg.properties.counterparties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_finance_category"]) -> 'PersonalFinanceCategory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["check_number"]) -> MetaOapg.properties.check_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_id"]) -> MetaOapg.properties.entity_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legacy_category_id"]) -> MetaOapg.properties.legacy_category_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legacy_category"]) -> MetaOapg.properties.legacy_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurrence"]) -> 'Recurrence': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["personal_finance_category_icon_url"], typing_extensions.Literal["website"], typing_extensions.Literal["logo_url"], typing_extensions.Literal["payment_channel"], typing_extensions.Literal["merchant_name"], typing_extensions.Literal["location"], typing_extensions.Literal["counterparties"], typing_extensions.Literal["personal_finance_category"], typing_extensions.Literal["check_number"], typing_extensions.Literal["entity_id"], typing_extensions.Literal["legacy_category_id"], typing_extensions.Literal["legacy_category"], typing_extensions.Literal["recurrence"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_finance_category_icon_url"]) -> MetaOapg.properties.personal_finance_category_icon_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_url"]) -> MetaOapg.properties.logo_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_channel"]) -> 'PaymentChannel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_name"]) -> MetaOapg.properties.merchant_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> 'Location': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["counterparties"]) -> MetaOapg.properties.counterparties: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_finance_category"]) -> 'PersonalFinanceCategory': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["check_number"]) -> typing.Union[MetaOapg.properties.check_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_id"]) -> typing.Union[MetaOapg.properties.entity_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legacy_category_id"]) -> typing.Union[MetaOapg.properties.legacy_category_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legacy_category"]) -> typing.Union[MetaOapg.properties.legacy_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurrence"]) -> typing.Union['Recurrence', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["personal_finance_category_icon_url"], typing_extensions.Literal["website"], typing_extensions.Literal["logo_url"], typing_extensions.Literal["payment_channel"], typing_extensions.Literal["merchant_name"], typing_extensions.Literal["location"], typing_extensions.Literal["counterparties"], typing_extensions.Literal["personal_finance_category"], typing_extensions.Literal["check_number"], typing_extensions.Literal["entity_id"], typing_extensions.Literal["legacy_category_id"], typing_extensions.Literal["legacy_category"], typing_extensions.Literal["recurrence"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        personal_finance_category_icon_url: typing.Union[MetaOapg.properties.personal_finance_category_icon_url, str, ],
        website: typing.Union[MetaOapg.properties.website, None, str, ],
        logo_url: typing.Union[MetaOapg.properties.logo_url, None, str, ],
        payment_channel: 'PaymentChannel',
        merchant_name: typing.Union[MetaOapg.properties.merchant_name, None, str, ],
        location: 'Location',
        counterparties: typing.Union[MetaOapg.properties.counterparties, list, tuple, ],
        personal_finance_category: 'PersonalFinanceCategory',
        check_number: typing.Union[MetaOapg.properties.check_number, None, str, schemas.Unset] = schemas.unset,
        entity_id: typing.Union[MetaOapg.properties.entity_id, None, str, schemas.Unset] = schemas.unset,
        legacy_category_id: typing.Union[MetaOapg.properties.legacy_category_id, None, str, schemas.Unset] = schemas.unset,
        legacy_category: typing.Union[MetaOapg.properties.legacy_category, list, tuple, schemas.Unset] = schemas.unset,
        recurrence: typing.Union['Recurrence', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'Enrichments':
        return super().__new__(
            cls,
            *_args,
            personal_finance_category_icon_url=personal_finance_category_icon_url,
            website=website,
            logo_url=logo_url,
            payment_channel=payment_channel,
            merchant_name=merchant_name,
            location=location,
            counterparties=counterparties,
            personal_finance_category=personal_finance_category,
            check_number=check_number,
            entity_id=entity_id,
            legacy_category_id=legacy_category_id,
            legacy_category=legacy_category,
            recurrence=recurrence,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.counterparty import Counterparty
from plaid.model.location import Location
from plaid.model.payment_channel import PaymentChannel
from plaid.model.personal_finance_category import PersonalFinanceCategory
from plaid.model.recurrence import Recurrence
