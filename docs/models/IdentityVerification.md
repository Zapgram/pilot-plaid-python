# plaid.model.identity_verification.IdentityVerification

A identity verification attempt represents a customer's attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A identity verification attempt represents a customer&#x27;s attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**template** | [**IdentityVerificationTemplateReference**](IdentityVerificationTemplateReference.md) | [**IdentityVerificationTemplateReference**](IdentityVerificationTemplateReference.md) |  | 
**client_user_id** | [**ClientUserID**](ClientUserID.md) | [**ClientUserID**](ClientUserID.md) |  | 
**redacted_at** | [**TimestampNullable**](TimestampNullable.md) | [**TimestampNullable**](TimestampNullable.md) |  | 
**created_at** | str, datetime,  | str,  | An ISO8601 formatted timestamp. | value must conform to RFC-3339 date-time
**selfie_check** | [**SelfieCheck**](SelfieCheck.md) | [**SelfieCheck**](SelfieCheck.md) |  | 
**steps** | [**IdentityVerificationStepSummary**](IdentityVerificationStepSummary.md) | [**IdentityVerificationStepSummary**](IdentityVerificationStepSummary.md) |  | 
**kyc_check** | [**KYCCheckDetails**](KYCCheckDetails.md) | [**KYCCheckDetails**](KYCCheckDetails.md) |  | 
**risk_check** | [**RiskCheckDetails**](RiskCheckDetails.md) | [**RiskCheckDetails**](RiskCheckDetails.md) |  | 
**completed_at** | [**TimestampNullable**](TimestampNullable.md) | [**TimestampNullable**](TimestampNullable.md) |  | 
**documentary_verification** | [**DocumentaryVerification**](DocumentaryVerification.md) | [**DocumentaryVerification**](DocumentaryVerification.md) |  | 
**shareable_url** | [**ShareableURL**](ShareableURL.md) | [**ShareableURL**](ShareableURL.md) |  | 
**previous_attempt_id** | [**PreviousIdentityVerificationAttemptID**](PreviousIdentityVerificationAttemptID.md) | [**PreviousIdentityVerificationAttemptID**](PreviousIdentityVerificationAttemptID.md) |  | 
**id** | str,  | str,  | ID of the associated Identity Verification attempt. | 
**watchlist_screening_id** | [**WatchlistScreeningIndividualIDNullable**](WatchlistScreeningIndividualIDNullable.md) | [**WatchlistScreeningIndividualIDNullable**](WatchlistScreeningIndividualIDNullable.md) |  | 
**user** | [**IdentityVerificationUserData**](IdentityVerificationUserData.md) | [**IdentityVerificationUserData**](IdentityVerificationUserData.md) |  | 
**status** | [**IdentityVerificationStatus**](IdentityVerificationStatus.md) | [**IdentityVerificationStatus**](IdentityVerificationStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

