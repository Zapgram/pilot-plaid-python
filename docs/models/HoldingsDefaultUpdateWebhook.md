# plaid.model.holdings_default_update_webhook.HoldingsDefaultUpdateWebhook

Fired when new or updated holdings have been detected on an investment account. The webhook typically fires in response to any newly added holdings or price changes to existing holdings, most commonly after market close.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when new or updated holdings have been detected on an investment account. The webhook typically fires in response to any newly added holdings or price changes to existing holdings, most commonly after market close. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;HOLDINGS&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**new_holdings** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of new holdings reported since the last time this webhook was fired. | 
**webhook_code** | str,  | str,  | &#x60;DEFAULT_UPDATE&#x60; | 
**updated_holdings** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of updated holdings reported since the last time this webhook was fired. | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

