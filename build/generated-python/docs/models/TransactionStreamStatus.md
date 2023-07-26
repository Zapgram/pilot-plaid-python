# plaid.model.transaction_stream_status.TransactionStreamStatus

The current status of the transaction stream.  `MATURE`: A `MATURE` recurring stream should have at least 3 transactions and happen on a regular cadence (For Annual recurring stream, we will mark it `MATURE` after 2 instances).  `EARLY_DETECTION`: When a recurring transaction first appears in the transaction history and before it fulfills the requirement of a mature stream, the status will be `EARLY_DETECTION`.  `TOMBSTONED`: A stream that was previously in the `EARLY_DETECTION` status will move to the `TOMBSTONED` status when no further transactions were found at the next expected date.  `UNKNOWN`: A stream is assigned an `UNKNOWN` status when none of the other statuses are applicable.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The current status of the transaction stream.  &#x60;MATURE&#x60;: A &#x60;MATURE&#x60; recurring stream should have at least 3 transactions and happen on a regular cadence (For Annual recurring stream, we will mark it &#x60;MATURE&#x60; after 2 instances).  &#x60;EARLY_DETECTION&#x60;: When a recurring transaction first appears in the transaction history and before it fulfills the requirement of a mature stream, the status will be &#x60;EARLY_DETECTION&#x60;.  &#x60;TOMBSTONED&#x60;: A stream that was previously in the &#x60;EARLY_DETECTION&#x60; status will move to the &#x60;TOMBSTONED&#x60; status when no further transactions were found at the next expected date.  &#x60;UNKNOWN&#x60;: A stream is assigned an &#x60;UNKNOWN&#x60; status when none of the other statuses are applicable. | must be one of ["UNKNOWN", "MATURE", "EARLY_DETECTION", "TOMBSTONED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

