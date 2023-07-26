# plaid.model.income_verification_precheck_user.IncomeVerificationPrecheckUser

Information about the user whose eligibility is being evaluated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Information about the user whose eligibility is being evaluated. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**first_name** | None, str,  | NoneClass, str,  | The user&#x27;s first name | [optional] 
**last_name** | None, str,  | NoneClass, str,  | The user&#x27;s last name | [optional] 
**email_address** | None, str,  | NoneClass, str,  | The user&#x27;s email address | [optional] 
**home_address** | [**SignalAddressData**](SignalAddressData.md) | [**SignalAddressData**](SignalAddressData.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

