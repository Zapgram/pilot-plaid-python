# plaid.model.transactions_removed_webhook.TransactionsRemovedWebhook

Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook payload. Plaid will typically check for deleted transaction data several times a day.  This webhook is intended for use with `/transactions/get`; if you are using the newer `/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook payload. Plaid will typically check for deleted transaction data several times a day.  This webhook is intended for use with &#x60;/transactions/get&#x60;; if you are using the newer &#x60;/transactions/sync&#x60; endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the &#x60;SYNC_UPDATES_AVAILABLE&#x60; webhook instead. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**[removed_transactions](#removed_transactions)** | list, tuple,  | tuple,  | An array of &#x60;transaction_ids&#x60; corresponding to the removed transactions | 
**webhook_type** | str,  | str,  | &#x60;TRANSACTIONS&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhook_code** | str,  | str,  | &#x60;TRANSACTIONS_REMOVED&#x60; | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# removed_transactions

An array of `transaction_ids` corresponding to the removed transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of &#x60;transaction_ids&#x60; corresponding to the removed transactions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

