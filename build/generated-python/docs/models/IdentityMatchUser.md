# plaid.model.identity_match_user.IdentityMatchUser

The user's legal name, phone number, email address and address used to perform fuzzy match. If Financial Account Matching is enabled in the Identity Verification product, leave this field empty to automatically match against PII collected from the Identity Verification checks.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The user&#x27;s legal name, phone number, email address and address used to perform fuzzy match. If Financial Account Matching is enabled in the Identity Verification product, leave this field empty to automatically match against PII collected from the Identity Verification checks. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**legal_name** | None, str,  | NoneClass, str,  | The user&#x27;s full legal name. | [optional] 
**phone_number** | None, str,  | NoneClass, str,  | The user&#x27;s phone number, in E.164 format: +{countrycode}{number}. For example: \&quot;+14151234567\&quot;. Phone numbers provided in other formats will be parsed on a best-effort basis. | [optional] 
**email_address** | None, str,  | NoneClass, str,  | The user&#x27;s email address. | [optional] 
**address** | [**AddressDataNullable**](AddressDataNullable.md) | [**AddressDataNullable**](AddressDataNullable.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

