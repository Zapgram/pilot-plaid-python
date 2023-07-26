# plaid.model.processor_token_webhook_update.ProcessorTokenWebhookUpdate

This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).  Fired when a processor updates the webhook URL for a processor token via `/processor/token/webhook/update`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).  Fired when a processor updates the webhook URL for a processor token via &#x60;/processor/token/webhook/update&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**account_id** | str,  | str,  | The ID of the account. | 
**webhook_type** | str,  | str,  | &#x60;PROCESSOR_TOKEN&#x60; | 
**new_webhook_url** | str,  | str,  | The new webhook URL. | 
**webhook_code** | str,  | str,  | &#x60;WEBHOOK_UPDATE_ACKNOWLEDGED&#x60; | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

