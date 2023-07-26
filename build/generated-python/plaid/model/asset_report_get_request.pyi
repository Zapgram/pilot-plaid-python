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


class AssetReportGetRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    AssetReportGetRequest defines the request schema for `/asset_report/get`
    """


    class MetaOapg:
        
        class properties:
            client_id = schemas.StrSchema
            secret = schemas.StrSchema
            asset_report_token = schemas.StrSchema
            user_token = schemas.StrSchema
            include_insights = schemas.BoolSchema
            fast_report = schemas.BoolSchema
        
            @staticmethod
            def options() -> typing.Type['AssetReportGetRequestOptions']:
                return AssetReportGetRequestOptions
            __annotations__ = {
                "client_id": client_id,
                "secret": secret,
                "asset_report_token": asset_report_token,
                "user_token": user_token,
                "include_insights": include_insights,
                "fast_report": fast_report,
                "options": options,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset_report_token"]) -> MetaOapg.properties.asset_report_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_token"]) -> MetaOapg.properties.user_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_insights"]) -> MetaOapg.properties.include_insights: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fast_report"]) -> MetaOapg.properties.fast_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'AssetReportGetRequestOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_id", "secret", "asset_report_token", "user_token", "include_insights", "fast_report", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset_report_token"]) -> typing.Union[MetaOapg.properties.asset_report_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_token"]) -> typing.Union[MetaOapg.properties.user_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_insights"]) -> typing.Union[MetaOapg.properties.include_insights, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fast_report"]) -> typing.Union[MetaOapg.properties.fast_report, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['AssetReportGetRequestOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_id", "secret", "asset_report_token", "user_token", "include_insights", "fast_report", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        asset_report_token: typing.Union[MetaOapg.properties.asset_report_token, str, schemas.Unset] = schemas.unset,
        user_token: typing.Union[MetaOapg.properties.user_token, str, schemas.Unset] = schemas.unset,
        include_insights: typing.Union[MetaOapg.properties.include_insights, bool, schemas.Unset] = schemas.unset,
        fast_report: typing.Union[MetaOapg.properties.fast_report, bool, schemas.Unset] = schemas.unset,
        options: typing.Union['AssetReportGetRequestOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssetReportGetRequest':
        return super().__new__(
            cls,
            *_args,
            client_id=client_id,
            secret=secret,
            asset_report_token=asset_report_token,
            user_token=user_token,
            include_insights=include_insights,
            fast_report=fast_report,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.asset_report_get_request_options import AssetReportGetRequestOptions
