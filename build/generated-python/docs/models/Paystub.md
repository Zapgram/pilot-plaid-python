# plaid.model.paystub.Paystub

An object representing data extracted from the end user's paystub.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing data extracted from the end user&#x27;s paystub. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**net_pay** | [**NetPay**](NetPay.md) | [**NetPay**](NetPay.md) |  | 
**earnings** | [**Earnings**](Earnings.md) | [**Earnings**](Earnings.md) |  | 
**pay_period_details** | [**PayPeriodDetails**](PayPeriodDetails.md) | [**PayPeriodDetails**](PayPeriodDetails.md) |  | 
**employer** | [**PaystubEmployer**](PaystubEmployer.md) | [**PaystubEmployer**](PaystubEmployer.md) |  | 
**deductions** | [**Deductions**](Deductions.md) | [**Deductions**](Deductions.md) |  | 
**employee** | [**Employee**](Employee.md) | [**Employee**](Employee.md) |  | 
**doc_id** | str,  | str,  | An identifier of the document referenced by the document metadata. | 
**employment_details** | [**EmploymentDetails**](EmploymentDetails.md) | [**EmploymentDetails**](EmploymentDetails.md) |  | [optional] 
**paystub_details** | [**PaystubDetails**](PaystubDetails.md) | [**PaystubDetails**](PaystubDetails.md) |  | [optional] 
**[income_breakdown](#income_breakdown)** | list, tuple,  | tuple,  |  | [optional] 
**ytd_earnings** | [**PaystubYTDDetails**](PaystubYTDDetails.md) | [**PaystubYTDDetails**](PaystubYTDDetails.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# income_breakdown

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IncomeBreakdown**](IncomeBreakdown.md) | [**IncomeBreakdown**](IncomeBreakdown.md) | [**IncomeBreakdown**](IncomeBreakdown.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

