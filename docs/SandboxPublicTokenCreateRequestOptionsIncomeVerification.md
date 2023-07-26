# SandboxPublicTokenCreateRequestOptionsIncomeVerification

A set of parameters for income verification options. This field is required if `income_verification` is included in the `initial_products` array.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**income_source_types** | [**[IncomeVerificationSourceType]**](IncomeVerificationSourceType.md) | The types of source income data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | [optional] 
**bank_income** | [**SandboxPublicTokenCreateRequestIncomeVerificationBankIncome**](SandboxPublicTokenCreateRequestIncomeVerificationBankIncome.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


