# plaid.model.identity_verification_create_request.IdentityVerificationCreateRequest

Request schema for '/identity_verification/create'

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request schema for &#x27;/identity_verification/create&#x27; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gave_consent** | bool,  | BoolClass,  | A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be shared with Plaid for verification purposes.  If &#x60;gave_consent&#x60; is set to &#x60;true&#x60;, the &#x60;accept_tos&#x60; step will be marked as &#x60;skipped&#x60; and the end user&#x27;s session will start at the next step requirement. | if omitted the server will use the default value of False
**is_shareable** | bool,  | BoolClass,  | A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created. | 
**template_id** | str,  | str,  | ID of the associated Identity Verification template. | 
**client_user_id** | [**ClientUserID**](ClientUserID.md) | [**ClientUserID**](ClientUserID.md) |  | [optional] 
**user** | [**IdentityVerificationCreateRequestUser**](IdentityVerificationCreateRequestUser.md) | [**IdentityVerificationCreateRequestUser**](IdentityVerificationCreateRequestUser.md) |  | [optional] 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**is_idempotent** | [**IdempotencyFlag**](IdempotencyFlag.md) | [**IdempotencyFlag**](IdempotencyFlag.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

