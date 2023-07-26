# plaid.model.credit_bank_statement_upload_bank_account.CreditBankStatementUploadBankAccount

An object containing data about a user's bank account related to an uploaded bank statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing data about a user&#x27;s bank account related to an uploaded bank statement. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**owner** | [**CreditBankStatementUploadAccountOwner**](CreditBankStatementUploadAccountOwner.md) | [**CreditBankStatementUploadAccountOwner**](CreditBankStatementUploadAccountOwner.md) |  | 
**account_number** | None, str,  | NoneClass, str,  | The bank account number. | 
**account_type** | None, str,  | NoneClass, str,  | The type of the bank account. | 
**account_id** | None, str,  | NoneClass, str,  | The unique id of the bank account | 
**bank_name** | None, str,  | NoneClass, str,  | The name of the bank institution. | 
**name** | None, str,  | NoneClass, str,  | The name of the bank account | 
**[periods](#periods)** | list, tuple,  | tuple,  | An array of period objects, containing more data on the overall period of the statement. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# periods

An array of period objects, containing more data on the overall period of the statement.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of period objects, containing more data on the overall period of the statement. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankStatementUploadBankAccountPeriod**](CreditBankStatementUploadBankAccountPeriod.md) | [**CreditBankStatementUploadBankAccountPeriod**](CreditBankStatementUploadBankAccountPeriod.md) | [**CreditBankStatementUploadBankAccountPeriod**](CreditBankStatementUploadBankAccountPeriod.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

