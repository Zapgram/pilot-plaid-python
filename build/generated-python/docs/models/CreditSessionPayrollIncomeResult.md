# plaid.model.credit_session_payroll_income_result.CreditSessionPayrollIncomeResult

The details of a digital payroll income verification in Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details of a digital payroll income verification in Link | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**num_paystubs_retrieved** | decimal.Decimal, int,  | decimal.Decimal,  | The number of paystubs retrieved from a payroll provider. | [optional] 
**num_w2s_retrieved** | decimal.Decimal, int,  | decimal.Decimal,  | The number of w2s retrieved from a payroll provider. | [optional] 
**institution_id** | str,  | str,  | The Plaid Institution ID associated with the Item. | [optional] 
**institution_name** | str,  | str,  | The Institution Name associated with the Item. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

