# plaid.model.liability_override.LiabilityOverride

Used to configure Sandbox test data for the Liabilities product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Used to configure Sandbox test data for the Liabilities product | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**repayment_plan_description** | str,  | str,  | Override the &#x60;repayment_plan.description&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**loan_status** | [**StudentLoanStatus**](StudentLoanStatus.md) | [**StudentLoanStatus**](StudentLoanStatus.md) |  | 
**interest_capitalization_grace_period_months** | decimal.Decimal, int, float,  | decimal.Decimal,  | If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**cash_apr** | decimal.Decimal, int, float,  | decimal.Decimal,  | The cash APR percentage value. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | value must be a 64 bit float
**payment_reference_number** | str,  | str,  | Override the &#x60;payment_reference_number&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**balance_transfer_apr** | decimal.Decimal, int, float,  | decimal.Decimal,  | The balance transfer APR percentage value. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | value must be a 64 bit float
**repayment_plan_type** | str,  | str,  | Override the &#x60;repayment_plan.type&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. Possible values are: &#x60;\&quot;extended graduated\&quot;&#x60;, &#x60;\&quot;extended standard\&quot;&#x60;, &#x60;\&quot;graduated\&quot;&#x60;, &#x60;\&quot;income-contingent repayment\&quot;&#x60;, &#x60;\&quot;income-based repayment\&quot;&#x60;, &#x60;\&quot;interest only\&quot;&#x60;, &#x60;\&quot;other\&quot;&#x60;, &#x60;\&quot;pay as you earn\&quot;&#x60;, &#x60;\&quot;revised pay as you earn\&quot;&#x60;, or &#x60;\&quot;standard\&quot;&#x60;. | 
**repayment_model** | [**StudentLoanRepaymentModel**](StudentLoanRepaymentModel.md) | [**StudentLoanRepaymentModel**](StudentLoanRepaymentModel.md) |  | 
**guarantor** | str,  | str,  | Override the &#x60;guarantor&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**is_overdue** | bool,  | BoolClass,  | Override the &#x60;is_overdue&#x60; field | 
**type** | str,  | str,  | The type of the liability object, either &#x60;credit&#x60; or &#x60;student&#x60;. Mortgages are not currently supported in the custom Sandbox. | 
**nominal_apr** | decimal.Decimal, int, float,  | decimal.Decimal,  | The interest rate on the loan as a percentage. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | value must be a 64 bit float
**last_payment_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Override the &#x60;last_payment_amount&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | value must be a 64 bit float
**expected_payoff_date** | str, date,  | str,  | Override the &#x60;expected_payoff_date&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | value must conform to RFC-3339 full-date YYYY-MM-DD
**principal** | decimal.Decimal, int, float,  | decimal.Decimal,  | The original loan principal. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | value must be a 64 bit float
**sequence_number** | str,  | str,  | Override the &#x60;sequence_number&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**pslf_status** | [**PSLFStatus**](PSLFStatus.md) | [**PSLFStatus**](PSLFStatus.md) |  | 
**origination_date** | str, date,  | str,  | The date on which the loan was initially lent, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | value must conform to RFC-3339 full-date YYYY-MM-DD
**special_apr** | decimal.Decimal, int, float,  | decimal.Decimal,  | The special APR percentage value. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | value must be a 64 bit float
**is_federal** | bool,  | BoolClass,  | Override the &#x60;is_federal&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**servicer_address** | [**Address**](Address.md) | [**Address**](Address.md) |  | 
**loan_name** | str,  | str,  | Override the &#x60;loan_name&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**minimum_payment_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Override the &#x60;minimum_payment_amount&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60; or &#x60;student&#x60;. | value must be a 64 bit float
**purchase_apr** | decimal.Decimal, int, float,  | decimal.Decimal,  | The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

