# plaid.model.sandbox_public_token_create_request_options.SandboxPublicTokenCreateRequestOptions

An optional set of options to be used when configuring the Item. If specified, must not be `null`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional set of options to be used when configuring the Item. If specified, must not be &#x60;null&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**webhook** | str,  | str,  | Specify a webhook to associate with the new Item. | [optional] 
**override_username** | [**SandboxOverrideUsername**](SandboxOverrideUsername.md) | [**SandboxOverrideUsername**](SandboxOverrideUsername.md) |  | [optional] 
**override_password** | [**SandboxOverridePassword**](SandboxOverridePassword.md) | [**SandboxOverridePassword**](SandboxOverridePassword.md) |  | [optional] 
**transactions** | [**SandboxPublicTokenCreateRequestOptionsTransactions**](SandboxPublicTokenCreateRequestOptionsTransactions.md) | [**SandboxPublicTokenCreateRequestOptionsTransactions**](SandboxPublicTokenCreateRequestOptionsTransactions.md) |  | [optional] 
**income_verification** | [**SandboxPublicTokenCreateRequestOptionsIncomeVerification**](SandboxPublicTokenCreateRequestOptionsIncomeVerification.md) | [**SandboxPublicTokenCreateRequestOptionsIncomeVerification**](SandboxPublicTokenCreateRequestOptionsIncomeVerification.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

