# CreditBankIncomeSummary

Summary for bank income across all income sources and items (max history of 730 days).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **float** | Total amount of earnings across all the income sources in the end user&#39;s Items for the days requested by the client. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**iso_currency_code** | **str, none_type** | The ISO 4217 currency code of the amount or balance. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the amount or balance. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**total_amounts** | [**[CreditAmountWithCurrency]**](CreditAmountWithCurrency.md) | Total amount of earnings across all the income sources in the end user&#39;s Items for the days requested by the client. This can contain multiple amounts, with each amount denominated in one unique currency. | [optional] 
**start_date** | **date** | The earliest date within the days requested in which all income sources identified by Plaid appear in a user&#39;s account. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**end_date** | **date** | The latest date in which all income sources identified by Plaid appear in the user&#39;s account. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**income_sources_count** | **int** | Number of income sources per end user. | [optional] 
**income_categories_count** | **int** | Number of income categories per end user. | [optional] 
**income_transactions_count** | **int** | Number of income transactions per end user. | [optional] 
**historical_summary** | [**[CreditBankIncomeHistoricalSummary]**](CreditBankIncomeHistoricalSummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


