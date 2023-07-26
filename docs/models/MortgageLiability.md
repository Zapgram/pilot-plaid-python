# plaid.model.mortgage_liability.MortgageLiability

Contains details about a mortgage account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains details about a mortgage account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**origination_principal_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The original principal balance of the mortgage. | value must be a 64 bit float
**account_number** | str,  | str,  | The account number of the loan. | 
**next_monthly_payment** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the next payment. | value must be a 64 bit float
**loan_type_description** | None, str,  | NoneClass, str,  | Description of the type of loan, for example &#x60;conventional&#x60;, &#x60;fixed&#x60;, or &#x60;variable&#x60;. This field is provided directly from the loan servicer and does not have an enumerated set of possible values. | 
**escrow_balance** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Total amount held in escrow to pay taxes and insurance on behalf of the borrower. | value must be a 64 bit float
**has_pmi** | None, bool,  | NoneClass, BoolClass,  | Indicates whether the borrower has private mortgage insurance in effect. | 
**last_payment_date** | None, str, date,  | NoneClass, str,  | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**past_due_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Amount of loan (principal + interest) past due for payment. | value must be a 64 bit float
**maturity_date** | None, str, date,  | NoneClass, str,  | Original date on which mortgage is due in full. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**has_prepayment_penalty** | None, bool,  | NoneClass, BoolClass,  | Indicates whether the borrower will pay a penalty for early payoff of mortgage. | 
**current_late_fee** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The current outstanding amount charged for late payment. | value must be a 64 bit float
**last_payment_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the last payment. | value must be a 64 bit float
**property_address** | [**MortgagePropertyAddress**](MortgagePropertyAddress.md) | [**MortgagePropertyAddress**](MortgagePropertyAddress.md) |  | 
**account_id** | str,  | str,  | The ID of the account that this liability belongs to. | 
**origination_date** | None, str, date,  | NoneClass, str,  | The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**loan_term** | None, str,  | NoneClass, str,  | Full duration of mortgage as at origination (e.g. &#x60;10 year&#x60;). | 
**interest_rate** | [**MortgageInterestRate**](MortgageInterestRate.md) | [**MortgageInterestRate**](MortgageInterestRate.md) |  | 
**ytd_interest_paid** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The year to date (YTD) interest paid. | value must be a 64 bit float
**ytd_principal_paid** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The YTD principal paid. | value must be a 64 bit float
**next_payment_due_date** | None, str, date,  | NoneClass, str,  | The due date for the next payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

