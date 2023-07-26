# CreditBankIncomeSource

Detailed information for the income source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**income_source_id** | **str** | A unique identifier for an income source. | [optional] 
**income_description** | **str** | The most common name or original description for the underlying income transactions. | [optional] 
**income_category** | [**CreditBankIncomeCategory**](CreditBankIncomeCategory.md) |  | [optional] 
**account_id** | **str** | Plaid&#39;s unique identifier for the account. | [optional] 
**start_date** | **date** | Minimum of all dates within the specific income sources in the user&#39;s bank account for days requested by the client. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**end_date** | **date** | Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**pay_frequency** | [**CreditBankIncomePayFrequency**](CreditBankIncomePayFrequency.md) |  | [optional] 
**total_amount** | **float** | Total amount of earnings in the user’s bank account for the specific income source for days requested by the client. | [optional] 
**transaction_count** | **int** | Number of transactions for the income source within the start and end date. | [optional] 
**historical_summary** | [**[CreditBankIncomeHistoricalSummary]**](CreditBankIncomeHistoricalSummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


