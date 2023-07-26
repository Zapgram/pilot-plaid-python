# plaid.model.credit_bank_employment_report.CreditBankEmploymentReport

The report of the Bank Employment data for an end user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The report of the Bank Employment data for an end user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[warnings](#warnings)** | list, tuple,  | tuple,  | If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | 
**bank_employment_report_id** | str,  | str,  | The unique identifier associated with the Bank Employment Report. | 
**[items](#items)** | list, tuple,  | tuple,  | The list of Items in the report along with the associated metadata about the Item. | 
**generated_time** | str, datetime,  | str,  | The time when the Bank Employment Report was generated, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \&quot;2018-04-12T03:32:11Z\&quot;). | value must conform to RFC-3339 date-time
**days_requested** | decimal.Decimal, int,  | decimal.Decimal,  | The number of days requested by the customer for the Bank Employment Report. | 
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
[**CreditBankEmploymentItem**](CreditBankEmploymentItem.md) | [**CreditBankEmploymentItem**](CreditBankEmploymentItem.md) | [**CreditBankEmploymentItem**](CreditBankEmploymentItem.md) |  | 

# warnings

If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankEmploymentWarning**](CreditBankEmploymentWarning.md) | [**CreditBankEmploymentWarning**](CreditBankEmploymentWarning.md) | [**CreditBankEmploymentWarning**](CreditBankEmploymentWarning.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

