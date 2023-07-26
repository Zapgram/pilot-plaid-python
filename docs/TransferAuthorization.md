# TransferAuthorization

Contains the authorization decision for a proposed transfer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid’s unique identifier for a transfer authorization. | 
**created** | **datetime** | The datetime representing when the authorization was created, in the format &#x60;2006-01-02T15:04:05Z&#x60;. | 
**decision** | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) |  | 
**decision_rationale** | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) |  | 
**guarantee_decision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guarantee_decision_rationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**proposed_transfer** | [**TransferAuthorizationProposedTransfer**](TransferAuthorizationProposedTransfer.md) |  | 
**signal_insights** | [**SignalInsights**](SignalInsights.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


