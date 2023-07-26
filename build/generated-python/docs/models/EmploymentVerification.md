# plaid.model.employment_verification.EmploymentVerification

An object containing proof of employment data for an individual

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing proof of employment data for an individual | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | [**EmploymentVerificationStatus**](EmploymentVerificationStatus.md) | [**EmploymentVerificationStatus**](EmploymentVerificationStatus.md) |  | [optional] 
**start_date** | None, str, date,  | NoneClass, str,  | Start of employment in ISO 8601 format (YYYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**end_date** | None, str, date,  | NoneClass, str,  | End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD). | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**employer** | [**EmployerVerification**](EmployerVerification.md) | [**EmployerVerification**](EmployerVerification.md) |  | [optional] 
**title** | None, str,  | NoneClass, str,  | Current title of employee. | [optional] 
**platform_ids** | [**PlatformIds**](PlatformIds.md) | [**PlatformIds**](PlatformIds.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

