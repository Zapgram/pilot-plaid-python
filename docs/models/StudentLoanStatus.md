# plaid.model.student_loan_status.StudentLoanStatus

An object representing the status of the student loan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the status of the student loan | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end_date** | None, str, date,  | NoneClass, str,  | The date until which the loan will be in its current status. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  | value must conform to RFC-3339 full-date YYYY-MM-DD
**type** | None, str,  | NoneClass, str,  | The status type of the student loan | must be one of ["cancelled", "charged off", "claim", "consolidated", "deferment", "delinquent", "discharged", "extension", "forbearance", "in grace", "in military", "in school", "not fully disbursed", "other", "paid in full", "refunded", "repayment", "transferred", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

