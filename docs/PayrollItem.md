# PayrollItem

An object containing information about the payroll item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**institution_id** | **str** | The unique identifier of the institution associated with the Item. | 
**institution_name** | **str** | The name of the institution associated with the Item. | 
**accounts** | [**[PayrollIncomeAccountData]**](PayrollIncomeAccountData.md) |  | 
**payroll_income** | [**[PayrollIncomeObject]**](PayrollIncomeObject.md) |  | 
**status** | [**PayrollItemStatus**](PayrollItemStatus.md) |  | 
**updated_at** | **datetime, none_type** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the Item was updated. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


