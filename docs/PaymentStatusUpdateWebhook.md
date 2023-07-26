# PaymentStatusUpdateWebhook

Fired when the status of a payment has changed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;PAYMENT_INITIATION&#x60; | 
**webhook_code** | **str** | &#x60;PAYMENT_STATUS_UPDATE&#x60; | 
**payment_id** | **str** | The &#x60;payment_id&#x60; for the payment being updated | 
**new_payment_status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**old_payment_status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**original_reference** | **str, none_type** | The original value of the reference when creating the payment. | 
**original_start_date** | **date, none_type** | The original value of the &#x60;start_date&#x60; provided during the creation of a standing order. If the payment is not a standing order, this field will be &#x60;null&#x60;. | 
**adjusted_start_date** | **date, none_type** | The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be &#x60;null&#x60;. | 
**timestamp** | **datetime** | The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. &#x60;\&quot;2017-09-14T14:42:19.350Z\&quot;&#x60; | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**transaction_id** | **str, none_type** | The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts. | [optional] 
**adjusted_reference** | **str, none_type** | The value of the reference sent to the bank after adjustment to pass bank validation rules. | [optional] 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


