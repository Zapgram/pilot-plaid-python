# IdentityVerificationRetryRequestStepsObject

Instructions for the `custom` retry strategy specifying which steps should be required or skipped.   Note:   This field must be provided when the retry strategy is `custom` and must be omitted otherwise.  Custom retries override settings in your Plaid Template. For example, if your Plaid Template has `verify_sms` disabled, a custom retry with `verify_sms` enabled will still require the step.  The `selfie_check` step is currently not supported on the sandbox server. Sandbox requests will silently disable the `selfie_check` step when provided.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_sms** | **bool** | A boolean field specifying whether the new session should require or skip the &#x60;verify_sms&#x60; step. | 
**kyc_check** | **bool** | A boolean field specifying whether the new session should require or skip the &#x60;kyc_check&#x60; step. | 
**documentary_verification** | **bool** | A boolean field specifying whether the new session should require or skip the &#x60;documentary_verification&#x60; step. | 
**selfie_check** | **bool** | A boolean field specifying whether the new session should require or skip the &#x60;selfie_check&#x60; step. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


