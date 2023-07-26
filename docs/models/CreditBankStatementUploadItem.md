# plaid.model.credit_bank_statement_upload_item.CreditBankStatementUploadItem

An object containing information about the bank statement upload Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing information about the bank statement upload Item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | None, str, datetime,  | NoneClass, str,  | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the Item was updated. | value must conform to RFC-3339 date-time
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**[bank_statements](#bank_statements)** | list, tuple,  | tuple,  |  | 
**status** | [**PayrollItemStatus**](PayrollItemStatus.md) | [**PayrollItemStatus**](PayrollItemStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bank_statements

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankStatementUploadObject**](CreditBankStatementUploadObject.md) | [**CreditBankStatementUploadObject**](CreditBankStatementUploadObject.md) | [**CreditBankStatementUploadObject**](CreditBankStatementUploadObject.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

