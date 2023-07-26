# plaid.model.credit_bank_income_cause.CreditBankIncomeCause

An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An error object and associated &#x60;item_id&#x60; used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**error_message** | str,  | str,  | A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use. | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this warning. | 
**error_type** | [**CreditBankIncomeErrorType**](CreditBankIncomeErrorType.md) | [**CreditBankIncomeErrorType**](CreditBankIncomeErrorType.md) |  | 
**display_message** | str,  | str,  | A user-friendly representation of the error code. null if the error is not related to user action. This may change over time and is not safe for programmatic use. | 
**error_code** | str,  | str,  | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by &#x60;error_type&#x60;. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. Error fields will be &#x60;null&#x60; if no error has occurred. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

