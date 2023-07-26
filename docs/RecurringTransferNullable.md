# RecurringTransferNullable

Represents a recurring transfer within the Transfers API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring_transfer_id** | **str** | Plaid’s unique identifier for a recurring transfer. | 
**created** | **datetime** | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**next_origination_date** | **date, none_type** | A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  The next transfer origination date after bank holiday adjustment. | 
**type** | [**TransferType**](TransferType.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**status** | [**TransferRecurringStatus**](TransferRecurringStatus.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | 
**funding_account_id** | **str** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**description** | **str** | The description of the recurring transfer. | 
**transfer_ids** | **[str]** |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**schedule** | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) |  | 
**test_clock_id** | **str, none_type** | Plaid’s unique identifier for a test clock. | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


