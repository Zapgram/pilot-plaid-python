# plaid.model.payment_initiation_consent.PaymentInitiationConsent

PaymentInitiationConsent defines a payment initiation consent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PaymentInitiationConsent defines a payment initiation consent. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  | A reference for the payment consent. | 
**created_at** | str, datetime,  | str,  | Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | value must conform to RFC-3339 date-time
**[scopes](#scopes)** | list, tuple,  | tuple,  | An array of payment consent scopes. | 
**constraints** | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) |  | 
**consent_id** | str,  | str,  | The consent ID. | 
**recipient_id** | str,  | str,  | The ID of the recipient the payment consent is for. | 
**status** | [**PaymentInitiationConsentStatus**](PaymentInitiationConsentStatus.md) | [**PaymentInitiationConsentStatus**](PaymentInitiationConsentStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

