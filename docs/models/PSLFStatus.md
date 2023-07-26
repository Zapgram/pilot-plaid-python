# plaid.model.pslf_status.PSLFStatus

Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (`ins_116527`). 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the student&#x27;s eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (&#x60;ins_116527&#x60;).  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payments_remaining** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of qualifying payments remaining. | 
**payments_made** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of qualifying payments that have been made. | 
**estimated_eligibility_date** | None, str, date,  | NoneClass, str,  | The estimated date borrower will have completed 120 qualifying monthly payments. Returned in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

