# plaid.model.investment_transaction.InvestmentTransaction

A transaction within an investment account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A transaction within an investment account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, date,  | str,  | The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction. | value must conform to RFC-3339 full-date YYYY-MM-DD
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the holding. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities. | value must be a 64 bit float
**fees** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The combined value of all fees applied to this transaction | value must be a 64 bit float
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | The number of units of the security involved in this transaction. Positive for buy transactions; negative for sell transactions. | value must be a 64 bit float
**type** | [**InvestmentTransactionType**](InvestmentTransactionType.md) | [**InvestmentTransactionType**](InvestmentTransactionType.md) |  | 
**account_id** | str,  | str,  | The &#x60;account_id&#x60; of the account against which this transaction posted. | 
**subtype** | [**InvestmentTransactionSubtype**](InvestmentTransactionSubtype.md) | [**InvestmentTransactionSubtype**](InvestmentTransactionSubtype.md) |  | 
**investment_transaction_id** | str,  | str,  | The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the &#x60;investment_transaction_id&#x60; is case sensitive. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price of the security at which this transaction occurred. | value must be a 64 bit float
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO-4217 currency code of the transaction. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | 
**name** | str,  | str,  | The institution’s description of the transaction. | 
**security_id** | None, str,  | NoneClass, str,  | The &#x60;security_id&#x60; to which this transaction is related. | 
**cancel_transaction_id** | None, str,  | NoneClass, str,  | A legacy field formerly used internally by Plaid to identify certain canceled transactions. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

