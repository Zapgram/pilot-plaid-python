# plaid.model.processor_default_update_webhook.ProcessorDefaultUpdateWebhook

This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).  Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day.  This webhook is intended for use with `/processor/transactions/get`; if you are using the newer `/processor/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).  Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day.  This webhook is intended for use with &#x60;/processor/transactions/get&#x60;; if you are using the newer &#x60;/processor/transactions/sync&#x60; endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the &#x60;SYNC_UPDATES_AVAILABLE&#x60; webhook instead.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**account_id** | str,  | str,  | The ID of the account. | 
**webhook_type** | str,  | str,  | &#x60;TRANSACTIONS&#x60; | 
**new_transactions** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of new transactions detected since the last time this webhook was fired. | 
**webhook_code** | str,  | str,  | &#x60;DEFAULT_UPDATE&#x60; | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

