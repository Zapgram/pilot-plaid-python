# LinkTokenCreateRequestEmployment

Specifies options for initializing Link for use with the Employment product. This field is required if `employment` is included in the `products` array.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employment_source_types** | [**[EmploymentSourceType]**](EmploymentSourceType.md) | The types of source employment data that users will be permitted to share. Options include &#x60;bank&#x60; and &#x60;payroll&#x60;. Currently you can only specify one of these options. | [optional] 
**bank_employment** | [**LinkTokenCreateRequestEmploymentBankIncome**](LinkTokenCreateRequestEmploymentBankIncome.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


