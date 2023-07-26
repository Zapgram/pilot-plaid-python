# plaid.model.credit_bank_income_summary.CreditBankIncomeSummary

Summary for bank income across all income sources and items (max history of 730 days).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary for bank income across all income sources and items (max history of 730 days). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total amount of earnings across all the income sources in the end user&#x27;s Items for the days requested by the client. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**iso_currency_code** | None, str,  | NoneClass, str,  | The ISO 4217 currency code of the amount or balance. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**unofficial_currency_code** | None, str,  | NoneClass, str,  | The unofficial currency code associated with the amount or balance. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**[total_amounts](#total_amounts)** | list, tuple,  | tuple,  | Total amount of earnings across all the income sources in the end user&#x27;s Items for the days requested by the client. This can contain multiple amounts, with each amount denominated in one unique currency. | [optional] 
**start_date** | str, date,  | str,  | The earliest date within the days requested in which all income sources identified by Plaid appear in a user&#x27;s account. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**end_date** | str, date,  | str,  | The latest date in which all income sources identified by Plaid appear in the user&#x27;s account. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**income_sources_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of income sources per end user. | [optional] 
**income_categories_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of income categories per end user. | [optional] 
**income_transactions_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of income transactions per end user. | [optional] 
**[historical_summary](#historical_summary)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# total_amounts

Total amount of earnings across all the income sources in the end user's Items for the days requested by the client. This can contain multiple amounts, with each amount denominated in one unique currency.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Total amount of earnings across all the income sources in the end user&#x27;s Items for the days requested by the client. This can contain multiple amounts, with each amount denominated in one unique currency. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditAmountWithCurrency**](CreditAmountWithCurrency.md) | [**CreditAmountWithCurrency**](CreditAmountWithCurrency.md) | [**CreditAmountWithCurrency**](CreditAmountWithCurrency.md) |  | 

# historical_summary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeHistoricalSummary**](CreditBankIncomeHistoricalSummary.md) | [**CreditBankIncomeHistoricalSummary**](CreditBankIncomeHistoricalSummary.md) | [**CreditBankIncomeHistoricalSummary**](CreditBankIncomeHistoricalSummary.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

