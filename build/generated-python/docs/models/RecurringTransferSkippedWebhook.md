# plaid.model.recurring_transfer_skipped_webhook.RecurringTransferSkippedWebhook

Fired when Plaid is unable to originate a new ACH transaction of the recurring transfer on the planned date.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when Plaid is unable to originate a new ACH transaction of the recurring transfer on the planned date. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;TRANSFER&#x60; | 
**skipped_origination_date** | str, date,  | str,  | The planned date on which Plaid is unable to originate a new ACH transaction of the recurring transfer. This will be of the form YYYY-MM-DD. | value must conform to RFC-3339 full-date YYYY-MM-DD
**authorization_decision** | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) |  | 
**recurring_transfer_id** | str,  | str,  | Plaid’s unique identifier for a recurring transfer. | 
**webhook_code** | str,  | str,  | &#x60;RECURRING_TRANSFER_SKIPPED&#x60; | 
**authorization_decision_rationale_code** | [**TransferAuthorizationDecisionRationaleCode**](TransferAuthorizationDecisionRationaleCode.md) | [**TransferAuthorizationDecisionRationaleCode**](TransferAuthorizationDecisionRationaleCode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

