# CreditBankEmploymentReport

The report of the Bank Employment data for an end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_employment_report_id** | **str** | The unique identifier associated with the Bank Employment Report. | 
**generated_time** | **datetime** | The time when the Bank Employment Report was generated, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \&quot;2018-04-12T03:32:11Z\&quot;). | 
**days_requested** | **int** | The number of days requested by the customer for the Bank Employment Report. | 
**items** | [**[CreditBankEmploymentItem]**](CreditBankEmploymentItem.md) | The list of Items in the report along with the associated metadata about the Item. | 
**warnings** | [**[CreditBankEmploymentWarning]**](CreditBankEmploymentWarning.md) | If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


