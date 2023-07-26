# CreditBankStatementUploadBankAccount

An object containing data about a user's bank account related to an uploaded bank statement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The name of the bank account | 
**bank_name** | **str, none_type** | The name of the bank institution. | 
**account_type** | **str, none_type** | The type of the bank account. | 
**account_number** | **str, none_type** | The bank account number. | 
**owner** | [**CreditBankStatementUploadAccountOwner**](CreditBankStatementUploadAccountOwner.md) |  | 
**periods** | [**[CreditBankStatementUploadBankAccountPeriod]**](CreditBankStatementUploadBankAccountPeriod.md) | An array of period objects, containing more data on the overall period of the statement. | 
**account_id** | **str, none_type** | The unique id of the bank account | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


