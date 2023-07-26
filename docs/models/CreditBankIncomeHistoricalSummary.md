# plaid.model.credit_bank_income_historical_summary.CreditBankIncomeHistoricalSummary

The end user's monthly summary for the income source(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The end user&#x27;s monthly summary for the income source(s). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total amount of earnings for the income source(s) of the user for the month in the summary. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead. | [optional] 
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO 4217 currency code of the amount or balance. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead. | [optional] 
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the amount or balance. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-items-bank-income-sources-historical-summary-total-amounts) instead. | [optional] 
**[total_amounts](#total_amounts)** | list, tuple,  | tuple,  | Total amount of earnings for the income source(s) of the user for the month in the summary. This can contain multiple amounts, with each amount denominated in one unique currency. | [optional] 
**start_date** | str, date,  | str,  | The start date of the period covered in this monthly summary. This date will be the first day of the month, unless the month being covered is a partial month because it is the first month included in the summary and the date range being requested does not begin with the first day of the month. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**end_date** | str, date,  | str,  | The end date of the period included in this monthly summary. This date will be the last day of the month, unless the month being covered is a partial month because it is the last month included in the summary and the date range being requested does not end with the last day of the month. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[transactions](#transactions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# total_amounts

Total amount of earnings for the income source(s) of the user for the month in the summary. This can contain multiple amounts, with each amount denominated in one unique currency.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Total amount of earnings for the income source(s) of the user for the month in the summary. This can contain multiple amounts, with each amount denominated in one unique currency. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditAmountWithCurrency**](CreditAmountWithCurrency.md) | [**CreditAmountWithCurrency**](CreditAmountWithCurrency.md) | [**CreditAmountWithCurrency**](CreditAmountWithCurrency.md) |  | 

# transactions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeTransaction**](CreditBankIncomeTransaction.md) | [**CreditBankIncomeTransaction**](CreditBankIncomeTransaction.md) | [**CreditBankIncomeTransaction**](CreditBankIncomeTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

