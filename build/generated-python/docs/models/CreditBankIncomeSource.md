# plaid.model.credit_bank_income_source.CreditBankIncomeSource

Detailed information for the income source.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detailed information for the income source. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**income_source_id** | str,  | str,  | A unique identifier for an income source. | [optional] 
**income_description** | str,  | str,  | The most common name or original description for the underlying income transactions. | [optional] 
**income_category** | [**CreditBankIncomeCategory**](CreditBankIncomeCategory.md) | [**CreditBankIncomeCategory**](CreditBankIncomeCategory.md) |  | [optional] 
**account_id** | str,  | str,  | Plaid&#x27;s unique identifier for the account. | [optional] 
**start_date** | str, date,  | str,  | Minimum of all dates within the specific income sources in the user&#x27;s bank account for days requested by the client. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**end_date** | str, date,  | str,  | Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**pay_frequency** | [**CreditBankIncomePayFrequency**](CreditBankIncomePayFrequency.md) | [**CreditBankIncomePayFrequency**](CreditBankIncomePayFrequency.md) |  | [optional] 
**total_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total amount of earnings in the user’s bank account for the specific income source for days requested by the client. | [optional] 
**transaction_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of transactions for the income source within the start and end date. | [optional] 
**[historical_summary](#historical_summary)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

