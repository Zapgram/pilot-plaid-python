# plaid.model.identity_verification_user_address.IdentityVerificationUserAddress

Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Even if an address has been collected, some fields may be null depending on the region&#x27;s addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | [**GenericCountryCode**](GenericCountryCode.md) | [**GenericCountryCode**](GenericCountryCode.md) |  | 
**city** | [**CityNullable**](CityNullable.md) | [**CityNullable**](CityNullable.md) |  | 
**street** | [**StreetNullable**](StreetNullable.md) | [**StreetNullable**](StreetNullable.md) |  | 
**street2** | [**Street2**](Street2.md) | [**Street2**](Street2.md) |  | 
**postal_code** | [**PostalCode**](PostalCode.md) | [**PostalCode**](PostalCode.md) |  | 
**region** | [**Region**](Region.md) | [**Region**](Region.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

