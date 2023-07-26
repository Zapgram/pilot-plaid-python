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


class DocumentMetadata(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An object representing metadata from the end user's uploaded document.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            
            
            class status(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            doc_id = schemas.StrSchema
        
            @staticmethod
            def doc_type() -> typing.Type['DocType']:
                return DocType
            __annotations__ = {
                "name": name,
                "status": status,
                "doc_id": doc_id,
                "doc_type": doc_type,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doc_id"]) -> MetaOapg.properties.doc_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doc_type"]) -> 'DocType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["status"], typing_extensions.Literal["doc_id"], typing_extensions.Literal["doc_type"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doc_id"]) -> typing.Union[MetaOapg.properties.doc_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doc_type"]) -> typing.Union['DocType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["status"], typing_extensions.Literal["doc_id"], typing_extensions.Literal["doc_type"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, None, str, schemas.Unset] = schemas.unset,
        doc_id: typing.Union[MetaOapg.properties.doc_id, str, schemas.Unset] = schemas.unset,
        doc_type: typing.Union['DocType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'DocumentMetadata':
        return super().__new__(
            cls,
            *_args,
            name=name,
            status=status,
            doc_id=doc_id,
            doc_type=doc_type,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.doc_type import DocType
