# plaid.model.student_loan.StudentLoan

Contains details about a student loan account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains details about a student loan account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**origination_principal_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The original principal balance of the loan. | value must be a 64 bit float
**account_number** | None, str,  | NoneClass, str,  | The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number). | 
**loan_status** | [**StudentLoanStatus**](StudentLoanStatus.md) | [**StudentLoanStatus**](StudentLoanStatus.md) |  | 
**repayment_plan** | [**StudentRepaymentPlan**](StudentRepaymentPlan.md) | [**StudentRepaymentPlan**](StudentRepaymentPlan.md) |  | 
**payment_reference_number** | None, str,  | NoneClass, str,  | The relevant account number that should be used to reference this loan for payments. In the majority of cases, &#x60;payment_reference_number&#x60; will match &#x60;account_number,&#x60; but in some institutions, such as Great Lakes (&#x60;ins_116861&#x60;), it will be different. | 
**last_payment_date** | None, str, date,  | NoneClass, str,  | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**guarantor** | None, str,  | NoneClass, str,  | The guarantor of the student loan. | 
**is_overdue** | None, bool,  | NoneClass, BoolClass,  | &#x60;true&#x60; if a payment is currently overdue. Availability for this field is limited. | 
**last_statement_issue_date** | None, str, date,  | NoneClass, str,  | The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**last_payment_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the last payment. | value must be a 64 bit float
**expected_payoff_date** | None, str, date,  | NoneClass, str,  | The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**sequence_number** | None, str,  | NoneClass, str,  | The sequence number of the student loan. Heartland ECSI (&#x60;ins_116948&#x60;) does not make this field available. | 
**account_id** | None, str,  | NoneClass, str,  | The ID of the account that this liability belongs to. | 
**pslf_status** | [**PSLFStatus**](PSLFStatus.md) | [**PSLFStatus**](PSLFStatus.md) |  | 
**interest_rate_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | The interest rate on the loan as a percentage. | value must be a 64 bit float
**[disbursement_dates](#disbursement_dates)** | list, tuple, None,  | tuple, NoneClass,  | The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 
**origination_date** | None, str, date,  | NoneClass, str,  | The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  | value must conform to RFC-3339 full-date YYYY-MM-DD
**outstanding_interest_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The total dollar amount of the accrued interest balance. For Sallie Mae ( &#x60;ins_116944&#x60;), this amount is included in the current balance of the loan, so this field will return as &#x60;null&#x60;. | value must be a 64 bit float
**servicer_address** | [**ServicerAddressData**](ServicerAddressData.md) | [**ServicerAddressData**](ServicerAddressData.md) |  | 
**ytd_interest_paid** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The year to date (YTD) interest paid. Availability for this field is limited. | value must be a 64 bit float
**ytd_principal_paid** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The year to date (YTD) principal paid. Availability for this field is limited. | value must be a 64 bit float
**loan_name** | None, str,  | NoneClass, str,  | The type of loan, e.g., \&quot;Consolidation Loans\&quot;. | 
**minimum_payment_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The minimum payment due for the next billing cycle. There are some exceptions: Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( &#x60;ins_116861&#x60;), Firstmark (&#x60;ins_116295&#x60;), Commonbond Firstmark Services (&#x60;ins_116950&#x60;), Nelnet (&#x60;ins_116528&#x60;), EdFinancial Services (&#x60;ins_116304&#x60;), Granite State (&#x60;ins_116308&#x60;), and Oklahoma Student Loan Authority (&#x60;ins_116945&#x60;). Firstmark (&#x60;ins_116295&#x60; ) and Navient (&#x60;ins_116248&#x60;) will display as $0 if there is an autopay program in effect. | value must be a 64 bit float
**next_payment_due_date** | None, str, date,  | NoneClass, str,  | The due date for the next payment. The due date is &#x60;null&#x60; if a payment is not expected. A payment is not expected if &#x60;loan_status.type&#x60; is &#x60;deferment&#x60;, &#x60;in_school&#x60;, &#x60;consolidated&#x60;, &#x60;paid in full&#x60;, or &#x60;transferred&#x60;. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# disbursement_dates

The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

