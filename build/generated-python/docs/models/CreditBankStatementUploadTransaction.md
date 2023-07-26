# plaid.model.credit_bank_statement_upload_transaction.CreditBankStatementUploadTransaction

An object containing data about a transaction appearing on a user-uploaded bank statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing data about a transaction appearing on a user-uploaded bank statement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | None, str, date,  | NoneClass, str,  | The date of when the transaction was made, in ISO 8601 format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The value of the transaction. A negative amount indicates that money moved into the account (such as a paycheck being deposited). | 
**account_id** | None, str,  | NoneClass, str,  | The unique id of the bank account that this transaction occurs in | 
**original_description** | None, str,  | NoneClass, str,  | The raw description of the transaction as it appears on the bank statement. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

