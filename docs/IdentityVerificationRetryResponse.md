# IdentityVerificationRetryResponse

A identity verification attempt represents a customer's attempt to verify their identity, reflecting the required steps for completing the session, the results for each step, and information collected in the process.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the associated Identity Verification attempt. | 
**client_user_id** | [**ClientUserID**](ClientUserID.md) |  | 
**created_at** | **datetime** | An ISO8601 formatted timestamp. | 
**completed_at** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**previous_attempt_id** | **str, none_type** | The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt. | 
**shareable_url** | **str, none_type** | A shareable URL that can be sent directly to the user to complete verification | 
**template** | [**IdentityVerificationTemplateReference**](IdentityVerificationTemplateReference.md) |  | 
**user** | [**IdentityVerificationUserData**](IdentityVerificationUserData.md) |  | 
**status** | [**IdentityVerificationStatus**](IdentityVerificationStatus.md) |  | 
**steps** | [**IdentityVerificationStepSummary**](IdentityVerificationStepSummary.md) |  | 
**documentary_verification** | [**DocumentaryVerification**](DocumentaryVerification.md) |  | 
**selfie_check** | [**SelfieCheck**](SelfieCheck.md) |  | 
**kyc_check** | [**KYCCheckDetails**](KYCCheckDetails.md) |  | 
**risk_check** | [**RiskCheckDetails**](RiskCheckDetails.md) |  | 
**watchlist_screening_id** | **str, none_type** | ID of the associated screening. | 
**redacted_at** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


