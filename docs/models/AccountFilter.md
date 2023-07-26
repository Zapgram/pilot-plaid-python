# plaid.model.account_filter.AccountFilter

Enumerates the account subtypes that the application wishes for the user to be able to select from. For more details refer to Plaid documentation on account filters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Enumerates the account subtypes that the application wishes for the user to be able to select from. For more details refer to Plaid documentation on account filters. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**depository** | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) |  | [optional] 
**credit** | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) |  | [optional] 
**loan** | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) |  | [optional] 
**investment** | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) | [**AccountFilterSubtypes**](AccountFilterSubtypes.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

