# plaid.model.credit_bank_employment_get_response.CreditBankEmploymentGetResponse

CreditBankEmploymentGetResponse defines the response schema for `/beta/credit/v1/bank_employment/get`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreditBankEmploymentGetResponse defines the response schema for &#x60;/beta/credit/v1/bank_employment/get&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[bank_employment_reports](#bank_employment_reports)** | list, tuple,  | tuple,  | Bank Employment data. Each entry in the array will be a distinct bank employment report. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bank_employment_reports

Bank Employment data. Each entry in the array will be a distinct bank employment report.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Bank Employment data. Each entry in the array will be a distinct bank employment report. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreditBankEmploymentReport**](CreditBankEmploymentReport.md) | [**CreditBankEmploymentReport**](CreditBankEmploymentReport.md) | [**CreditBankEmploymentReport**](CreditBankEmploymentReport.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

