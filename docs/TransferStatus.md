# TransferStatus

The status of the transfer.  `pending`: A new transfer was created; it is in the pending state. `posted`: The transfer has been successfully submitted to the payment network. `settled`: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account. `cancelled`: The transfer was cancelled by the client. `failed`: The transfer failed, no funds were moved. `returned`: A posted transfer was returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the transfer.  &#x60;pending&#x60;: A new transfer was created; it is in the pending state. &#x60;posted&#x60;: The transfer has been successfully submitted to the payment network. &#x60;settled&#x60;: Credits are available to be withdrawn or debits have been deducted from the Plaid linked account. &#x60;cancelled&#x60;: The transfer was cancelled by the client. &#x60;failed&#x60;: The transfer failed, no funds were moved. &#x60;returned&#x60;: A posted transfer was returned. |  must be one of ["pending", "posted", "settled", "cancelled", "failed", "returned", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


