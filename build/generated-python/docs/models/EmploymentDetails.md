# plaid.model.employment_details.EmploymentDetails

An object representing employment details found on a paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing employment details found on a paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**annual_salary** | [**Pay**](Pay.md) | [**Pay**](Pay.md) |  | [optional] 
**hire_date** | None, str, date,  | NoneClass, str,  | Date on which the employee was hired, in the YYYY-MM-DD format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
