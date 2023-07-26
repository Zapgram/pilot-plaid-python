# plaid.model.payment_status_update_webhook.PaymentStatusUpdateWebhook

Fired when the status of a payment has changed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when the status of a payment has changed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**new_payment_status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**original_reference** | None, str,  | NoneClass, str,  | The original value of the reference when creating the payment. | 
**original_start_date** | None, str, date,  | NoneClass, str,  | The original value of the &#x60;start_date&#x60; provided during the creation of a standing order. If the payment is not a standing order, this field will be &#x60;null&#x60;. | value must conform to RFC-3339 full-date YYYY-MM-DD
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;PAYMENT_INITIATION&#x60; | 
**payment_id** | str,  | str,  | The &#x60;payment_id&#x60; for the payment being updated | 
**adjusted_start_date** | None, str, date,  | NoneClass, str,  | The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be &#x60;null&#x60;. | value must conform to RFC-3339 full-date YYYY-MM-DD
**webhook_code** | str,  | str,  | &#x60;PAYMENT_STATUS_UPDATE&#x60; | 
**old_payment_status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**timestamp** | str, datetime,  | str,  | The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. &#x60;\&quot;2017-09-14T14:42:19.350Z\&quot;&#x60; | value must conform to RFC-3339 date-time
**transaction_id** | None, str,  | NoneClass, str,  | The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts. | [optional] 
**adjusted_reference** | None, str,  | NoneClass, str,  | The value of the reference sent to the bank after adjustment to pass bank validation rules. | [optional] 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

