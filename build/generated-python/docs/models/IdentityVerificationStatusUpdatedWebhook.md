# plaid.model.identity_verification_status_updated_webhook.IdentityVerificationStatusUpdatedWebhook

Fired when the status of an identity verification has been updated, which can be triggered via the dashboard or the API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when the status of an identity verification has been updated, which can be triggered via the dashboard or the API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**identity_verification_id** | str,  | str,  | The ID of the associated Identity Verification attempt. | 
**webhook_type** | str,  | str,  | &#x60;IDENTITY_VERIFICATION&#x60; | 
**webhook_code** | str,  | str,  | &#x60;STATUS_UPDATED&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

