# plaid.model.transaction_data.TransactionData

Information about the matched direct deposit transaction used to verify a user's payroll information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Information about the matched direct deposit transaction used to verify a user&#x27;s payroll information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, date,  | str,  | The date of the transaction, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\&quot;yyyy-mm-dd\&quot;). | value must conform to RFC-3339 full-date YYYY-MM-DD
**transaction_id** | str,  | str,  | A unique identifier for the transaction. | 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the transaction. | value must be a 64 bit float
**account_id** | str,  | str,  | A unique identifier for the end user&#x27;s account. | 
**description** | str,  | str,  | The description of the transaction. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

