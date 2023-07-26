# CreditBankIncomeItem

The details and metadata for an end user's Item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_income_accounts** | [**[CreditBankIncomeAccount]**](CreditBankIncomeAccount.md) | The Item&#39;s accounts that have Bank Income data. | [optional] 
**bank_income_sources** | [**[CreditBankIncomeSource]**](CreditBankIncomeSource.md) | The income sources for this Item. Each entry in the array is a single income source. | [optional] 
**last_updated_time** | **datetime** | The time when this Item&#39;s data was last retrieved from the financial institution. | [optional] 
**institution_id** | **str** | The unique identifier of the institution associated with the Item. | [optional] 
**institution_name** | **str** | The name of the institution associated with the Item. | [optional] 
**item_id** | **str** | The unique identifier for the Item. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


