# plaid.model.student_loan_repayment_model.StudentLoanRepaymentModel

Student loan repayment information used to configure Sandbox test data for the Liabilities product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Student loan repayment information used to configure Sandbox test data for the Liabilities product | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**non_repayment_months** | decimal.Decimal, int, float,  | decimal.Decimal,  | Configures the number of months before repayment starts. | 
**repayment_months** | decimal.Decimal, int, float,  | decimal.Decimal,  | Configures the number of months of repayments before the loan is paid off. | 
**type** | str,  | str,  | The only currently supported value for this field is &#x60;standard&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

