# plaid.model.credit_session_error.CreditSessionError

The details of a Link error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details of a Link error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error_type** | str,  | str,  | A broad categorization of the error. | [optional] 
**error_code** | str,  | str,  | The particular error code. | [optional] 
**error_message** | str,  | str,  | A developer-friendly representation of the error code. | [optional] 
**display_message** | None, str,  | NoneClass, str,  | A user-friendly representation of the error code. &#x60;null&#x60; if the error is not related to user action. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

