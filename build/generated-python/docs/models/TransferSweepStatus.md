# plaid.model.transfer_sweep_status.TransferSweepStatus

The status of the sweep for the transfer.  `unswept`: The transfer hasn't been swept yet. `swept`: The transfer was swept to the sweep account. `swept_settled`: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account. `return_swept`: The transfer was returned, funds were pulled back or pushed back to the sweep account. `null`: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being swept)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  | The status of the sweep for the transfer.  &#x60;unswept&#x60;: The transfer hasn&#x27;t been swept yet. &#x60;swept&#x60;: The transfer was swept to the sweep account. &#x60;swept_settled&#x60;: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account. &#x60;return_swept&#x60;: The transfer was returned, funds were pulled back or pushed back to the sweep account. &#x60;null&#x60;: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being swept) | must be one of [None, "unswept", "swept", "swept_settled", "return_swept", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

