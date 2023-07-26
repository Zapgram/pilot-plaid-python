# plaid.model.auth_supported_methods.AuthSupportedMethods

Metadata specifically related to which auth methods an institution supports.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata specifically related to which auth methods an institution supports. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**automated_micro_deposits** | bool,  | BoolClass,  | Indicates if automated microdeposits are supported. | 
**instant_match** | bool,  | BoolClass,  | Indicates if instant match is supported. | 
**instant_auth** | bool,  | BoolClass,  | Indicates if instant auth is supported. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

