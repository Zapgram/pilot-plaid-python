# plaid.model.statements_download_response.StatementsDownloadResponse

StatementsDownloadResponse defines the response schema for `/statements/download`. The response will contain a `Plaid-Content-Hash` header containing a SHA 256 checksum of the statement. This can be used to verify that the file being sent by Plaid is the same file that was downloaded to your systems.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | StatementsDownloadResponse defines the response schema for &#x60;/statements/download&#x60;. The response will contain a &#x60;Plaid-Content-Hash&#x60; header containing a SHA 256 checksum of the statement. This can be used to verify that the file being sent by Plaid is the same file that was downloaded to your systems. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

