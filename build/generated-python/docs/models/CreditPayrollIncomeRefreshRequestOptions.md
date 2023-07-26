# plaid.model.credit_payroll_income_refresh_request_options.CreditPayrollIncomeRefreshRequestOptions

An optional object for `/credit/payroll_income/refresh` request options.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object for &#x60;/credit/payroll_income/refresh&#x60; request options. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[item_ids](#item_ids)** | list, tuple,  | tuple,  | An array of &#x60;item_id&#x60;s to be refreshed. Each &#x60;item_id&#x60; should uniquely identify a payroll income item. | [optional] 
**webhook** | str,  | str,  | The URL where Plaid will send the payroll income refresh webhook. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# item_ids

An array of `item_id`s to be refreshed. Each `item_id` should uniquely identify a payroll income item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of &#x60;item_id&#x60;s to be refreshed. Each &#x60;item_id&#x60; should uniquely identify a payroll income item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

