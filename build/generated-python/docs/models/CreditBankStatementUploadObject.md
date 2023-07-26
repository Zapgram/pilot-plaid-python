# plaid.model.credit_bank_statement_upload_object.CreditBankStatementUploadObject

An object containing data that has been parsed from a user-uploaded bank statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing data that has been parsed from a user-uploaded bank statement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[bank_accounts](#bank_accounts)** | list, tuple,  | tuple,  | An array of bank accounts associated with the uploaded bank statement. | 
**document_id** | None, str,  | NoneClass, str,  | An identifier of the document referenced by the document metadata. | 
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | 
**[transactions](#transactions)** | list, tuple,  | tuple,  | An array of transactions appearing on the bank statement. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

An array of transactions appearing on the bank statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of transactions appearing on the bank statement. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankStatementUploadTransaction**](CreditBankStatementUploadTransaction.md) | [**CreditBankStatementUploadTransaction**](CreditBankStatementUploadTransaction.md) | [**CreditBankStatementUploadTransaction**](CreditBankStatementUploadTransaction.md) |  | 

# bank_accounts

An array of bank accounts associated with the uploaded bank statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of bank accounts associated with the uploaded bank statement. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankStatementUploadBankAccount**](CreditBankStatementUploadBankAccount.md) | [**CreditBankStatementUploadBankAccount**](CreditBankStatementUploadBankAccount.md) | [**CreditBankStatementUploadBankAccount**](CreditBankStatementUploadBankAccount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

