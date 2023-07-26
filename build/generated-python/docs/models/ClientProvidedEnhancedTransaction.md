# plaid.model.client_provided_enhanced_transaction.ClientProvidedEnhancedTransaction

A client-provided transaction that Plaid has enhanced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A client-provided transaction that Plaid has enhanced. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The value of the transaction, denominated in the account&#x27;s currency, as stated in &#x60;iso_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | value must be a 64 bit float
**enhancements** | [**Enhancements**](Enhancements.md) | [**Enhancements**](Enhancements.md) |  | 
**iso_currency_code** | str,  | str,  | The ISO-4217 currency code of the transaction. | 
**description** | str,  | str,  | The raw description of the transaction. | 
**id** | str,  | str,  | Unique transaction identifier to tie transactions back to clients&#x27; systems. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

