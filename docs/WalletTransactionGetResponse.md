# WalletTransactionGetResponse

WalletTransactionGetResponse defines the response schema for `/wallet/transaction/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | A unique ID identifying the transaction | 
**wallet_id** | **str** | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | 
**reference** | **str** | A reference for the transaction | 
**type** | **str** | The type of the transaction. The supported transaction types that are returned are: &#x60;BANK_TRANSFER:&#x60; a transaction which credits an e-wallet through an external bank transfer.  &#x60;PAYOUT:&#x60; a transaction which debits an e-wallet by disbursing funds to a counterparty.  &#x60;PIS_PAY_IN:&#x60; a payment which credits an e-wallet through Plaid&#39;s Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).  &#x60;REFUND:&#x60; a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid&#39;s [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).  &#x60;FUNDS_SWEEP&#x60;: an automated transaction which debits funds from an e-wallet to a designated client-owned account. | 
**amount** | [**WalletTransactionAmount**](WalletTransactionAmount.md) |  | 
**counterparty** | [**WalletTransactionCounterparty**](WalletTransactionCounterparty.md) |  | 
**status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**created_at** | **datetime** | Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**last_status_update** | **datetime** | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**scheme** | [**WalletPaymentScheme**](WalletPaymentScheme.md) |  | [optional] 
**payment_id** | **str, none_type** | The payment id that this transaction is associated with, if any. This is present only for transaction types &#x60;PIS_PAY_IN&#x60; and &#x60;REFUND&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


