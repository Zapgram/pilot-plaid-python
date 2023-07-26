# plaid.model.payroll_income_rate_of_pay.PayrollIncomeRateOfPay

An object representing the rate at which an individual is paid.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the rate at which an individual is paid. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pay_rate** | None, str,  | NoneClass, str,  | The rate at which an employee is paid. | [optional] 
**pay_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount at which an employee is paid. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

