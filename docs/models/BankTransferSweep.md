# plaid.model.bank_transfer_sweep.BankTransferSweep

BankTransferSweep describes a sweep transfer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | BankTransferSweep describes a sweep transfer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The amount of the sweep. | 
**iso_currency_code** | str,  | str,  | The currency of the sweep, e.g. \&quot;USD\&quot;. | 
**created_at** | str, datetime,  | str,  | The datetime when the sweep occurred, in RFC 3339 format. | value must conform to RFC-3339 date-time
**id** | str,  | str,  | Identifier of the sweep. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

