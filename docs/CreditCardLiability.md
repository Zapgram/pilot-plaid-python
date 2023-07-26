# CreditCardLiability

An object representing a credit card account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | The ID of the account that this liability belongs to. | 
**aprs** | [**[APR]**](APR.md) | The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty. | 
**is_overdue** | **bool, none_type** | true if a payment is currently overdue. Availability for this field is limited. | 
**last_payment_amount** | **float, none_type** | The amount of the last payment. | 
**last_payment_date** | **date, none_type** | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). Availability for this field is limited. | 
**last_statement_issue_date** | **date, none_type** | The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 
**last_statement_balance** | **float, none_type** | The total amount owed as of the last statement issued | 
**minimum_payment_amount** | **float, none_type** | The minimum payment due for the next billing cycle. | 
**next_payment_due_date** | **date, none_type** | The due date for the next payment. The due date is &#x60;null&#x60; if a payment is not expected. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


