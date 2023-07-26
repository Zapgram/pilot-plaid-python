# plaid.model.link_token_create_request_employment.LinkTokenCreateRequestEmployment

Specifies options for initializing Link for use with the Employment product. This field is required if `employment` is included in the `products` array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies options for initializing Link for use with the Employment product. This field is required if &#x60;employment&#x60; is included in the &#x60;products&#x60; array. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[employment_source_types](#employment_source_types)** | list, tuple,  | tuple,  | The types of source employment data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | [optional] 
**bank_employment** | [**LinkTokenCreateRequestEmploymentBankIncome**](LinkTokenCreateRequestEmploymentBankIncome.md) | [**LinkTokenCreateRequestEmploymentBankIncome**](LinkTokenCreateRequestEmploymentBankIncome.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# employment_source_types

The types of source employment data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The types of source employment data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EmploymentSourceType**](EmploymentSourceType.md) | [**EmploymentSourceType**](EmploymentSourceType.md) | [**EmploymentSourceType**](EmploymentSourceType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

