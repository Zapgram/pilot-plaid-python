# DocumentAnalysis

High level descriptions of how the associated document was processed. If a document fails verification, the details in the `analysis` object should help clarify why the document was rejected.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticity** | [**DocumentAuthenticityMatchCode**](DocumentAuthenticityMatchCode.md) |  | 
**image_quality** | [**ImageQuality**](ImageQuality.md) |  | 
**extracted_data** | [**PhysicalDocumentExtractedDataAnalysis**](PhysicalDocumentExtractedDataAnalysis.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


