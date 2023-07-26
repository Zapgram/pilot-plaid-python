# plaid.model.credit_pay_stub_deductions.CreditPayStubDeductions

An object with the deduction information found on a pay stub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object with the deduction information found on a pay stub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | [**PayStubDeductionsTotal**](PayStubDeductionsTotal.md) | [**PayStubDeductionsTotal**](PayStubDeductionsTotal.md) |  | 
**[breakdown](#breakdown)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# breakdown

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PayStubDeductionsBreakdown**](PayStubDeductionsBreakdown.md) | [**PayStubDeductionsBreakdown**](PayStubDeductionsBreakdown.md) | [**PayStubDeductionsBreakdown**](PayStubDeductionsBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

