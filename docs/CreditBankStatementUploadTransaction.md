# CreditBankStatementUploadTransaction

An object containing data about a transaction appearing on a user-uploaded bank statement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float, none_type** | The value of the transaction. A negative amount indicates that money moved into the account (such as a paycheck being deposited). | 
**date** | **date, none_type** | The date of when the transaction was made, in ISO 8601 format (YYYY-MM-DD). | 
**original_description** | **str, none_type** | The raw description of the transaction as it appears on the bank statement. | 
**account_id** | **str, none_type** | The unique id of the bank account that this transaction occurs in | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


