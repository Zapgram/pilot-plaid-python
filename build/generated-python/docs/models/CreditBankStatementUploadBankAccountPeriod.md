# plaid.model.credit_bank_statement_upload_bank_account_period.CreditBankStatementUploadBankAccountPeriod

An object containing data on the overall period of the statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing data on the overall period of the statement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end_date** | None, str, date,  | NoneClass, str,  | The end date of the statement period in ISO 8601 format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**ending_balance** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The ending balance of the bank account for the period. | 
**starting_balance** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The starting balance of the bank account for the period. | 
**start_date** | None, str, date,  | NoneClass, str,  | The start date of the statement period in ISO 8601 format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

