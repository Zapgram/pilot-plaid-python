# plaid.model.transfer_refund_status.TransferRefundStatus

The status of the refund.  `pending`: A new refund was created; it is in the pending state. `posted`: The refund has been successfully submitted to the payment network. `cancelled`: The refund was cancelled by the client. `failed`: The refund failed or was returned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The status of the refund.  &#x60;pending&#x60;: A new refund was created; it is in the pending state. &#x60;posted&#x60;: The refund has been successfully submitted to the payment network. &#x60;cancelled&#x60;: The refund was cancelled by the client. &#x60;failed&#x60;: The refund failed or was returned. | must be one of ["pending", "posted", "cancelled", "failed", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

