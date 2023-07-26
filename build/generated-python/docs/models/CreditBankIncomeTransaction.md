# plaid.model.credit_bank_income_transaction.CreditBankIncomeTransaction

The transactions data for the end user's income source(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The transactions data for the end user&#x27;s income source(s). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The settled value of the transaction, denominated in the transactions&#x27;s currency as stated in &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, credit card purchases are positive; credit card payment, direct deposits, and refunds are negative. | [optional] 
**date** | str, date,  | str,  | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**name** | str,  | str,  | The merchant name or transaction description. | [optional] 
**original_description** | None, str,  | NoneClass, str,  | The string returned by the financial institution to describe the transaction. | [optional] 
**pending** | bool,  | BoolClass,  | When true, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. | [optional] 
**transaction_id** | str,  | str,  | The unique ID of the transaction. Like all Plaid identifiers, the &#x60;transaction_id&#x60; is case sensitive. | [optional] 
**check_number** | None, str,  | NoneClass, str,  | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**iso_currency_code** | [**CreditIsoCurrencyCode**](CreditIsoCurrencyCode.md) | [**CreditIsoCurrencyCode**](CreditIsoCurrencyCode.md) |  | [optional] 
**unofficial_currency_code** | [**CreditUnofficialCurrencyCode**](CreditUnofficialCurrencyCode.md) | [**CreditUnofficialCurrencyCode**](CreditUnofficialCurrencyCode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

