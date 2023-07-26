# plaid.model.investments_historical_update_webhook.InvestmentsHistoricalUpdateWebhook

Fired after an asynchronous extraction on an investments account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired after an asynchronous extraction on an investments account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;INVESTMENTS_TRANSACTIONS&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**canceled_investments_transactions** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of canceled transactions reported since the last time this webhook was fired. | 
**webhook_code** | str,  | str,  | &#x60;HISTORICAL_UPDATE&#x60; | 
**new_investments_transactions** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of new transactions reported since the last time this webhook was fired. | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

