# CreditBankStatementUploadObject

An object containing data that has been parsed from a user-uploaded bank statement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**[CreditBankStatementUploadTransaction]**](CreditBankStatementUploadTransaction.md) | An array of transactions appearing on the bank statement. | 
**document_metadata** | [**CreditDocumentMetadata**](CreditDocumentMetadata.md) |  | 
**document_id** | **str, none_type** | An identifier of the document referenced by the document metadata. | 
**bank_accounts** | [**[CreditBankStatementUploadBankAccount]**](CreditBankStatementUploadBankAccount.md) | An array of bank accounts associated with the uploaded bank statement. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


