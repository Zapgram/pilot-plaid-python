# plaid.model.transfer_event_type.TransferEventType

The type of event that this transfer represents.  `pending`: A new transfer was created; it is in the pending state.  `cancelled`: The transfer was cancelled by the client.  `failed`: The transfer failed, no funds were moved.  `posted`: The transfer has been successfully submitted to the payment network.  `settled`: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account.  `returned`: A posted transfer was returned.  `swept`: The transfer was swept to / from the sweep account.  `swept_settled`: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account.  `return_swept`: Due to the transfer being returned, funds were pulled from or pushed back to the sweep account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The type of event that this transfer represents.  &#x60;pending&#x60;: A new transfer was created; it is in the pending state.  &#x60;cancelled&#x60;: The transfer was cancelled by the client.  &#x60;failed&#x60;: The transfer failed, no funds were moved.  &#x60;posted&#x60;: The transfer has been successfully submitted to the payment network.  &#x60;settled&#x60;: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account.  &#x60;returned&#x60;: A posted transfer was returned.  &#x60;swept&#x60;: The transfer was swept to / from the sweep account.  &#x60;swept_settled&#x60;: Credits are available to be withdrawn or debits have been deducted from the customer’s business checking account.  &#x60;return_swept&#x60;: Due to the transfer being returned, funds were pulled from or pushed back to the sweep account. | must be one of ["pending", "cancelled", "failed", "posted", "settled", "returned", "swept", "swept_settled", "return_swept", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

