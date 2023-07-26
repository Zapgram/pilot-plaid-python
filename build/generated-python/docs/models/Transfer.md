# plaid.model.transfer.Transfer

Represents a transfer within the Transfers API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents a transfer within the Transfers API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**metadata** | [**TransferMetadata**](TransferMetadata.md) | [**TransferMetadata**](TransferMetadata.md) |  | 
**credit_funds_source** | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) | [**TransferCreditFundsSource**](TransferCreditFundsSource.md) |  | 
**created** | str, datetime,  | str,  | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | value must conform to RFC-3339 date-time
**guarantee_decision** | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) | [**TransferAuthorizationGuaranteeDecision**](TransferAuthorizationGuaranteeDecision.md) |  | 
**description** | str,  | str,  | The description of the transfer. | 
**failure_reason** | [**TransferFailure**](TransferFailure.md) | [**TransferFailure**](TransferFailure.md) |  | 
**type** | [**TransferType**](TransferType.md) | [**TransferType**](TransferType.md) |  | 
**cancellable** | bool,  | BoolClass,  | When &#x60;true&#x60;, you can still cancel this transfer. | 
**expected_settlement_date** | None, str, date,  | NoneClass, str,  | The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer&#x27;s business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD. | value must conform to RFC-3339 full-date YYYY-MM-DD
**standard_return_window** | None, str, date,  | NoneClass, str,  | The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD. | value must conform to RFC-3339 full-date YYYY-MM-DD
**network** | [**TransferNetwork**](TransferNetwork.md) | [**TransferNetwork**](TransferNetwork.md) |  | 
**[refunds](#refunds)** | list, tuple,  | tuple,  | A list of refunds associated with this transfer. | 
**funding_account_id** | [**TransferFundingAccountIDResponseNullable**](TransferFundingAccountIDResponseNullable.md) | [**TransferFundingAccountIDResponseNullable**](TransferFundingAccountIDResponseNullable.md) |  | 
**originator_client_id** | None, str,  | NoneClass, str,  | The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS). | 
**guarantee_decision_rationale** | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) | [**TransferAuthorizationGuaranteeDecisionRationale**](TransferAuthorizationGuaranteeDecisionRationale.md) |  | 
**iso_currency_code** | str,  | str,  | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**origination_account_id** | str,  | str,  | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**recurring_transfer_id** | None, str,  | NoneClass, str,  | The id of the recurring transfer if this transfer belongs to a recurring transfer. | 
**unauthorized_return_window** | None, str, date,  | NoneClass, str,  | The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD. | value must conform to RFC-3339 full-date YYYY-MM-DD
**id** | str,  | str,  | Plaid’s unique identifier for a transfer. | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 
**status** | [**TransferStatus**](TransferStatus.md) | [**TransferStatus**](TransferStatus.md) |  | 
**ach_class** | [**ACHClass**](ACHClass.md) | [**ACHClass**](ACHClass.md) |  | [optional] 
**account_id** | str,  | str,  | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | [optional] 
**sweep_status** | [**TransferSweepStatus**](TransferSweepStatus.md) | [**TransferSweepStatus**](TransferSweepStatus.md) |  | [optional] 
**[expected_sweep_settlement_schedule](#expected_sweep_settlement_schedule)** | list, tuple,  | tuple,  | The expected sweep settlement schedule of this transfer, assuming this transfer is not &#x60;returned&#x60;. Only applies to ACH debit transfers. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# refunds

A list of refunds associated with this transfer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of refunds associated with this transfer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransferRefund**](TransferRefund.md) | [**TransferRefund**](TransferRefund.md) | [**TransferRefund**](TransferRefund.md) |  | 

# expected_sweep_settlement_schedule

The expected sweep settlement schedule of this transfer, assuming this transfer is not `returned`. Only applies to ACH debit transfers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The expected sweep settlement schedule of this transfer, assuming this transfer is not &#x60;returned&#x60;. Only applies to ACH debit transfers. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransferExpectedSweepSettlementScheduleItem**](TransferExpectedSweepSettlementScheduleItem.md) | [**TransferExpectedSweepSettlementScheduleItem**](TransferExpectedSweepSettlementScheduleItem.md) | [**TransferExpectedSweepSettlementScheduleItem**](TransferExpectedSweepSettlementScheduleItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

