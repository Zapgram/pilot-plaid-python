# plaid.model.payment_initiation_payment_token_create_response.PaymentInitiationPaymentTokenCreateResponse

PaymentInitiationPaymentTokenCreateResponse defines the response schema for `/payment_initiation/payment/token/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationPaymentTokenCreateResponse defines the response schema for &#x60;/payment_initiation/payment/token/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**payment_token_expiration_time** | str, datetime,  | str,  | The date and time at which the token will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. A &#x60;payment_token&#x60; expires after 15 minutes. | value must conform to RFC-3339 date-time
**payment_token** | str,  | str,  | A &#x60;payment_token&#x60; that can be provided to Link initialization to enter the payment initiation flow | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
