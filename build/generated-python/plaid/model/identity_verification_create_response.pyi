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


class IdentityVerificationCreateResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A identity verification attempt represents a customer's attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process.
    """


    class MetaOapg:
        required = {
            "template",
            "client_user_id",
            "redacted_at",
            "created_at",
            "selfie_check",
            "steps",
            "kyc_check",
            "risk_check",
            "completed_at",
            "documentary_verification",
            "shareable_url",
            "previous_attempt_id",
            "id",
            "watchlist_screening_id",
            "request_id",
            "user",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def client_user_id() -> typing.Type['ClientUserID']:
                return ClientUserID
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def completed_at() -> typing.Type['TimestampNullable']:
                return TimestampNullable
        
            @staticmethod
            def previous_attempt_id() -> typing.Type['PreviousIdentityVerificationAttemptID']:
                return PreviousIdentityVerificationAttemptID
        
            @staticmethod
            def shareable_url() -> typing.Type['ShareableURL']:
                return ShareableURL
        
            @staticmethod
            def template() -> typing.Type['IdentityVerificationTemplateReference']:
                return IdentityVerificationTemplateReference
        
            @staticmethod
            def user() -> typing.Type['IdentityVerificationUserData']:
                return IdentityVerificationUserData
        
            @staticmethod
            def status() -> typing.Type['IdentityVerificationStatus']:
                return IdentityVerificationStatus
        
            @staticmethod
            def steps() -> typing.Type['IdentityVerificationStepSummary']:
                return IdentityVerificationStepSummary
        
            @staticmethod
            def documentary_verification() -> typing.Type['DocumentaryVerification']:
                return DocumentaryVerification
        
            @staticmethod
            def selfie_check() -> typing.Type['SelfieCheck']:
                return SelfieCheck
        
            @staticmethod
            def kyc_check() -> typing.Type['KYCCheckDetails']:
                return KYCCheckDetails
        
            @staticmethod
            def risk_check() -> typing.Type['RiskCheckDetails']:
                return RiskCheckDetails
        
            @staticmethod
            def watchlist_screening_id() -> typing.Type['WatchlistScreeningIndividualIDNullable']:
                return WatchlistScreeningIndividualIDNullable
        
            @staticmethod
            def redacted_at() -> typing.Type['TimestampNullable']:
                return TimestampNullable
            request_id = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "client_user_id": client_user_id,
                "created_at": created_at,
                "completed_at": completed_at,
                "previous_attempt_id": previous_attempt_id,
                "shareable_url": shareable_url,
                "template": template,
                "user": user,
                "status": status,
                "steps": steps,
                "documentary_verification": documentary_verification,
                "selfie_check": selfie_check,
                "kyc_check": kyc_check,
                "risk_check": risk_check,
                "watchlist_screening_id": watchlist_screening_id,
                "redacted_at": redacted_at,
                "request_id": request_id,
            }
        additional_properties = schemas.AnyTypeSchema
    
    template: 'IdentityVerificationTemplateReference'
    client_user_id: 'ClientUserID'
    redacted_at: 'TimestampNullable'
    created_at: MetaOapg.properties.created_at
    selfie_check: 'SelfieCheck'
    steps: 'IdentityVerificationStepSummary'
    kyc_check: 'KYCCheckDetails'
    risk_check: 'RiskCheckDetails'
    completed_at: 'TimestampNullable'
    documentary_verification: 'DocumentaryVerification'
    shareable_url: 'ShareableURL'
    previous_attempt_id: 'PreviousIdentityVerificationAttemptID'
    id: MetaOapg.properties.id
    watchlist_screening_id: 'WatchlistScreeningIndividualIDNullable'
    request_id: MetaOapg.properties.request_id
    user: 'IdentityVerificationUserData'
    status: 'IdentityVerificationStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> 'IdentityVerificationTemplateReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_user_id"]) -> 'ClientUserID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redacted_at"]) -> 'TimestampNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfie_check"]) -> 'SelfieCheck': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps"]) -> 'IdentityVerificationStepSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kyc_check"]) -> 'KYCCheckDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk_check"]) -> 'RiskCheckDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed_at"]) -> 'TimestampNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentary_verification"]) -> 'DocumentaryVerification': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareable_url"]) -> 'ShareableURL': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previous_attempt_id"]) -> 'PreviousIdentityVerificationAttemptID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["watchlist_screening_id"]) -> 'WatchlistScreeningIndividualIDNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'IdentityVerificationUserData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'IdentityVerificationStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["template"], typing_extensions.Literal["client_user_id"], typing_extensions.Literal["redacted_at"], typing_extensions.Literal["created_at"], typing_extensions.Literal["selfie_check"], typing_extensions.Literal["steps"], typing_extensions.Literal["kyc_check"], typing_extensions.Literal["risk_check"], typing_extensions.Literal["completed_at"], typing_extensions.Literal["documentary_verification"], typing_extensions.Literal["shareable_url"], typing_extensions.Literal["previous_attempt_id"], typing_extensions.Literal["id"], typing_extensions.Literal["watchlist_screening_id"], typing_extensions.Literal["request_id"], typing_extensions.Literal["user"], typing_extensions.Literal["status"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> 'IdentityVerificationTemplateReference': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_user_id"]) -> 'ClientUserID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redacted_at"]) -> 'TimestampNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selfie_check"]) -> 'SelfieCheck': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps"]) -> 'IdentityVerificationStepSummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kyc_check"]) -> 'KYCCheckDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk_check"]) -> 'RiskCheckDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed_at"]) -> 'TimestampNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentary_verification"]) -> 'DocumentaryVerification': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareable_url"]) -> 'ShareableURL': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previous_attempt_id"]) -> 'PreviousIdentityVerificationAttemptID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["watchlist_screening_id"]) -> 'WatchlistScreeningIndividualIDNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_id"]) -> MetaOapg.properties.request_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'IdentityVerificationUserData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'IdentityVerificationStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["template"], typing_extensions.Literal["client_user_id"], typing_extensions.Literal["redacted_at"], typing_extensions.Literal["created_at"], typing_extensions.Literal["selfie_check"], typing_extensions.Literal["steps"], typing_extensions.Literal["kyc_check"], typing_extensions.Literal["risk_check"], typing_extensions.Literal["completed_at"], typing_extensions.Literal["documentary_verification"], typing_extensions.Literal["shareable_url"], typing_extensions.Literal["previous_attempt_id"], typing_extensions.Literal["id"], typing_extensions.Literal["watchlist_screening_id"], typing_extensions.Literal["request_id"], typing_extensions.Literal["user"], typing_extensions.Literal["status"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        template: 'IdentityVerificationTemplateReference',
        client_user_id: 'ClientUserID',
        redacted_at: 'TimestampNullable',
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        selfie_check: 'SelfieCheck',
        steps: 'IdentityVerificationStepSummary',
        kyc_check: 'KYCCheckDetails',
        risk_check: 'RiskCheckDetails',
        completed_at: 'TimestampNullable',
        documentary_verification: 'DocumentaryVerification',
        shareable_url: 'ShareableURL',
        previous_attempt_id: 'PreviousIdentityVerificationAttemptID',
        id: typing.Union[MetaOapg.properties.id, str, ],
        watchlist_screening_id: 'WatchlistScreeningIndividualIDNullable',
        request_id: typing.Union[MetaOapg.properties.request_id, str, ],
        user: 'IdentityVerificationUserData',
        status: 'IdentityVerificationStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'IdentityVerificationCreateResponse':
        return super().__new__(
            cls,
            *_args,
            template=template,
            client_user_id=client_user_id,
            redacted_at=redacted_at,
            created_at=created_at,
            selfie_check=selfie_check,
            steps=steps,
            kyc_check=kyc_check,
            risk_check=risk_check,
            completed_at=completed_at,
            documentary_verification=documentary_verification,
            shareable_url=shareable_url,
            previous_attempt_id=previous_attempt_id,
            id=id,
            watchlist_screening_id=watchlist_screening_id,
            request_id=request_id,
            user=user,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from plaid.model.client_user_id import ClientUserID
from plaid.model.documentary_verification import DocumentaryVerification
from plaid.model.identity_verification_status import IdentityVerificationStatus
from plaid.model.identity_verification_step_summary import IdentityVerificationStepSummary
from plaid.model.identity_verification_template_reference import IdentityVerificationTemplateReference
from plaid.model.identity_verification_user_data import IdentityVerificationUserData
from plaid.model.kyc_check_details import KYCCheckDetails
from plaid.model.previous_identity_verification_attempt_id import PreviousIdentityVerificationAttemptID
from plaid.model.risk_check_details import RiskCheckDetails
from plaid.model.selfie_check import SelfieCheck
from plaid.model.shareable_url import ShareableURL
from plaid.model.timestamp_nullable import TimestampNullable
from plaid.model.watchlist_screening_individual_id_nullable import WatchlistScreeningIndividualIDNullable
