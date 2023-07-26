# CreditBankEmploymentItem

The details and metadata for an end user's Item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The unique identifier for the Item. | 
**last_updated_time** | **datetime** | The time when this Item&#39;s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \&quot;2018-04-12T03:32:11Z\&quot;). | 
**institution_id** | **str** | The unique identifier of the institution associated with the Item. | 
**institution_name** | **str** | The name of the institution associated with the Item. | 
**bank_employments** | [**[CreditBankEmployment]**](CreditBankEmployment.md) | The bank employment information for this Item. Each entry in the array is a different employer found. | 
**bank_employment_accounts** | [**[CreditBankIncomeAccount]**](CreditBankIncomeAccount.md) | The Item&#39;s accounts that have Bank Employment data. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


