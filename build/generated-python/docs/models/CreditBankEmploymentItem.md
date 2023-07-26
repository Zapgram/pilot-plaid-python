# plaid.model.credit_bank_employment_item.CreditBankEmploymentItem

The details and metadata for an end user's Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details and metadata for an end user&#x27;s Item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**last_updated_time** | str, datetime,  | str,  | The time when this Item&#x27;s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \&quot;2018-04-12T03:32:11Z\&quot;). | value must conform to RFC-3339 date-time
**item_id** | str,  | str,  | The unique identifier for the Item. | 
**[bank_employments](#bank_employments)** | list, tuple,  | tuple,  | The bank employment information for this Item. Each entry in the array is a different employer found. | 
**[bank_employment_accounts](#bank_employment_accounts)** | list, tuple,  | tuple,  | The Item&#x27;s accounts that have Bank Employment data. | 
**institution_name** | str,  | str,  | The name of the institution associated with the Item. | 
**institution_id** | str,  | str,  | The unique identifier of the institution associated with the Item. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bank_employments

The bank employment information for this Item. Each entry in the array is a different employer found.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The bank employment information for this Item. Each entry in the array is a different employer found. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankEmployment**](CreditBankEmployment.md) | [**CreditBankEmployment**](CreditBankEmployment.md) | [**CreditBankEmployment**](CreditBankEmployment.md) |  | 

# bank_employment_accounts

The Item's accounts that have Bank Employment data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Item&#x27;s accounts that have Bank Employment data. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeAccount**](CreditBankIncomeAccount.md) | [**CreditBankIncomeAccount**](CreditBankIncomeAccount.md) | [**CreditBankIncomeAccount**](CreditBankIncomeAccount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

