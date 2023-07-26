# TransferRecurringCreateResponse

Defines the response schema for `/transfer/recurring/create`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | [**TransferAuthorizationDecision**](TransferAuthorizationDecision.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**recurring_transfer** | [**RecurringTransferNullable**](RecurringTransferNullable.md) |  | [optional] 
**decision_rationale** | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


