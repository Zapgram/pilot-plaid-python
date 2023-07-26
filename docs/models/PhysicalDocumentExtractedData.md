# plaid.model.physical_document_extracted_data.PhysicalDocumentExtractedData

Data extracted from a user-submitted document.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Data extracted from a user-submitted document. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id_number** | [**PhysicalDocumentIDNumber**](PhysicalDocumentIDNumber.md) | [**PhysicalDocumentIDNumber**](PhysicalDocumentIDNumber.md) |  | 
**address** | [**IdentityVerificationDocumentAddressResponse**](IdentityVerificationDocumentAddressResponse.md) | [**IdentityVerificationDocumentAddressResponse**](IdentityVerificationDocumentAddressResponse.md) |  | 
**issuing_region** | [**Region**](Region.md) | [**Region**](Region.md) |  | 
**issuing_country** | [**GenericCountryCode**](GenericCountryCode.md) | [**GenericCountryCode**](GenericCountryCode.md) |  | 
**date_of_birth** | [**IdentityVerificationDocumentISO8601DateOfBirth**](IdentityVerificationDocumentISO8601DateOfBirth.md) | [**IdentityVerificationDocumentISO8601DateOfBirth**](IdentityVerificationDocumentISO8601DateOfBirth.md) |  | 
**category** | [**PhysicalDocumentCategory**](PhysicalDocumentCategory.md) | [**PhysicalDocumentCategory**](PhysicalDocumentCategory.md) |  | 
**expiration_date** | [**ISO8601DateNullable**](ISO8601DateNullable.md) | [**ISO8601DateNullable**](ISO8601DateNullable.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

