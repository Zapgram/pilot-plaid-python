# plaid.model.credit_document_metadata.CreditDocumentMetadata

Object representing metadata pertaining to the document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object representing metadata pertaining to the document. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**download_url** | None, str,  | NoneClass, str,  | Signed URL to retrieve the underlying file. This download URL can only be used once and expires after two minutes. To generate a new download URL, call &#x60;/credit/payroll_income/get&#x60; again. | 
**name** | str,  | str,  | The name of the document. | 
**document_type** | [**CreditDocumentType**](CreditDocumentType.md) | [**CreditDocumentType**](CreditDocumentType.md) |  | 
**status** | None, str,  | NoneClass, str,  | The processing status of the document.  &#x60;PROCESSING_COMPLETE&#x60;: The document was successfully processed.  &#x60;DOCUMENT_ERROR&#x60;: The document could not be processed. Possible causes include: The document was an unacceptable document type such as an offer letter or bank statement, the document image was cropped or blurry, or the document was corrupted.  &#x60;UNKNOWN&#x60; or &#x60;null&#x60;: An internal error occurred. If this happens repeatedly, contact support or your Plaid account manager. | 
**page_count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of pages of the uploaded document (if available). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

