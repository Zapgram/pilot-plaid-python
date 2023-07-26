# PaymentInitiationConsentCreateRequest

PaymentInitiationConsentCreateRequest defines the request schema for `/payment_initiation/consent/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | The ID of the recipient the payment consent is for. The created consent can be used to transfer funds to this recipient only. | 
**reference** | **str** | A reference for the payment consent. This must be an alphanumeric string with at most 18 characters and must not contain any special characters. | 
**scopes** | [**[PaymentInitiationConsentScope]**](PaymentInitiationConsentScope.md) | An array of payment consent scopes. | 
**constraints** | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**ExternalPaymentInitiationConsentOptions**](ExternalPaymentInitiationConsentOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


