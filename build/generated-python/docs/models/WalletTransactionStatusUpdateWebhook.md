# plaid.model.wallet_transaction_status_update_webhook.WalletTransactionStatusUpdateWebhook

Fired when the status of a wallet transaction has changed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when the status of a wallet transaction has changed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**old_status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**transaction_id** | str,  | str,  | The &#x60;transaction_id&#x60; for the wallet transaction being updated | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;WALLET&#x60; | 
**new_status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**webhook_code** | str,  | str,  | &#x60;WALLET_TRANSACTION_STATUS_UPDATE&#x60; | 
**timestamp** | str, datetime,  | str,  | The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. &#x60;\&quot;2017-09-14T14:42:19.350Z\&quot;&#x60; | value must conform to RFC-3339 date-time
**payment_id** | None, str,  | NoneClass, str,  | The &#x60;payment_id&#x60; associated with the transaction. This will be present in case of &#x60;REFUND&#x60; and &#x60;PIS_PAY_IN&#x60; | [optional] 
**wallet_id** | str,  | str,  | The EMI (E-Money Institution) wallet that this payment is associated with. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

