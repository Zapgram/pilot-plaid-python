# plaid.model.transfer_recurring_schedule.TransferRecurringSchedule

The schedule that the recurring transfer will be executed on.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The schedule that the recurring transfer will be executed on. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**interval_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of recurring &#x60;interval_units&#x60; between originations. The recurring interval(before holiday adjustment) is calculated by multiplying &#x60;interval_unit&#x60; and &#x60;interval_count&#x60;. For instance, to schedule a recurring transfer which originates once every two weeks, set &#x60;interval_unit&#x60; &#x3D; &#x60;week&#x60; and &#x60;interval_count&#x60; &#x3D; 2. | 
**interval_unit** | [**TransferScheduleIntervalUnit**](TransferScheduleIntervalUnit.md) | [**TransferScheduleIntervalUnit**](TransferScheduleIntervalUnit.md) |  | 
**interval_execution_day** | decimal.Decimal, int,  | decimal.Decimal,  | The day of the interval on which to schedule the transfer.  If the &#x60;interval_unit&#x60; is &#x60;week&#x60;, &#x60;interval_execution_day&#x60; should be an integer from 1 (Monday) to 5 (Friday).  If the &#x60;interval_unit&#x60; is &#x60;month&#x60;, &#x60;interval_execution_day&#x60; should be an integer indicating which day of the month to make the transfer on. Integers from 1 to 28 can be used to make a transfer on that day of the month. Negative integers from -1 to -5 can be used to make a transfer relative to the end of the month. To make a transfer on the last day of the month, use -1; to make the transfer on the second-to-last day, use -2, and so on.  The transfer will be originated on next available banking day if the designated day is a non banking day. | 
**start_date** | str, date,  | str,  | A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). The recurring transfer will begin on the first &#x60;interval_execution_day&#x60; on or after the &#x60;start_date&#x60;.  If the first &#x60;interval_execution_day&#x60; on or after the start date is also the same day that &#x60;/transfer/recurring/create&#x60; was called, the bank *may* make the first payment on that day, but it is not guaranteed to do so. | value must conform to RFC-3339 full-date YYYY-MM-DD
**end_date** | None, str, date,  | NoneClass, str,  | A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). The recurring transfer will end on the last &#x60;interval_execution_day&#x60; on or before the &#x60;end_date&#x60;. If the &#x60;interval_execution_day&#x60; between the start date and the end date (inclusive) is also the same day that &#x60;/transfer/recurring/create&#x60; was called, the bank *may* make a payment on that day, but it is not guaranteed to do so. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

