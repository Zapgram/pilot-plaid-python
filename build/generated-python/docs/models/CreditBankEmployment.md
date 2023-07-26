# plaid.model.credit_bank_employment.CreditBankEmployment

Detailed information for the bank employment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detailed information for the bank employment. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | str,  | str,  | Plaid&#x27;s unique identifier for the account. | 
**earliest_deposit_date** | str, date,  | str,  | The date of the earliest deposit from this employer from within the period of the days requested. | value must conform to RFC-3339 full-date YYYY-MM-DD
**employer** | [**CreditBankEmployer**](CreditBankEmployer.md) | [**CreditBankEmployer**](CreditBankEmployer.md) |  | 
**latest_deposit_date** | str, date,  | str,  | The date of the most recent deposit from this employer. | value must conform to RFC-3339 full-date YYYY-MM-DD
**bank_employment_id** | str,  | str,  | A unique identifier for the bank employment. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

