# plaid.model.student_repayment_plan.StudentRepaymentPlan

An object representing the repayment plan for the student loan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the repayment plan for the student loan | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | None, str,  | NoneClass, str,  | The description of the repayment plan as provided by the servicer. | 
**type** | None, str,  | NoneClass, str,  | The type of the repayment plan. | must be one of ["extended graduated", "extended standard", "graduated", "income-contingent repayment", "income-based repayment", "interest-only", "other", "pay as you earn", "revised pay as you earn", "standard", None, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

