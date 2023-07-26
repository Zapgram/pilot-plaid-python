# IdentityVerificationStepUpdatedWebhook

Fired when an end user has completed a step of the Identity Verification process.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;IDENTITY_VERIFICATION&#x60; | 
**webhook_code** | **str** | &#x60;STEP_UPDATED&#x60; | 
**identity_verification_id** | **str** | The ID of the associated Identity Verification attempt. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


