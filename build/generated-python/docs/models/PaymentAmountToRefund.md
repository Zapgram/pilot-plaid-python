# plaid.model.payment_amount_to_refund.PaymentAmountToRefund

The amount and currency of a payment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The amount and currency of a payment | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PaymentAmountNullable](PaymentAmountNullable.md) | [**PaymentAmountNullable**](PaymentAmountNullable.md) | [**PaymentAmountNullable**](PaymentAmountNullable.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | An amount to refund the payment partially. If this amount is not specified, the payment is refunded fully for the remaining amount. | 

# all_of_1

An amount to refund the payment partially. If this amount is not specified, the payment is refunded fully for the remaining amount.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An amount to refund the payment partially. If this amount is not specified, the payment is refunded fully for the remaining amount. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

