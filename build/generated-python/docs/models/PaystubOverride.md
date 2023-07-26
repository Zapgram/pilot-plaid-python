# plaid.model.paystub_override.PaystubOverride

An object representing data from a paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing data from a paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**employer** | [**PaystubOverrideEmployer**](PaystubOverrideEmployer.md) | [**PaystubOverrideEmployer**](PaystubOverrideEmployer.md) |  | [optional] 
**employee** | [**PaystubOverrideEmployee**](PaystubOverrideEmployee.md) | [**PaystubOverrideEmployee**](PaystubOverrideEmployee.md) |  | [optional] 
**[income_breakdown](#income_breakdown)** | list, tuple,  | tuple,  |  | [optional] 
**pay_period_details** | [**PayPeriodDetails**](PayPeriodDetails.md) | [**PayPeriodDetails**](PayPeriodDetails.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# income_breakdown

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncomeBreakdown**](IncomeBreakdown.md) | [**IncomeBreakdown**](IncomeBreakdown.md) | [**IncomeBreakdown**](IncomeBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

