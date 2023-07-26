# TransferDiligenceDocumentUploadRequest

Defines the request schema for `/transfer/diligence/document/upload`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_client_id** | **str** | The Client ID of the originator whose document that you want to upload. | 
**file** | **file_type** | A file to upload. | 
**purpose** | [**TransferDocumentPurpose**](TransferDocumentPurpose.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


