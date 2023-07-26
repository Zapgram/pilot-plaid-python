# plaid.model.income_summary.IncomeSummary

The verified fields from a paystub verification. All fields are provided as reported on the paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The verified fields from a paystub verification. All fields are provided as reported on the paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**projected_wage** | [**ProjectedIncomeSummaryFieldNumber**](ProjectedIncomeSummaryFieldNumber.md) | [**ProjectedIncomeSummaryFieldNumber**](ProjectedIncomeSummaryFieldNumber.md) |  | 
**ytd_gross_income** | [**YTDGrossIncomeSummaryFieldNumber**](YTDGrossIncomeSummaryFieldNumber.md) | [**YTDGrossIncomeSummaryFieldNumber**](YTDGrossIncomeSummaryFieldNumber.md) |  | 
**ytd_net_income** | [**YTDNetIncomeSummaryFieldNumber**](YTDNetIncomeSummaryFieldNumber.md) | [**YTDNetIncomeSummaryFieldNumber**](YTDNetIncomeSummaryFieldNumber.md) |  | 
**employee_name** | [**EmployeeIncomeSummaryFieldString**](EmployeeIncomeSummaryFieldString.md) | [**EmployeeIncomeSummaryFieldString**](EmployeeIncomeSummaryFieldString.md) |  | 
**employer_name** | [**EmployerIncomeSummaryFieldString**](EmployerIncomeSummaryFieldString.md) | [**EmployerIncomeSummaryFieldString**](EmployerIncomeSummaryFieldString.md) |  | 
**pay_frequency** | [**PayFrequency**](PayFrequency.md) | [**PayFrequency**](PayFrequency.md) |  | 
**verified_transaction** | [**TransactionData**](TransactionData.md) | [**TransactionData**](TransactionData.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

