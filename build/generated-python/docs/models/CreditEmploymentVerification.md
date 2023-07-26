# plaid.model.credit_employment_verification.CreditEmploymentVerification

The object containing proof of employment data for an individual.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The object containing proof of employment data for an individual. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end_date** | None, str, date,  | NoneClass, str,  | End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**employee_type** | [**CreditEmploymentEmployeeType**](CreditEmploymentEmployeeType.md) | [**CreditEmploymentEmployeeType**](CreditEmploymentEmployeeType.md) |  | 
**account_id** | None, str,  | NoneClass, str,  | ID of the payroll provider account. | 
**platform_ids** | [**CreditPlatformIds**](CreditPlatformIds.md) | [**CreditPlatformIds**](CreditPlatformIds.md) |  | 
**last_paystub_date** | None, str, date,  | NoneClass, str,  | The date of the employee&#x27;s most recent paystub in ISO 8601 format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**employer** | [**CreditEmployerVerification**](CreditEmployerVerification.md) | [**CreditEmployerVerification**](CreditEmployerVerification.md) |  | 
**title** | None, str,  | NoneClass, str,  | Current title of employee. | 
**start_date** | None, str, date,  | NoneClass, str,  | Start of employment in ISO 8601 format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**status** | [**CreditEmploymentVerificationStatus**](CreditEmploymentVerificationStatus.md) | [**CreditEmploymentVerificationStatus**](CreditEmploymentVerificationStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

