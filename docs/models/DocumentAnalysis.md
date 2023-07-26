# plaid.model.document_analysis.DocumentAnalysis

High level descriptions of how the associated document was processed. If a document fails verification, the details in the `analysis` object should help clarify why the document was rejected.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | High level descriptions of how the associated document was processed. If a document fails verification, the details in the &#x60;analysis&#x60; object should help clarify why the document was rejected. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**extracted_data** | [**PhysicalDocumentExtractedDataAnalysis**](PhysicalDocumentExtractedDataAnalysis.md) | [**PhysicalDocumentExtractedDataAnalysis**](PhysicalDocumentExtractedDataAnalysis.md) |  | 
**authenticity** | [**DocumentAuthenticityMatchCode**](DocumentAuthenticityMatchCode.md) | [**DocumentAuthenticityMatchCode**](DocumentAuthenticityMatchCode.md) |  | 
**image_quality** | [**ImageQuality**](ImageQuality.md) | [**ImageQuality**](ImageQuality.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

