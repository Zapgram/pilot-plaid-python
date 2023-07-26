# plaid.model.income_verification_risk_signals_status_webhook.IncomeVerificationRiskSignalsStatusWebhook

Fired when a risk signal is available for documents uploaded via Document Income. It will typically take a minute or two for this webhook to fire after the end user has uploaded their documents in the Document Income flow. Once this webhook has fired, `/credit/payroll_income/risk_signals/get` may then be called to retrieve risk data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when a risk signal is available for documents uploaded via Document Income. It will typically take a minute or two for this webhook to fire after the end user has uploaded their documents in the Document Income flow. Once this webhook has fired, &#x60;/credit/payroll_income/risk_signals/get&#x60; may then be called to retrieve risk data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;\&quot;INCOME\&quot;&#x60; | 
**item_id** | str,  | str,  | The Item ID associated with the verification. | 
**webhook_code** | str,  | str,  | &#x60;INCOME_VERIFICATION_RISK_SIGNALS&#x60; | 
**status** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**user_id** | str,  | str,  | The Plaid &#x60;user_id&#x60; of the User associated with this webhook, warning, or error. | [optional] 
**risk_signals_status** | str,  | str,  | &#x60;RISK_SIGNALS_PROCESSING_COMPLETE&#x60;: The income verification fraud detection processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the &#x60;/credit/payroll_income/risk_signals/get&#x60; endpoint to get all risk signal data. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

