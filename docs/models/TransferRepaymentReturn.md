# plaid.model.transfer_repayment_return.TransferRepaymentReturn

Represents a return on a Guaranteed ACH transfer that is included in the specified repayment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a return on a Guaranteed ACH transfer that is included in the specified repayment. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The value of the returned transfer. | 
**event_id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the corresponding &#x60;returned&#x60; transfer event. | 
**iso_currency_code** | str,  | str,  | The currency of the repayment, e.g. \&quot;USD\&quot;. | 
**transfer_id** | str,  | str,  | The unique identifier of the guaranteed transfer that was returned. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

