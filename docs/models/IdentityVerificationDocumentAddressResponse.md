# plaid.model.identity_verification_document_address_response.IdentityVerificationDocumentAddressResponse

The address extracted from the document. The address must at least contain the following fields to be a valid address: `street`, `city`, `country`. If any are missing or unable to be extracted, the address will be null.  `region`, and `postal_code` may be null based on the addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code  Note: Optical Character Recognition (OCR) technology may sometimes extract incorrect data from a document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The address extracted from the document. The address must at least contain the following fields to be a valid address: &#x60;street&#x60;, &#x60;city&#x60;, &#x60;country&#x60;. If any are missing or unable to be extracted, the address will be null.  &#x60;region&#x60;, and &#x60;postal_code&#x60; may be null based on the addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code  Note: Optical Character Recognition (OCR) technology may sometimes extract incorrect data from a document. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | [**IdentityVerificationDocumentCountryCode**](IdentityVerificationDocumentCountryCode.md) | [**IdentityVerificationDocumentCountryCode**](IdentityVerificationDocumentCountryCode.md) |  | 
**city** | str,  | str,  | City extracted from the document. | 
**street** | str,  | str,  | The full street address extracted from the document. | 
**postal_code** | [**IdentityVerificationDocumentPostalCode**](IdentityVerificationDocumentPostalCode.md) | [**IdentityVerificationDocumentPostalCode**](IdentityVerificationDocumentPostalCode.md) |  | 
**region** | [**IdentityVerificationDocumentRegion**](IdentityVerificationDocumentRegion.md) | [**IdentityVerificationDocumentRegion**](IdentityVerificationDocumentRegion.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

