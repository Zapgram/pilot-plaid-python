# plaid.model.transfer_diligence_document_upload_request.TransferDiligenceDocumentUploadRequest

Defines the request schema for `/transfer/diligence/document/upload`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/diligence/document/upload&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**originator_client_id** | str,  | str,  | The Client ID of the originator whose document that you want to upload. | 
**file** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | A file to upload. | 
**purpose** | [**TransferDocumentPurpose**](TransferDocumentPurpose.md) | [**TransferDocumentPurpose**](TransferDocumentPurpose.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

