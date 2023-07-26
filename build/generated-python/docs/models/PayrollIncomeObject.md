# plaid.model.payroll_income_object.PayrollIncomeObject

An object representing payroll data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing payroll data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[pay_stubs](#pay_stubs)** | list, tuple,  | tuple,  | Array of pay stubs for the user. | 
**account_id** | None, str,  | NoneClass, str,  | ID of the payroll provider account. | 
**[form1099s](#form1099s)** | list, tuple,  | tuple,  | Array of tax form 1099s. | 
**[w2s](#w2s)** | list, tuple,  | tuple,  | Array of tax form W-2s. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pay_stubs

Array of pay stubs for the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of pay stubs for the user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditPayStub**](CreditPayStub.md) | [**CreditPayStub**](CreditPayStub.md) | [**CreditPayStub**](CreditPayStub.md) |  | 

# w2s

Array of tax form W-2s.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of tax form W-2s. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditW2**](CreditW2.md) | [**CreditW2**](CreditW2.md) | [**CreditW2**](CreditW2.md) |  | 

# form1099s

Array of tax form 1099s.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of tax form 1099s. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Credit1099**](Credit1099.md) | [**Credit1099**](Credit1099.md) | [**Credit1099**](Credit1099.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

