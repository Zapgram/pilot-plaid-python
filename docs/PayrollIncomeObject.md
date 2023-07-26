# PayrollIncomeObject

An object representing payroll data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | ID of the payroll provider account. | 
**pay_stubs** | [**[CreditPayStub]**](CreditPayStub.md) | Array of pay stubs for the user. | 
**w2s** | [**[CreditW2]**](CreditW2.md) | Array of tax form W-2s. | 
**form1099s** | [**[Credit1099]**](Credit1099.md) | Array of tax form 1099s. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


