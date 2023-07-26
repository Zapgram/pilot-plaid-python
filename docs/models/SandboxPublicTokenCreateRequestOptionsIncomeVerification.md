# plaid.model.sandbox_public_token_create_request_options_income_verification.SandboxPublicTokenCreateRequestOptionsIncomeVerification

A set of parameters for income verification options. This field is required if `income_verification` is included in the `initial_products` array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of parameters for income verification options. This field is required if &#x60;income_verification&#x60; is included in the &#x60;initial_products&#x60; array. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[income_source_types](#income_source_types)** | list, tuple,  | tuple,  | The types of source income data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | [optional] 
**bank_income** | [**SandboxPublicTokenCreateRequestIncomeVerificationBankIncome**](SandboxPublicTokenCreateRequestIncomeVerificationBankIncome.md) | [**SandboxPublicTokenCreateRequestIncomeVerificationBankIncome**](SandboxPublicTokenCreateRequestIncomeVerificationBankIncome.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# income_source_types

The types of source income data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The types of source income data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncomeVerificationSourceType**](IncomeVerificationSourceType.md) | [**IncomeVerificationSourceType**](IncomeVerificationSourceType.md) | [**IncomeVerificationSourceType**](IncomeVerificationSourceType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

