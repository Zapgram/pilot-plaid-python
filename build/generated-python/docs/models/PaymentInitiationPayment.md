# plaid.model.payment_initiation_payment.PaymentInitiationPayment

PaymentInitiationPayment defines a payment initiation payment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationPayment defines a payment initiation payment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | A reference for the payment. | 
**bacs** | [**SenderBACSNullable**](SenderBACSNullable.md) | [**SenderBACSNullable**](SenderBACSNullable.md) |  | 
**amount** | [**PaymentAmount**](PaymentAmount.md) | [**PaymentAmount**](PaymentAmount.md) |  | 
**payment_id** | str,  | str,  | The ID of the payment. Like all Plaid identifiers, the &#x60;payment_id&#x60; is case sensitive. | 
**iban** | None, str,  | NoneClass, str,  | The International Bank Account Number (IBAN) for the sender, if specified in the &#x60;/payment_initiation/payment/create&#x60; call. | 
**last_status_update** | str, datetime,  | str,  | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | value must conform to RFC-3339 date-time
**recipient_id** | str,  | str,  | The ID of the recipient | 
**status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**adjusted_reference** | None, str,  | NoneClass, str,  | The value of the reference sent to the bank after adjustment to pass bank validation rules. | [optional] 
**schedule** | [**ExternalPaymentScheduleGet**](ExternalPaymentScheduleGet.md) | [**ExternalPaymentScheduleGet**](ExternalPaymentScheduleGet.md) |  | [optional] 
**refund_details** | [**ExternalPaymentRefundDetails**](ExternalPaymentRefundDetails.md) | [**ExternalPaymentRefundDetails**](ExternalPaymentRefundDetails.md) |  | [optional] 
**[refund_ids](#refund_ids)** | list, tuple, None,  | tuple, NoneClass,  | Refund IDs associated with the payment. | [optional] 
**amount_refunded** | [**PaymentAmountRefunded**](PaymentAmountRefunded.md) | [**PaymentAmountRefunded**](PaymentAmountRefunded.md) |  | [optional] 
**wallet_id** | None, str,  | NoneClass, str,  | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | [optional] 
**scheme** | [**PaymentScheme**](PaymentScheme.md) | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**adjusted_scheme** | [**PaymentScheme**](PaymentScheme.md) | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**consent_id** | None, str,  | NoneClass, str,  | The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent. | [optional] 
**transaction_id** | None, str,  | NoneClass, str,  | The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# refund_ids

Refund IDs associated with the payment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Refund IDs associated with the payment. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

