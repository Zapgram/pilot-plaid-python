# CreditPayrollIncomeGetResponse

Defines the response body for `/credit/payroll_income/get`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[PayrollItem]**](PayrollItem.md) | Array of payroll items. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


