# PaymentInitiationMetadata

Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_international_payments** | **bool** | Indicates whether the institution supports payments from a different country. | 
**supports_sepa_instant** | **bool** | Indicates whether the institution supports SEPA Instant payments. | 
**maximum_payment_amount** | [**PaymentInitiationMaximumPaymentAmount**](PaymentInitiationMaximumPaymentAmount.md) |  | 
**supports_refund_details** | **bool** | Indicates whether the institution supports returning refund details when initiating a payment. | 
**standing_order_metadata** | [**PaymentInitiationStandingOrderMetadata**](PaymentInitiationStandingOrderMetadata.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


