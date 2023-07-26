# plaid.model.wallet_transaction_counterparty_numbers.WalletTransactionCounterpartyNumbers

The counterparty's bank account numbers. Exactly one of IBAN or BACS data is required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The counterparty&#x27;s bank account numbers. Exactly one of IBAN or BACS data is required. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bacs** | [**WalletTransactionCounterpartyBACS**](WalletTransactionCounterpartyBACS.md) | [**WalletTransactionCounterpartyBACS**](WalletTransactionCounterpartyBACS.md) |  | [optional] 
**international** | [**WalletTransactionCounterpartyInternational**](WalletTransactionCounterpartyInternational.md) | [**WalletTransactionCounterpartyInternational**](WalletTransactionCounterpartyInternational.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

