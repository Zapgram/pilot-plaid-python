# plaid.model.credit_bank_income.CreditBankIncome

The report of the Bank Income data for an end user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The report of the Bank Income data for an end user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bank_income_id** | str,  | str,  | The unique identifier associated with the Bank Income Report. | [optional] 
**generated_time** | str, datetime,  | str,  | The time when the Bank Income Report was generated. | [optional] value must conform to RFC-3339 date-time
**days_requested** | decimal.Decimal, int,  | decimal.Decimal,  | The number of days requested by the customer for the Bank Income Report. | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | The list of Items in the report along with the associated metadata about the Item. | [optional] 
**bank_income_summary** | [**CreditBankIncomeSummary**](CreditBankIncomeSummary.md) | [**CreditBankIncomeSummary**](CreditBankIncomeSummary.md) |  | [optional] 
**[warnings](#warnings)** | list, tuple,  | tuple,  | If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

The list of Items in the report along with the associated metadata about the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Items in the report along with the associated metadata about the Item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeItem**](CreditBankIncomeItem.md) | [**CreditBankIncomeItem**](CreditBankIncomeItem.md) | [**CreditBankIncomeItem**](CreditBankIncomeItem.md) |  | 

# warnings

If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeWarning**](CreditBankIncomeWarning.md) | [**CreditBankIncomeWarning**](CreditBankIncomeWarning.md) | [**CreditBankIncomeWarning**](CreditBankIncomeWarning.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

