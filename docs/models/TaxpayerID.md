# plaid.model.taxpayer_id.TaxpayerID

Taxpayer ID of the individual receiving the paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Taxpayer ID of the individual receiving the paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id_type** | None, str,  | NoneClass, str,  | Type of ID, e.g. &#x27;SSN&#x27; | [optional] 
**id_mask** | None, str,  | NoneClass, str,  | ID mask; i.e. last 4 digits of the taxpayer ID | [optional] 
**last_4_digits** | None, str,  | NoneClass, str,  | Last 4 digits of unique number of ID. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

