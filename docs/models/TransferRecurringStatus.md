# plaid.model.transfer_recurring_status.TransferRecurringStatus

The status of the recurring transfer.  `active`: The recurring transfer is currently active. `cancelled`: The recurring transfer was cancelled by the client or Plaid. `expired`: The recurring transfer has completed all originations according to its recurring schedule.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The status of the recurring transfer.  &#x60;active&#x60;: The recurring transfer is currently active. &#x60;cancelled&#x60;: The recurring transfer was cancelled by the client or Plaid. &#x60;expired&#x60;: The recurring transfer has completed all originations according to its recurring schedule. | must be one of ["active", "cancelled", "expired", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

