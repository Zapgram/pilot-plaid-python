# plaid.model.signal_person_name.SignalPersonName

The user's legal name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The user&#x27;s legal name | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**prefix** | None, str,  | NoneClass, str,  | The user&#x27;s name prefix (e.g. \&quot;Mr.\&quot;) | [optional] 
**given_name** | None, str,  | NoneClass, str,  | The user&#x27;s given name. If the user has a one-word name, it should be provided in this field. | [optional] 
**middle_name** | None, str,  | NoneClass, str,  | The user&#x27;s middle name | [optional] 
**family_name** | None, str,  | NoneClass, str,  | The user&#x27;s family name / surname | [optional] 
**suffix** | None, str,  | NoneClass, str,  | The user&#x27;s name suffix (e.g. \&quot;II\&quot;) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

