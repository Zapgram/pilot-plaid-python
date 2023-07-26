# plaid.model.payment_initiation_metadata.PaymentInitiationMetadata

Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**supports_refund_details** | bool,  | BoolClass,  | Indicates whether the institution supports returning refund details when initiating a payment. | 
**maximum_payment_amount** | [**PaymentInitiationMaximumPaymentAmount**](PaymentInitiationMaximumPaymentAmount.md) | [**PaymentInitiationMaximumPaymentAmount**](PaymentInitiationMaximumPaymentAmount.md) |  | 
**standing_order_metadata** | [**PaymentInitiationStandingOrderMetadata**](PaymentInitiationStandingOrderMetadata.md) | [**PaymentInitiationStandingOrderMetadata**](PaymentInitiationStandingOrderMetadata.md) |  | 
**supports_sepa_instant** | bool,  | BoolClass,  | Indicates whether the institution supports SEPA Instant payments. | 
**supports_international_payments** | bool,  | BoolClass,  | Indicates whether the institution supports payments from a different country. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

