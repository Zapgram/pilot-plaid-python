# plaid.model.credit_bank_income_refresh_request_options.CreditBankIncomeRefreshRequestOptions

An optional object for `/credit/bank_income/refresh` request options.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object for &#x60;/credit/bank_income/refresh&#x60; request options. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**days_requested** | decimal.Decimal, int,  | decimal.Decimal,  | How many days of data to include in the refresh. If not specified, this will default to the days requested in the most recently generated bank income report for the user. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

