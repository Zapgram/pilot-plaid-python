# EmploymentVerification

An object containing proof of employment data for an individual

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EmploymentVerificationStatus**](EmploymentVerificationStatus.md) |  | [optional] 
**start_date** | **date, none_type** | Start of employment in ISO 8601 format (YYYY-MM-DD). | [optional] 
**end_date** | **date, none_type** | End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD). | [optional] 
**employer** | [**EmployerVerification**](EmployerVerification.md) |  | [optional] 
**title** | **str, none_type** | Current title of employee. | [optional] 
**platform_ids** | [**PlatformIds**](PlatformIds.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


