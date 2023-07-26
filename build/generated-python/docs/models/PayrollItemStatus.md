# plaid.model.payroll_item_status.PayrollItemStatus

Details about the status of the payroll item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Details about the status of the payroll item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**processing_status** | None, str,  | NoneClass, str,  | Denotes the processing status for the verification.  &#x60;UNKNOWN&#x60;: The processing status could not be determined.  &#x60;PROCESSING_COMPLETE&#x60;: The processing has completed and the user has approved for sharing. The data is available to be retrieved.  &#x60;PROCESSING&#x60;: The verification is still processing. The data is not available yet.  &#x60;FAILED&#x60;: The processing failed to complete successfully.  &#x60;APPROVAL_STATUS_PENDING&#x60;: The processing has completed but the user has not yet approved the sharing of the data. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

