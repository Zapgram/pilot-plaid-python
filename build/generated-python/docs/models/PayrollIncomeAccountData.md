# plaid.model.payroll_income_account_data.PayrollIncomeAccountData

An object containing account level data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An object containing account level data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | None, str,  | NoneClass, str,  | ID of the payroll provider account. | 
**rate_of_pay** | [**PayrollIncomeRateOfPay**](PayrollIncomeRateOfPay.md) | [**PayrollIncomeRateOfPay**](PayrollIncomeRateOfPay.md) |  | 
**pay_frequency** | None, str,  | NoneClass, str,  | The frequency at which an individual is paid. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

