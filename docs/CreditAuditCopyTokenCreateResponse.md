# CreditAuditCopyTokenCreateResponse

CreditAuditCopyTokenCreateResponse defines the response schema for `/credit/audit_copy_token/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_copy_token** | **str** | A token that can be shared with a third party auditor, which allows them to fetch the Asset Reports attached to the token. This token should be stored securely. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


