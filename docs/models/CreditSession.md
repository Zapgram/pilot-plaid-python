# plaid.model.credit_session.CreditSession

Metadata and results for a Link session

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata and results for a Link session | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**link_session_id** | str,  | str,  | The unique identifier associated with the Link session. This identifier matches the &#x60;link_session_id&#x60; returned in the onSuccess/onExit callbacks. | [optional] 
**session_start_time** | str, datetime,  | str,  | The time when the Link session started | [optional] value must conform to RFC-3339 date-time
**results** | [**CreditSessionResults**](CreditSessionResults.md) | [**CreditSessionResults**](CreditSessionResults.md) |  | [optional] 
**[errors](#errors)** | list, tuple,  | tuple,  | The set of errors that occurred during the Link session. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

The set of errors that occurred during the Link session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of errors that occurred during the Link session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditSessionError**](CreditSessionError.md) | [**CreditSessionError**](CreditSessionError.md) | [**CreditSessionError**](CreditSessionError.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

