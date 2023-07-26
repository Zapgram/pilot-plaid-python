# plaid.model.transfer_authorization.TransferAuthorization

Contains the authorization decision for a proposed transfer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains the authorization decision for a proposed transfer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**proposed_transfer** | [**TransferAuthorizationProposedTransfer**](TransferAuthorizationProposedTransfer.md) | [**TransferAuthorizationProposedTransfer**](TransferAuthorizationProposedTransfer.md) |  | 
**decision** | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) |  | 
**created** | str, datetime,  | str,  | The datetime representing when the authorization was created, in the format &#x60;2006-01-02T15:04:05Z&#x60;. | value must conform to RFC-3339 date-time
**guarantee_decision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guarantee_decision_rationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**decision_rationale** | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) |  | 
**id** | str,  | str,  | Plaid’s unique identifier for a transfer authorization. | 
**signal_insights** | [**SignalInsights**](SignalInsights.md) | [**SignalInsights**](SignalInsights.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

