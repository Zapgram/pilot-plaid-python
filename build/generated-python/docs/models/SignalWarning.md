# plaid.model.signal_warning.SignalWarning

Conveys information about the errors causing missing or stale bank data used to construct the /signal/evaluate scores and response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Conveys information about the errors causing missing or stale bank data used to construct the /signal/evaluate scores and response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**warning_type** | str,  | str,  | A broad categorization of the warning. Safe for programmatic use. | [optional] 
**warning_code** | str,  | str,  | The warning code identifies a specific kind of warning that pertains to the error causing bank data to be missing. Safe for programmatic use. For more details on warning codes, please refer to Plaid standard error codes documentation. In case you receive the &#x60;ITEM_LOGIN_REQUIRED&#x60; warning, we recommend re-authenticating your user by implementing Link&#x27;s update mode. This will guide your user to fix their credentials, allowing Plaid to start fetching data again for future Signal requests. | [optional] 
**warning_message** | str,  | str,  | A developer-friendly representation of the warning type. This may change over time and is not safe for programmatic use. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

