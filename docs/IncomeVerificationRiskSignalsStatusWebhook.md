# IncomeVerificationRiskSignalsStatusWebhook

Fired when a risk signal is available for documents uploaded via Document Income. It will typically take a minute or two for this webhook to fire after the end user has uploaded their documents in the Document Income flow. Once this webhook has fired, `/credit/payroll_income/risk_signals/get` may then be called to retrieve risk data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;\&quot;INCOME\&quot;&#x60; | 
**webhook_code** | **str** | &#x60;INCOME_VERIFICATION_RISK_SIGNALS&#x60; | 
**item_id** | **str** | The Item ID associated with the verification. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**user_id** | **str** | The Plaid &#x60;user_id&#x60; of the User associated with this webhook, warning, or error. | [optional] 
**risk_signals_status** | **str** | &#x60;RISK_SIGNALS_PROCESSING_COMPLETE&#x60;: The income verification fraud detection processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the &#x60;/credit/payroll_income/risk_signals/get&#x60; endpoint to get all risk signal data. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


