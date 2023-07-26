# plaid.model.physical_document_extracted_data_analysis.PhysicalDocumentExtractedDataAnalysis

Analysis of the data extracted from the submitted document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Analysis of the data extracted from the submitted document. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**issuing_country** | [**IssuingCountry**](IssuingCountry.md) | [**IssuingCountry**](IssuingCountry.md) |  | 
**date_of_birth** | [**DocumentDateOfBirthMatchCode**](DocumentDateOfBirthMatchCode.md) | [**DocumentDateOfBirthMatchCode**](DocumentDateOfBirthMatchCode.md) |  | 
**name** | [**DocumentNameMatchCode**](DocumentNameMatchCode.md) | [**DocumentNameMatchCode**](DocumentNameMatchCode.md) |  | 
**expiration_date** | [**ExpirationDate**](ExpirationDate.md) | [**ExpirationDate**](ExpirationDate.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

