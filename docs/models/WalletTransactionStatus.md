# plaid.model.wallet_transaction_status.WalletTransactionStatus

The status of the transaction.  `AUTHORISING`: The transaction is being processed for validation and compliance.  `INITIATED`: The transaction has been initiated and is currently being processed.  `EXECUTED`: The transaction has been successfully executed and is considered complete. This is only applicable for debit transactions.  `SETTLED`: The transaction has settled and funds are available for use. This is only applicable for credit transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is used.  `FAILED`: The transaction failed to process successfully. This is a terminal status.  `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The status of the transaction.  &#x60;AUTHORISING&#x60;: The transaction is being processed for validation and compliance.  &#x60;INITIATED&#x60;: The transaction has been initiated and is currently being processed.  &#x60;EXECUTED&#x60;: The transaction has been successfully executed and is considered complete. This is only applicable for debit transactions.  &#x60;SETTLED&#x60;: The transaction has settled and funds are available for use. This is only applicable for credit transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is used.  &#x60;FAILED&#x60;: The transaction failed to process successfully. This is a terminal status.  &#x60;BLOCKED&#x60;: The transaction has been blocked for violating compliance rules. This is a terminal status. | must be one of ["AUTHORISING", "INITIATED", "EXECUTED", "SETTLED", "BLOCKED", "FAILED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

