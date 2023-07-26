# TransferIntentGet

Represents a transfer intent within Transfer UI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid&#39;s unique identifier for a transfer intent object. | 
**created** | **datetime** | The datetime the transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**status** | [**TransferIntentStatus**](TransferIntentStatus.md) |  | 
**transfer_id** | **str, none_type** | Plaid&#39;s unique identifier for the transfer created through the UI. Returned only if the transfer was successfully created. Null value otherwise. | 
**failure_reason** | [**TransferIntentGetFailureReason**](TransferIntentGetFailureReason.md) |  | 
**authorization_decision** | [**TransferIntentAuthorizationDecision**](TransferIntentAuthorizationDecision.md) |  | 
**authorization_decision_rationale** | [**TransferAuthorizationDecisionRationale**](TransferAuthorizationDecisionRationale.md) |  | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account used for the transfer. | 
**funding_account_id** | **str** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**mode** | [**TransferIntentCreateMode**](TransferIntentCreateMode.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**description** | **str** | A description for the underlying transfer. Maximum of 8 characters. | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**guarantee_decision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guarantee_decision_rationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**account_id** | **str, none_type** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. Returned only if &#x60;account_id&#x60; was set on intent creation. | [optional] 
**network** | [**TransferIntentCreateNetwork**](TransferIntentCreateNetwork.md) |  | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | [optional] 
**require_guarantee** | **bool, none_type** | When &#x60;true&#x60;, the transfer requires a &#x60;GUARANTEED&#x60; decision by Plaid to proceed (Guarantee customers only). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


