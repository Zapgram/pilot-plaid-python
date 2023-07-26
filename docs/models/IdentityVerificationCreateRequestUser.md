# plaid.model.identity_verification_create_request_user.IdentityVerificationCreateRequestUser

User information collected outside of Link, most likely via your own onboarding process.  Each of the following identity fields are optional:  `email_address`  `phone_number`  `date_of_birth`  `name`  `address`  `id_number`  Specifically, these fields are optional in that they can either be fully provided (satisfying every required field in their subschema) or omitted from the request entirely by not providing the key or value. Providing these fields via the API will result in Link skipping the data collection process for the associated user. All verification steps enabled in the associated Identity Verification Template will still be run. Verification steps will either be run immediately, or once the user completes the `accept_tos` step, depending on the value provided to the `gave_consent` field. If you are not using the shareable URL feature, you can optionally provide these fields via `/link/token/create` instead; both `/identity_verification/create` and `/link/token/create` are valid ways to provide this information. Note that if you provide a non-`null` user data object via `/identity_verification/create`, any user data fields entered via `/link/token/create` for the same `client_user_id` will be ignored when prefilling Link.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | User information collected outside of Link, most likely via your own onboarding process.  Each of the following identity fields are optional:  &#x60;email_address&#x60;  &#x60;phone_number&#x60;  &#x60;date_of_birth&#x60;  &#x60;name&#x60;  &#x60;address&#x60;  &#x60;id_number&#x60;  Specifically, these fields are optional in that they can either be fully provided (satisfying every required field in their subschema) or omitted from the request entirely by not providing the key or value. Providing these fields via the API will result in Link skipping the data collection process for the associated user. All verification steps enabled in the associated Identity Verification Template will still be run. Verification steps will either be run immediately, or once the user completes the &#x60;accept_tos&#x60; step, depending on the value provided to the &#x60;gave_consent&#x60; field. If you are not using the shareable URL feature, you can optionally provide these fields via &#x60;/link/token/create&#x60; instead; both &#x60;/identity_verification/create&#x60; and &#x60;/link/token/create&#x60; are valid ways to provide this information. Note that if you provide a non-&#x60;null&#x60; user data object via &#x60;/identity_verification/create&#x60;, any user data fields entered via &#x60;/link/token/create&#x60; for the same &#x60;client_user_id&#x60; will be ignored when prefilling Link. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email_address** | str,  | str,  | A valid email address. | [optional] 
**phone_number** | [**IdentityVerificationUserPhoneNumber**](IdentityVerificationUserPhoneNumber.md) | [**IdentityVerificationUserPhoneNumber**](IdentityVerificationUserPhoneNumber.md) |  | [optional] 
**date_of_birth** | str, date,  | str,  | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**name** | [**IdentityVerificationRequestUserName**](IdentityVerificationRequestUserName.md) | [**IdentityVerificationRequestUserName**](IdentityVerificationRequestUserName.md) |  | [optional] 
**address** | [**UserAddress**](UserAddress.md) | [**UserAddress**](UserAddress.md) |  | [optional] 
**id_number** | [**UserIDNumber**](UserIDNumber.md) | [**UserIDNumber**](UserIDNumber.md) |  | [optional] 
**client_user_id** | [**DeprecatedClientUserID**](DeprecatedClientUserID.md) | [**DeprecatedClientUserID**](DeprecatedClientUserID.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
