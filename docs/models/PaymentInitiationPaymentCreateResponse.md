# plaid.model.payment_initiation_payment_create_response.PaymentInitiationPaymentCreateResponse

PaymentInitiationPaymentCreateResponse defines the response schema for `/payment_initiation/payment/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationPaymentCreateResponse defines the response schema for &#x60;/payment_initiation/payment/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payment_id** | str,  | str,  | A unique ID identifying the payment | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**status** | [**PaymentInitiationPaymentCreateStatus**](PaymentInitiationPaymentCreateStatus.md) | [**PaymentInitiationPaymentCreateStatus**](PaymentInitiationPaymentCreateStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

