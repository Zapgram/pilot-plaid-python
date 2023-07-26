# plaid.model.income_verification_precheck_military_info.IncomeVerificationPrecheckMilitaryInfo

Data about military info in the income verification precheck.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Data about military info in the income verification precheck. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_active_duty** | None, bool,  | NoneClass, BoolClass,  | Is the user currently active duty in the US military | [optional] 
**branch** | None, str,  | NoneClass, str,  | If the user is currently serving in the US military, the branch of the military in which they are serving Valid values: &#x27;AIR FORCE&#x27;, &#x27;ARMY&#x27;, &#x27;COAST GUARD&#x27;, &#x27;MARINES&#x27;, &#x27;NAVY&#x27;, &#x27;UNKNOWN&#x27; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

