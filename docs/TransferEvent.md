# TransferEvent

Represents an event in the Transfers API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers. | 
**timestamp** | **datetime** | The datetime when this event occurred. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**event_type** | [**TransferEventType**](TransferEventType.md) |  | 
**account_id** | **str** | The account ID associated with the transfer. | 
**funding_account_id** | **str, none_type** | The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of your business checking accounts will be credited or debited. | 
**transfer_id** | **str** | Plaid’s unique identifier for a transfer. | 
**origination_account_id** | **str, none_type** | The ID of the origination account that this balance belongs to. | 
**transfer_type** | [**TransferType**](TransferType.md) |  | 
**transfer_amount** | **str** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**failure_reason** | [**TransferFailure**](TransferFailure.md) |  | 
**sweep_id** | **str, none_type** | Plaid’s unique identifier for a sweep. | 
**sweep_amount** | **str, none_type** | A signed amount of how much was &#x60;swept&#x60; or &#x60;return_swept&#x60; for this transfer (decimal string with two digits of precision e.g. \&quot;-5.50\&quot;). | 
**refund_id** | **str, none_type** | Plaid’s unique identifier for a refund. A non-null value indicates the event is for the associated refund of the transfer. | 
**originator_client_id** | **str, none_type** | The Plaid client ID that is the originator of the transfer that this event applies to. Only present if the transfer was created on behalf of another client as a third-party sender (TPS). | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


