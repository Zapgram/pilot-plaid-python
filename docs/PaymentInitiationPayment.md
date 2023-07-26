# PaymentInitiationPayment

PaymentInitiationPayment defines a payment initiation payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The ID of the payment. Like all Plaid identifiers, the &#x60;payment_id&#x60; is case sensitive. | 
**amount** | [**PaymentAmount**](PaymentAmount.md) |  | 
**status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**recipient_id** | **str** | The ID of the recipient | 
**reference** | **str** | A reference for the payment. | 
**last_status_update** | **datetime** | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | 
**bacs** | [**SenderBACSNullable**](SenderBACSNullable.md) |  | 
**iban** | **str, none_type** | The International Bank Account Number (IBAN) for the sender, if specified in the &#x60;/payment_initiation/payment/create&#x60; call. | 
**adjusted_reference** | **str, none_type** | The value of the reference sent to the bank after adjustment to pass bank validation rules. | [optional] 
**schedule** | [**ExternalPaymentScheduleGet**](ExternalPaymentScheduleGet.md) |  | [optional] 
**refund_details** | [**ExternalPaymentRefundDetails**](ExternalPaymentRefundDetails.md) |  | [optional] 
**refund_ids** | **[str], none_type** | Refund IDs associated with the payment. | [optional] 
**amount_refunded** | [**PaymentAmountRefunded**](PaymentAmountRefunded.md) |  | [optional] 
**wallet_id** | **str, none_type** | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | [optional] 
**scheme** | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**adjusted_scheme** | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**consent_id** | **str, none_type** | The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent. | [optional] 
**transaction_id** | **str, none_type** | The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


