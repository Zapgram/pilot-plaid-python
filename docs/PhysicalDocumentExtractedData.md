# PhysicalDocumentExtractedData

Data extracted from a user-submitted document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_number** | **str, none_type** | Alpha-numeric ID number extracted via OCR from the user&#39;s document image. | 
**category** | [**PhysicalDocumentCategory**](PhysicalDocumentCategory.md) |  | 
**expiration_date** | **date, none_type** | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**issuing_country** | [**GenericCountryCode**](GenericCountryCode.md) |  | 
**issuing_region** | **str, none_type** | An ISO 3166-2 subdivision code. Related terms would be \&quot;state\&quot;, \&quot;province\&quot;, \&quot;prefecture\&quot;, \&quot;zone\&quot;, \&quot;subdivision\&quot;, etc. | 
**date_of_birth** | **date, none_type** | A date extracted from the document in the format YYYY-MM-DD (RFC 3339 Section 5.6). | 
**address** | [**IdentityVerificationDocumentAddressResponse**](IdentityVerificationDocumentAddressResponse.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


