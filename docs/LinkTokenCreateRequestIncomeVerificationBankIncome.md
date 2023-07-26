# LinkTokenCreateRequestIncomeVerificationBankIncome

Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_requested** | **int** | The number of days of data to request for the Bank Income product | 
**enable_multiple_items** | **bool, none_type** | Whether to enable multiple Items to be added in the Link session | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


