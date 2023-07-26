# IdentityVerificationDocumentAddressResponse

The address extracted from the document. The address must at least contain the following fields to be a valid address: `street`, `city`, `country`. If any are missing or unable to be extracted, the address will be null.  `region`, and `postal_code` may be null based on the addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code  Note: Optical Character Recognition (OCR) technology may sometimes extract incorrect data from a document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | The full street address extracted from the document. | 
**city** | **str** | City extracted from the document. | 
**region** | **str, none_type** | An ISO 3166-2 subdivision code extracted from the document. Related terms would be \&quot;state\&quot;, \&quot;province\&quot;, \&quot;prefecture\&quot;, \&quot;zone\&quot;, \&quot;subdivision\&quot;, etc. | 
**postal_code** | **str, none_type** | The postal code extracted from the document. Between 2 and 10 alphanumeric characters. For US-based addresses this must be 5 numeric digits. | 
**country** | [**IdentityVerificationDocumentCountryCode**](IdentityVerificationDocumentCountryCode.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


