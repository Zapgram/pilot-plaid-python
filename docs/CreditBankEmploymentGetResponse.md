# CreditBankEmploymentGetResponse

CreditBankEmploymentGetResponse defines the response schema for `/beta/credit/v1/bank_employment/get`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_employment_reports** | [**[CreditBankEmploymentReport]**](CreditBankEmploymentReport.md) | Bank Employment data. Each entry in the array will be a distinct bank employment report. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


