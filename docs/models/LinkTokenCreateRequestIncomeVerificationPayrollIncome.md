# plaid.model.link_token_create_request_income_verification_payroll_income.LinkTokenCreateRequestIncomeVerificationPayrollIncome

Specifies options for initializing Link for use with Payroll Income.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with Payroll Income. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[flow_types](#flow_types)** | list, tuple, None,  | tuple, NoneClass,  | The types of payroll income verification to enable for the Link session. If none are specified, then users will see both document and digital payroll income. | [optional] 
**is_update_mode** | bool,  | BoolClass,  | An identifier to indicate whether the income verification Link token will be used for an update or not | [optional] if omitted the server will use the default value of False
**item_id_to_update** | None, str,  | NoneClass, str,  | Uniquely identify a payroll income item to update with. It should only be used for update mode. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flow_types

The types of payroll income verification to enable for the Link session. If none are specified, then users will see both document and digital payroll income.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The types of payroll income verification to enable for the Link session. If none are specified, then users will see both document and digital payroll income. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncomeVerificationPayrollFlowType**](IncomeVerificationPayrollFlowType.md) | [**IncomeVerificationPayrollFlowType**](IncomeVerificationPayrollFlowType.md) | [**IncomeVerificationPayrollFlowType**](IncomeVerificationPayrollFlowType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

