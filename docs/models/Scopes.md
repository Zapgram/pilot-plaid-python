# plaid.model.scopes.Scopes

The scopes object

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The scopes object | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**product_access** | [**ProductAccess**](ProductAccess.md) | [**ProductAccess**](ProductAccess.md) |  | [optional] 
**[accounts](#accounts)** | list, tuple,  | tuple,  |  | [optional] 
**new_accounts** | None, bool,  | NoneClass, BoolClass,  | Allow access to newly opened accounts as they are opened. If unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AccountAccess**](AccountAccess.md) | [**AccountAccess**](AccountAccess.md) | [**AccountAccess**](AccountAccess.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

