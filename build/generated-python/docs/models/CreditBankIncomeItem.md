# plaid.model.credit_bank_income_item.CreditBankIncomeItem

The details and metadata for an end user's Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The details and metadata for an end user&#x27;s Item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[bank_income_accounts](#bank_income_accounts)** | list, tuple,  | tuple,  | The Item&#x27;s accounts that have Bank Income data. | [optional] 
**[bank_income_sources](#bank_income_sources)** | list, tuple,  | tuple,  | The income sources for this Item. Each entry in the array is a single income source. | [optional] 
**last_updated_time** | str, datetime,  | str,  | The time when this Item&#x27;s data was last retrieved from the financial institution. | [optional] value must conform to RFC-3339 date-time
**institution_id** | str,  | str,  | The unique identifier of the institution associated with the Item. | [optional] 
**institution_name** | str,  | str,  | The name of the institution associated with the Item. | [optional] 
**item_id** | str,  | str,  | The unique identifier for the Item. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bank_income_accounts

The Item's accounts that have Bank Income data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Item&#x27;s accounts that have Bank Income data. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeAccount**](CreditBankIncomeAccount.md) | [**CreditBankIncomeAccount**](CreditBankIncomeAccount.md) | [**CreditBankIncomeAccount**](CreditBankIncomeAccount.md) |  | 

# bank_income_sources

The income sources for this Item. Each entry in the array is a single income source.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The income sources for this Item. Each entry in the array is a single income source. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankIncomeSource**](CreditBankIncomeSource.md) | [**CreditBankIncomeSource**](CreditBankIncomeSource.md) | [**CreditBankIncomeSource**](CreditBankIncomeSource.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

