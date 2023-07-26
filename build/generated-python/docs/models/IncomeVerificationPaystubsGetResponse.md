# plaid.model.income_verification_paystubs_get_response.IncomeVerificationPaystubsGetResponse

IncomeVerificationPaystubsGetResponse defines the response schema for `/income/verification/paystubs/get`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | IncomeVerificationPaystubsGetResponse defines the response schema for &#x60;/income/verification/paystubs/get&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[paystubs](#paystubs)** | list, tuple,  | tuple,  |  | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**[document_metadata](#document_metadata)** | list, tuple,  | tuple,  | Metadata for an income document. | [optional] 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# paystubs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Paystub**](Paystub.md) | [**Paystub**](Paystub.md) | [**Paystub**](Paystub.md) |  | 

# document_metadata

Metadata for an income document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Metadata for an income document. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DocumentMetadata**](DocumentMetadata.md) | [**DocumentMetadata**](DocumentMetadata.md) | [**DocumentMetadata**](DocumentMetadata.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

