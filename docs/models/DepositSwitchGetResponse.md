# plaid.model.deposit_switch_get_response.DepositSwitchGetResponse

DepositSwitchGetResponse defines the response schema for `/deposit_switch/get`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DepositSwitchGetResponse defines the response schema for &#x60;/deposit_switch/get&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_allocated_remainder** | None, bool,  | NoneClass, BoolClass,  | When &#x60;true&#x60;, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When &#x60;false&#x60;, user’s direct deposit is allocated as a percent or amount. Always &#x60;null&#x60; if the deposit switch has not been completed. | 
**percent_allocated** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The percentage of direct deposit allocated to the target account. Always &#x60;null&#x60; if the target account is not allocated a percentage or if the deposit switch has not been completed or if &#x60;is_allocated_remainder&#x60; is true. | value must be a 64 bit float
**date_created** | str, date,  | str,  | [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was created.  | value must conform to RFC-3339 full-date YYYY-MM-DD
**target_account_id** | None, str,  | NoneClass, str,  | The ID of the bank account the direct deposit was switched to. | 
**account_has_multiple_allocations** | None, bool,  | NoneClass, BoolClass,  | When &#x60;true&#x60;, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always &#x60;null&#x60; if the deposit switch has not been completed. | 
**date_completed** | None, str, date,  | NoneClass, str,  | [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was completed. Always &#x60;null&#x60; if the deposit switch has not been completed.  | value must conform to RFC-3339 full-date YYYY-MM-DD
**state** | str,  | str,  | The state, or status, of the deposit switch.  - &#x60;initialized&#x60; – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  - &#x60;processing&#x60; – The deposit switch request has been submitted and is being processed.  - &#x60;completed&#x60; – The user&#x27;s employer has fulfilled the deposit switch request.  - &#x60;error&#x60; – There was an error processing the deposit switch request. | must be one of ["initialized", "processing", "completed", "error", ] 
**target_item_id** | None, str,  | NoneClass, str,  | The ID of the Item the direct deposit was switched to. | 
**amount_allocated** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The dollar amount of direct deposit allocated to the target account. Always &#x60;null&#x60; if the target account is not allocated an amount or if the deposit switch has not been completed. | value must be a 64 bit float
**deposit_switch_id** | str,  | str,  | The ID of the deposit switch. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**switch_method** | None, str,  | NoneClass, str,  | The method used to make the deposit switch.  - &#x60;instant&#x60; – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.  - &#x60;mail&#x60; – User requested that Plaid contact their employer by mail to make the direct deposit switch.  - &#x60;pdf&#x60; – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.&#x27; | [optional] must be one of ["instant", "mail", "pdf", None, ] 
**employer_name** | None, str,  | NoneClass, str,  | The name of the employer selected by the user. If the user did not select an employer, the value returned is &#x60;null&#x60;. | [optional] 
**employer_id** | None, str,  | NoneClass, str,  | The ID of the employer selected by the user. If the user did not select an employer, the value returned is &#x60;null&#x60;. | [optional] 
**institution_name** | None, str,  | NoneClass, str,  | The name of the institution selected by the user. If the user did not select an institution, the value returned is &#x60;null&#x60;. | [optional] 
**institution_id** | None, str,  | NoneClass, str,  | The ID of the institution selected by the user. If the user did not select an institution, the value returned is &#x60;null&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

