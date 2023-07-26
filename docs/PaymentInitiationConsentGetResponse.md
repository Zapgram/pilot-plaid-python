# PaymentInitiationConsentGetResponse

PaymentInitiationConsentGetResponse defines the response schema for `/payment_initation/consent/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **str** | The consent ID. | 
**status** | [**PaymentInitiationConsentStatus**](PaymentInitiationConsentStatus.md) |  | 
**created_at** | **datetime** | Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**recipient_id** | **str** | The ID of the recipient the payment consent is for. | 
**reference** | **str** | A reference for the payment consent. | 
**constraints** | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) |  | 
**scopes** | [**[PaymentInitiationConsentScope]**](PaymentInitiationConsentScope.md) | An array of payment consent scopes. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


