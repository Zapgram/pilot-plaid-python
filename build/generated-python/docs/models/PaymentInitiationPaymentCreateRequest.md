# plaid.model.payment_initiation_payment_create_request.PaymentInitiationPaymentCreateRequest

PaymentInitiationPaymentCreateRequest defines the request schema for `/payment_initiation/payment/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationPaymentCreateRequest defines the request schema for &#x60;/payment_initiation/payment/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them). In order to track settlement via Payment Confirmation, each payment must have a unique reference. If the reference provided through the API is not unique, Plaid will adjust it. Both the originally provided and automatically adjusted references (if any) can be found in the &#x60;reference&#x60; and &#x60;adjusted_reference&#x60; fields, respectively. | 
**amount** | [**PaymentAmount**](PaymentAmount.md) | [**PaymentAmount**](PaymentAmount.md) |  | 
**recipient_id** | str,  | str,  | The ID of the recipient the payment is for. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**schedule** | [**ExternalPaymentScheduleRequest**](ExternalPaymentScheduleRequest.md) | [**ExternalPaymentScheduleRequest**](ExternalPaymentScheduleRequest.md) |  | [optional] 
**options** | [**ExternalPaymentOptions**](ExternalPaymentOptions.md) | [**ExternalPaymentOptions**](ExternalPaymentOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

