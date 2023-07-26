# DocumentMetadata

An object representing metadata from the end user's uploaded document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the document. | [optional] 
**status** | **str, none_type** | The processing status of the document.  &#x60;PROCESSING_COMPLETE&#x60;: The document was successfully processed.  &#x60;DOCUMENT_ERROR&#x60;: The document could not be processed. Possible causes include: The document was an unacceptable document type such as an offer letter or bank statement, the document image was cropped or blurry, or the document was corrupted.  &#x60;UNKNOWN&#x60; or &#x60;null&#x60;: An internal error occurred. If this happens repeatedly, contact support or your Plaid account manager. | [optional] 
**doc_id** | **str** | An identifier of the document that is also present in the paystub response. | [optional] 
**doc_type** | [**DocType**](DocType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


