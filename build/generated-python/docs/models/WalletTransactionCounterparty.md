# plaid.model.wallet_transaction_counterparty.WalletTransactionCounterparty

An object representing the e-wallet transaction's counterparty

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the e-wallet transaction&#x27;s counterparty | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the counterparty | 
**numbers** | [**WalletTransactionCounterpartyNumbers**](WalletTransactionCounterpartyNumbers.md) | [**WalletTransactionCounterpartyNumbers**](WalletTransactionCounterpartyNumbers.md) |  | 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**date_of_birth** | None, str, date,  | NoneClass, str,  | The counterparty&#x27;s birthdate, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

