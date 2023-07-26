# CreditBankIncome

The report of the Bank Income data for an end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_income_id** | **str** | The unique identifier associated with the Bank Income Report. | [optional] 
**generated_time** | **datetime** | The time when the Bank Income Report was generated. | [optional] 
**days_requested** | **int** | The number of days requested by the customer for the Bank Income Report. | [optional] 
**items** | [**[CreditBankIncomeItem]**](CreditBankIncomeItem.md) | The list of Items in the report along with the associated metadata about the Item. | [optional] 
**bank_income_summary** | [**CreditBankIncomeSummary**](CreditBankIncomeSummary.md) |  | [optional] 
**warnings** | [**[CreditBankIncomeWarning]**](CreditBankIncomeWarning.md) | If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


