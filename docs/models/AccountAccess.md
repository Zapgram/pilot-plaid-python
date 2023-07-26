# plaid.model.account_access.AccountAccess

Allow or disallow product access by account. Unlisted (e.g. missing) accounts will be considered `new_accounts`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Allow or disallow product access by account. Unlisted (e.g. missing) accounts will be considered &#x60;new_accounts&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**unique_id** | str,  | str,  | The unique account identifier for this account. This value must match that returned by the data access API for this account. | 
**authorized** | None, bool,  | NoneClass, BoolClass,  | Allow the application to see this account (and associated details, including balance) in the list of accounts  If unset, defaults to &#x60;true&#x60;. | [optional] if omitted the server will use the default value of True
**account_product_access** | [**AccountProductAccessNullable**](AccountProductAccessNullable.md) | [**AccountProductAccessNullable**](AccountProductAccessNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

