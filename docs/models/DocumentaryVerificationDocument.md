# plaid.model.documentary_verification_document.DocumentaryVerificationDocument

Images, extracted data, and analysis from a user's identity document

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Images, extracted data, and analysis from a user&#x27;s identity document | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**extracted_data** | [**PhysicalDocumentExtractedData**](PhysicalDocumentExtractedData.md) | [**PhysicalDocumentExtractedData**](PhysicalDocumentExtractedData.md) |  | 
**images** | [**PhysicalDocumentImages**](PhysicalDocumentImages.md) | [**PhysicalDocumentImages**](PhysicalDocumentImages.md) |  | 
**redacted_at** | [**TimestampNullable**](TimestampNullable.md) | [**TimestampNullable**](TimestampNullable.md) |  | 
**analysis** | [**DocumentAnalysis**](DocumentAnalysis.md) | [**DocumentAnalysis**](DocumentAnalysis.md) |  | 
**attempt** | decimal.Decimal, int,  | decimal.Decimal,  | The &#x60;attempt&#x60; field begins with 1 and increments with each subsequent document upload. | 
**status** | [**DocumentStatus**](DocumentStatus.md) | [**DocumentStatus**](DocumentStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

