# plaid.model.physical_document_images.PhysicalDocumentImages

URLs for downloading original and cropped images for this document submission. The URLs are designed to only allow downloading, not hot linking, so the URL will only serve the document image for 60 seconds before expiring. The expiration time is 60 seconds after the `GET` request for the associated Identity Verification attempt. A new expiring URL is generated with each request, so you can always rerequest the Identity Verification attempt if one of your URLs expires.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | URLs for downloading original and cropped images for this document submission. The URLs are designed to only allow downloading, not hot linking, so the URL will only serve the document image for 60 seconds before expiring. The expiration time is 60 seconds after the &#x60;GET&#x60; request for the associated Identity Verification attempt. A new expiring URL is generated with each request, so you can always rerequest the Identity Verification attempt if one of your URLs expires. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**face** | [**DocumentImageFace**](DocumentImageFace.md) | [**DocumentImageFace**](DocumentImageFace.md) |  | 
**original_front** | [**DocumentImageFront**](DocumentImageFront.md) | [**DocumentImageFront**](DocumentImageFront.md) |  | 
**original_back** | [**DocumentImageBack**](DocumentImageBack.md) | [**DocumentImageBack**](DocumentImageBack.md) |  | 
**cropped_back** | [**DocumentImageCroppedBack**](DocumentImageCroppedBack.md) | [**DocumentImageCroppedBack**](DocumentImageCroppedBack.md) |  | 
**cropped_front** | [**DocumentImageCroppedFront**](DocumentImageCroppedFront.md) | [**DocumentImageCroppedFront**](DocumentImageCroppedFront.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

