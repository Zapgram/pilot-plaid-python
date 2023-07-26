# plaid.model.credit_pay_stub_earnings.CreditPayStubEarnings

An object representing both a breakdown of earnings on a pay stub and the total earnings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing both a breakdown of earnings on a pay stub and the total earnings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total** | [**PayStubEarningsTotal**](PayStubEarningsTotal.md) | [**PayStubEarningsTotal**](PayStubEarningsTotal.md) |  | 
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
[**PayStubEarningsBreakdown**](PayStubEarningsBreakdown.md) | [**PayStubEarningsBreakdown**](PayStubEarningsBreakdown.md) | [**PayStubEarningsBreakdown**](PayStubEarningsBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

