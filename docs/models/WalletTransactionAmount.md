# plaid.model.wallet_transaction_amount.WalletTransactionAmount

The amount and currency of a transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The amount and currency of a transaction | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**iso_currency_code** | [**WalletISOCurrencyCode**](WalletISOCurrencyCode.md) | [**WalletISOCurrencyCode**](WalletISOCurrencyCode.md) |  | 
**value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the transaction. Must contain at most two digits of precision e.g. &#x60;1.23&#x60;. | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

