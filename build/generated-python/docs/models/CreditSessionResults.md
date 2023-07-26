# plaid.model.credit_session_results.CreditSessionResults

The set of results for a Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The set of results for a Link session. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[item_add_results](#item_add_results)** | list, tuple,  | tuple,  | The set of Item adds for the Link session. | [optional] 
**[bank_income_results](#bank_income_results)** | list, tuple,  | tuple,  | The set of bank income verifications for the Link session. | [optional] 
**[bank_employment_results](#bank_employment_results)** | list, tuple,  | tuple,  | The set of bank employment verifications for the Link session. | [optional] 
**[payroll_income_results](#payroll_income_results)** | list, tuple,  | tuple,  | The set of payroll income verifications for the Link session. | [optional] 
**document_income_results** | [**CreditSessionDocumentIncomeResult**](CreditSessionDocumentIncomeResult.md) | [**CreditSessionDocumentIncomeResult**](CreditSessionDocumentIncomeResult.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# item_add_results

The set of Item adds for the Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of Item adds for the Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditSessionItemAddResult**](CreditSessionItemAddResult.md) | [**CreditSessionItemAddResult**](CreditSessionItemAddResult.md) | [**CreditSessionItemAddResult**](CreditSessionItemAddResult.md) |  | 

# bank_income_results

The set of bank income verifications for the Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of bank income verifications for the Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditSessionBankIncomeResult**](CreditSessionBankIncomeResult.md) | [**CreditSessionBankIncomeResult**](CreditSessionBankIncomeResult.md) | [**CreditSessionBankIncomeResult**](CreditSessionBankIncomeResult.md) |  | 

# bank_employment_results

The set of bank employment verifications for the Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of bank employment verifications for the Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditSessionBankEmploymentResult**](CreditSessionBankEmploymentResult.md) | [**CreditSessionBankEmploymentResult**](CreditSessionBankEmploymentResult.md) | [**CreditSessionBankEmploymentResult**](CreditSessionBankEmploymentResult.md) |  | 

# payroll_income_results

The set of payroll income verifications for the Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of payroll income verifications for the Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditSessionPayrollIncomeResult**](CreditSessionPayrollIncomeResult.md) | [**CreditSessionPayrollIncomeResult**](CreditSessionPayrollIncomeResult.md) | [**CreditSessionPayrollIncomeResult**](CreditSessionPayrollIncomeResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

