# plaid.model.recurring_transactions_update_webhook.RecurringTransactionsUpdateWebhook

Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when a new transaction is added to an existing recurring stream. The `RECURRING_TRANSACTIONS_UPDATE` webhook will also fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update, or removal of transactions to the stream.  After receipt of this webhook, the updated data can be fetched from `/transactions/recurring/get`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when a new transaction is added to an existing recurring stream. The &#x60;RECURRING_TRANSACTIONS_UPDATE&#x60; webhook will also fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update, or removal of transactions to the stream.  After receipt of this webhook, the updated data can be fetched from &#x60;/transactions/recurring/get&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**[account_ids](#account_ids)** | list, tuple,  | tuple,  | A list of &#x60;account_ids&#x60; for accounts that have new or updated recurring transactions data. | 
**webhook_type** | str,  | str,  | &#x60;TRANSACTIONS&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhook_code** | str,  | str,  | &#x60;RECURRING_TRANSACTIONS_UPDATE&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_ids

A list of `account_ids` for accounts that have new or updated recurring transactions data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of &#x60;account_ids&#x60; for accounts that have new or updated recurring transactions data. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

