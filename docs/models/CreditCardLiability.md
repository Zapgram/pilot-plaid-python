# plaid.model.credit_card_liability.CreditCardLiability

An object representing a credit card account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing a credit card account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | None, str,  | NoneClass, str,  | The ID of the account that this liability belongs to. | 
**last_payment_date** | None, str, date,  | NoneClass, str,  | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). Availability for this field is limited. | value must conform to RFC-3339 full-date YYYY-MM-DD
**is_overdue** | None, bool,  | NoneClass, BoolClass,  | true if a payment is currently overdue. Availability for this field is limited. | 
**last_statement_issue_date** | None, str, date,  | NoneClass, str,  | The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**minimum_payment_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The minimum payment due for the next billing cycle. | value must be a 64 bit float
**[aprs](#aprs)** | list, tuple,  | tuple,  | The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty. | 
**last_payment_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The amount of the last payment. | value must be a 64 bit float
**next_payment_due_date** | None, str, date,  | NoneClass, str,  | The due date for the next payment. The due date is &#x60;null&#x60; if a payment is not expected. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | value must conform to RFC-3339 full-date YYYY-MM-DD
**last_statement_balance** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The total amount owed as of the last statement issued | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# aprs

The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**APR**](APR.md) | [**APR**](APR.md) | [**APR**](APR.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

