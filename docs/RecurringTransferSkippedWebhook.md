# RecurringTransferSkippedWebhook

Fired when Plaid is unable to originate a new ACH transaction of the recurring transfer on the planned date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSFER&#x60; | 
**webhook_code** | **str** | &#x60;RECURRING_TRANSFER_SKIPPED&#x60; | 
**recurring_transfer_id** | **str** | Plaid’s unique identifier for a recurring transfer. | 
**authorization_decision** | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) |  | 
**skipped_origination_date** | **date** | The planned date on which Plaid is unable to originate a new ACH transaction of the recurring transfer. This will be of the form YYYY-MM-DD. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**authorization_decision_rationale_code** | [**TransferAuthorizationDecisionRationaleCode**](TransferAuthorizationDecisionRationaleCode.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


