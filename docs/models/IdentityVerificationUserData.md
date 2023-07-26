# plaid.model.identity_verification_user_data.IdentityVerificationUserData

The identity data that was either collected from the user or provided via API in order to perform an identity verification.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The identity data that was either collected from the user or provided via API in order to perform an identity verification. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id_number** | [**UserIDNumber**](UserIDNumber.md) | [**UserIDNumber**](UserIDNumber.md) |  | 
**address** | [**IdentityVerificationUserAddress**](IdentityVerificationUserAddress.md) | [**IdentityVerificationUserAddress**](IdentityVerificationUserAddress.md) |  | 
**email_address** | [**EmailAddressNullable**](EmailAddressNullable.md) | [**EmailAddressNullable**](EmailAddressNullable.md) |  | 
**date_of_birth** | [**ISO8601DateNullable**](ISO8601DateNullable.md) | [**ISO8601DateNullable**](ISO8601DateNullable.md) |  | 
**name** | [**IdentityVerificationResponseUserName**](IdentityVerificationResponseUserName.md) | [**IdentityVerificationResponseUserName**](IdentityVerificationResponseUserName.md) |  | 
**ip_address** | [**IPAddress**](IPAddress.md) | [**IPAddress**](IPAddress.md) |  | 
**phone_number** | [**IdentityVerificationUserPhoneNumber**](IdentityVerificationUserPhoneNumber.md) | [**IdentityVerificationUserPhoneNumber**](IdentityVerificationUserPhoneNumber.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

