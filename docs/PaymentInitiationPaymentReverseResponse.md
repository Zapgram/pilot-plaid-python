# PaymentInitiationPaymentReverseResponse

PaymentInitiationPaymentReverseResponse defines the response schema for `/payment_initation/payment/reverse`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_id** | **str** | A unique ID identifying the refund | 
**status** | [**WalletTransactionStatus**](WalletTransactionStatus.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


