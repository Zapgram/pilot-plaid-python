# plaid.model.wallet_transaction.WalletTransaction

The transaction details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The transaction details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | A reference for the transaction | 
**transaction_id** | str,  | str,  | A unique ID identifying the transaction | 
**amount** | [**WalletTransactionAmount**](WalletTransactionAmount.md) | [**WalletTransactionAmount**](WalletTransactionAmount.md) |  | 
**wallet_id** | str,  | str,  | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | 
**counterparty** | [**WalletTransactionCounterparty**](WalletTransactionCounterparty.md) | [**WalletTransactionCounterparty**](WalletTransactionCounterparty.md) |  | 
**created_at** | str, datetime,  | str,  | Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | value must conform to RFC-3339 date-time
**last_status_update** | str, datetime,  | str,  | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | value must conform to RFC-3339 date-time
**type** | str,  | str,  | The type of the transaction. The supported transaction types that are returned are: &#x60;BANK_TRANSFER:&#x60; a transaction which credits an e-wallet through an external bank transfer.  &#x60;PAYOUT:&#x60; a transaction which debits an e-wallet by disbursing funds to a counterparty.  &#x60;PIS_PAY_IN:&#x60; a payment which credits an e-wallet through Plaid&#x27;s Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).  &#x60;REFUND:&#x60; a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid&#x27;s [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).  &#x60;FUNDS_SWEEP&#x60;: an automated transaction which debits funds from an e-wallet to a designated client-owned account. | must be one of ["BANK_TRANSFER", "PAYOUT", "PIS_PAY_IN", "REFUND", "FUNDS_SWEEP", ] 
**status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**scheme** | [**WalletPaymentScheme**](WalletPaymentScheme.md) | [**WalletPaymentScheme**](WalletPaymentScheme.md) |  | [optional] 
**payment_id** | None, str,  | NoneClass, str,  | The payment id that this transaction is associated with, if any. This is present only for transaction types &#x60;PIS_PAY_IN&#x60; and &#x60;REFUND&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

