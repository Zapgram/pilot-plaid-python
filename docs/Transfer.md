# Transfer

Represents a transfer within the Transfers API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plaid’s unique identifier for a transfer. | 
**funding_account_id** | **str, none_type** | The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of your business checking accounts will be credited or debited. | 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**description** | **str** | The description of the transfer. | 
**created** | **datetime** | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**status** | [**TransferStatus**](TransferStatus.md) |  | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**cancellable** | **bool** | When &#x60;true&#x60;, you can still cancel this transfer. | 
**failure_reason** | [**TransferFailure**](TransferFailure.md) |  | 
**metadata** | [**TransferMetadata**](TransferMetadata.md) |  | 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**guarantee_decision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**guarantee_decision_rationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**iso_currency_code** | **str** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**standard_return_window** | **date, none_type** | The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD. | 
**unauthorized_return_window** | **date, none_type** | The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD. | 
**expected_settlement_date** | **date, none_type** | The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer&#39;s business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD. | 
**originator_client_id** | **str, none_type** | The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS). | 
**refunds** | [**[TransferRefund]**](TransferRefund.md) | A list of refunds associated with this transfer. | 
**recurring_transfer_id** | **str, none_type** | The id of the recurring transfer if this transfer belongs to a recurring transfer. | 
**credit_funds_source** | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) |  | 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | [optional] 
**sweep_status** | [**TransferSweepStatus**](TransferSweepStatus.md) |  | [optional] 
**expected_sweep_settlement_schedule** | [**[TransferExpectedSweepSettlementScheduleItem]**](TransferExpectedSweepSettlementScheduleItem.md) | The expected sweep settlement schedule of this transfer, assuming this transfer is not &#x60;returned&#x60;. Only applies to ACH debit transfers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


