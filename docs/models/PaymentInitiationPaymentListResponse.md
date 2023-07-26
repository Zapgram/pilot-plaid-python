# plaid.model.payment_initiation_payment_list_response.PaymentInitiationPaymentListResponse

PaymentInitiationPaymentListResponse defines the response schema for `/payment_initiation/payment/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationPaymentListResponse defines the response schema for &#x60;/payment_initiation/payment/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next_cursor** | None, str, datetime,  | NoneClass, str,  | The value that, when used as the optional &#x60;cursor&#x60; parameter to &#x60;/payment_initiation/payment/list&#x60;, will return the next unreturned payment as its first payment. | value must conform to RFC-3339 date-time
**[payments](#payments)** | list, tuple,  | tuple,  | An array of payments that have been created, associated with the given &#x60;client_id&#x60;. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# payments

An array of payments that have been created, associated with the given `client_id`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of payments that have been created, associated with the given &#x60;client_id&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentInitiationPayment**](PaymentInitiationPayment.md) | [**PaymentInitiationPayment**](PaymentInitiationPayment.md) | [**PaymentInitiationPayment**](PaymentInitiationPayment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

