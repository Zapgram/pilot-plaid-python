# LinkTokenCreateRequestIncomeVerificationPayrollIncome

Specifies options for initializing Link for use with Payroll Income.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_types** | [**[IncomeVerificationPayrollFlowType], none_type**](IncomeVerificationPayrollFlowType.md) | The types of payroll income verification to enable for the Link session. If none are specified, then users will see both document and digital payroll income. | [optional] 
**is_update_mode** | **bool** | An identifier to indicate whether the income verification Link token will be used for an update or not | [optional]  if omitted the server will use the default value of False
**item_id_to_update** | **str, none_type** | Uniquely identify a payroll income item to update with. It should only be used for update mode. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


