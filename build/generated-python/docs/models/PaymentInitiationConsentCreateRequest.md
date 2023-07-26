# plaid.model.payment_initiation_consent_create_request.PaymentInitiationConsentCreateRequest

PaymentInitiationConsentCreateRequest defines the request schema for `/payment_initiation/consent/create`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationConsentCreateRequest defines the request schema for &#x60;/payment_initiation/consent/create&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not contain any special characters. | 
**[scopes](#scopes)** | list, tuple,  | tuple,  | An array of payment consent scopes. | 
**constraints** | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) |  | 
**recipient_id** | str,  | str,  | The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this recipient only. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**ExternalPaymentInitiationConsentOptions**](ExternalPaymentInitiationConsentOptions.md) | [**ExternalPaymentInitiationConsentOptions**](ExternalPaymentInitiationConsentOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scopes

An array of payment consent scopes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of payment consent scopes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentInitiationConsentScope**](PaymentInitiationConsentScope.md) | [**PaymentInitiationConsentScope**](PaymentInitiationConsentScope.md) | [**PaymentInitiationConsentScope**](PaymentInitiationConsentScope.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

