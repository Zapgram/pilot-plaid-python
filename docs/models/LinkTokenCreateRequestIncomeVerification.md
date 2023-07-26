# plaid.model.link_token_create_request_income_verification.LinkTokenCreateRequestIncomeVerification

Specifies options for initializing Link for use with the Income product. This field is required if `income_verification` is included in the `products` array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with the Income product. This field is required if &#x60;income_verification&#x60; is included in the &#x60;products&#x60; array. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**income_verification_id** | str,  | str,  | The &#x60;income_verification_id&#x60; of the verification instance, as provided by &#x60;/income/verification/create&#x60;. | [optional] 
**asset_report_id** | str,  | str,  | The &#x60;asset_report_id&#x60; of an asset report associated with the user, as provided by &#x60;/asset_report/create&#x60;. Providing an &#x60;asset_report_id&#x60; is optional and can be used to verify the user through a streamlined flow. If provided, the bank linking flow will be skipped. | [optional] 
**precheck_id** | str,  | str,  | The ID of a precheck created with &#x60;/income/verification/precheck&#x60;. Will be used to improve conversion of the income verification flow by streamlining the Link interface presented to the end user. | [optional] 
**[access_tokens](#access_tokens)** | list, tuple,  | tuple,  | An array of access tokens corresponding to Items that a user has previously connected with. Data from these institutions will be cross-referenced with document data received during the Document Income flow to help verify that the uploaded documents are accurate. If the &#x60;transactions&#x60; product was not initialized for these Items during link, it will be initialized after this Link session.  This field should only be used with the &#x60;payroll&#x60; income source type. | [optional] 
**[income_source_types](#income_source_types)** | list, tuple,  | tuple,  | The types of source income data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | [optional] 
**bank_income** | [**LinkTokenCreateRequestIncomeVerificationBankIncome**](LinkTokenCreateRequestIncomeVerificationBankIncome.md) | [**LinkTokenCreateRequestIncomeVerificationBankIncome**](LinkTokenCreateRequestIncomeVerificationBankIncome.md) |  | [optional] 
**payroll_income** | [**LinkTokenCreateRequestIncomeVerificationPayrollIncome**](LinkTokenCreateRequestIncomeVerificationPayrollIncome.md) | [**LinkTokenCreateRequestIncomeVerificationPayrollIncome**](LinkTokenCreateRequestIncomeVerificationPayrollIncome.md) |  | [optional] 
**[stated_income_sources](#stated_income_sources)** | list, tuple,  | tuple,  | A list of user stated income sources | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# access_tokens

An array of access tokens corresponding to Items that a user has previously connected with. Data from these institutions will be cross-referenced with document data received during the Document Income flow to help verify that the uploaded documents are accurate. If the `transactions` product was not initialized for these Items during link, it will be initialized after this Link session.  This field should only be used with the `payroll` income source type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of access tokens corresponding to Items that a user has previously connected with. Data from these institutions will be cross-referenced with document data received during the Document Income flow to help verify that the uploaded documents are accurate. If the &#x60;transactions&#x60; product was not initialized for these Items during link, it will be initialized after this Link session.  This field should only be used with the &#x60;payroll&#x60; income source type. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The access token associated with the Item data is being requested for. | 

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

# stated_income_sources

A list of user stated income sources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of user stated income sources | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LinkTokenCreateRequestUserStatedIncomeSource**](LinkTokenCreateRequestUserStatedIncomeSource.md) | [**LinkTokenCreateRequestUserStatedIncomeSource**](LinkTokenCreateRequestUserStatedIncomeSource.md) | [**LinkTokenCreateRequestUserStatedIncomeSource**](LinkTokenCreateRequestUserStatedIncomeSource.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

