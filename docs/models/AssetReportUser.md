# plaid.model.asset_report_user.AssetReportUser

The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The &#x60;first_name&#x60;, &#x60;last_name&#x60;, and &#x60;ssn&#x60; fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_user_id** | None, str,  | NoneClass, str,  | An identifier you determine and submit for the user. | [optional] 
**first_name** | None, str,  | NoneClass, str,  | The user&#x27;s first name. Required for the Fannie Mae Day 1 Certainty™ program. | [optional] 
**middle_name** | None, str,  | NoneClass, str,  | The user&#x27;s middle name | [optional] 
**last_name** | None, str,  | NoneClass, str,  | The user&#x27;s last name.  Required for the Fannie Mae Day 1 Certainty™ program. | [optional] 
**ssn** | None, str,  | NoneClass, str,  | The user&#x27;s Social Security Number. Required for the Fannie Mae Day 1 Certainty™ program.  Format: \&quot;ddd-dd-dddd\&quot; | [optional] 
**phone_number** | None, str,  | NoneClass, str,  | The user&#x27;s phone number, in E.164 format: +{countrycode}{number}. For example: \&quot;+14151234567\&quot;. Phone numbers provided in other formats will be parsed on a best-effort basis. | [optional] 
**email** | None, str,  | NoneClass, str,  | The user&#x27;s email address. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

