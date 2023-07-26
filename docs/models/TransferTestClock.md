# plaid.model.transfer_test_clock.TransferTestClock

Defines the test clock for a transfer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the test clock for a transfer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**virtual_time** | str, datetime,  | str,  | The virtual timestamp on the test clock. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | value must conform to RFC-3339 date-time
**test_clock_id** | str,  | str,  | Plaid’s unique identifier for a test clock. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

