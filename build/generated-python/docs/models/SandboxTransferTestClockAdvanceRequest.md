# plaid.model.sandbox_transfer_test_clock_advance_request.SandboxTransferTestClockAdvanceRequest

Defines the request schema for `/sandbox/transfer/test_clock/advance`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/sandbox/transfer/test_clock/advance&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**test_clock_id** | str,  | str,  | Plaid’s unique identifier for a test clock. | 
**new_virtual_time** | str, datetime,  | str,  | The virtual timestamp on the test clock. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | value must conform to RFC-3339 date-time
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
