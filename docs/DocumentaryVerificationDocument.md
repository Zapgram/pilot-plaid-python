# DocumentaryVerificationDocument

Images, extracted data, and analysis from a user's identity document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DocumentStatus**](DocumentStatus.md) |  | 
**attempt** | **int** | The &#x60;attempt&#x60; field begins with 1 and increments with each subsequent document upload. | 
**images** | [**PhysicalDocumentImages**](PhysicalDocumentImages.md) |  | 
**extracted_data** | [**PhysicalDocumentExtractedData**](PhysicalDocumentExtractedData.md) |  | 
**analysis** | [**DocumentAnalysis**](DocumentAnalysis.md) |  | 
**redacted_at** | **datetime, none_type** | An ISO8601 formatted timestamp. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


