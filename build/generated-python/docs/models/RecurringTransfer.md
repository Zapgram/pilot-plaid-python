# plaid.model.recurring_transfer.RecurringTransfer

Represents a recurring transfer within the Transfers API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a recurring transfer within the Transfers API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**[transfer_ids](#transfer_ids)** | list, tuple,  | tuple,  |  | 
**created** | str, datetime,  | str,  | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | value must conform to RFC-3339 date-time
**description** | str,  | str,  | The description of the recurring transfer. | 
**type** | [**TransferType**](TransferType.md) | [**TransferType**](TransferType.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) | [**TransferNetwork**](TransferNetwork.md) |  | 
**funding_account_id** | str,  | str,  | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**schedule** | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) |  | 
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | 
**next_origination_date** | None, str, date,  | NoneClass, str,  | A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  The next transfer origination date after bank holiday adjustment. | value must conform to RFC-3339 full-date YYYY-MM-DD
**iso_currency_code** | str,  | str,  | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**origination_account_id** | str,  | str,  | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**recurring_transfer_id** | str,  | str,  | Plaid’s unique identifier for a recurring transfer. | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**status** | [**TransferRecurringStatus**](TransferRecurringStatus.md) | [**TransferRecurringStatus**](TransferRecurringStatus.md) |  | 
**test_clock_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for a test clock. | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transfer_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Plaid’s unique identifier for a transfer. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

