# plaid.model.bank_income_refresh_update_webhook.BankIncomeRefreshUpdateWebhook

Fired when a change to the user's income is detected. You should call `/credit/bank_income/refresh` to get updated income data for the user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when a change to the user&#x27;s income is detected. You should call &#x60;/credit/bank_income/refresh&#x60; to get updated income data for the user | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;INCOME&#x60; | 
**user_id** | str,  | str,  | The &#x60;user_id&#x60; corresponding to the user the webhook has fired for. | 
**webhook_code** | str,  | str,  | &#x60;BANK_INCOME_REFRESH_UPDATE&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

