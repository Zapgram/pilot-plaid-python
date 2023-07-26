# plaid.model.identity_default_update_webhook.IdentityDefaultUpdateWebhook

Fired when a change to identity data has been detected on an Item. Items are checked for identity updates every 30-90 days. We recommend that upon receiving this webhook you make another call to `/identity/get` to fetch the user's latest identity data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when a change to identity data has been detected on an Item. Items are checked for identity updates every 30-90 days. We recommend that upon receiving this webhook you make another call to &#x60;/identity/get&#x60; to fetch the user&#x27;s latest identity data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;IDENTITY&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**account_ids_with_updated_identity** | [**AccountIdsWithUpdatedIdentity**](AccountIdsWithUpdatedIdentity.md) | [**AccountIdsWithUpdatedIdentity**](AccountIdsWithUpdatedIdentity.md) |  | 
**webhook_code** | str,  | str,  | &#x60;DEFAULT_UPDATE&#x60; | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

