# plaid.model.transfer_event.TransferEvent

Represents an event in the Transfers API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents an event in the Transfers API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sweep_id** | [**TransferSweepID**](TransferSweepID.md) | [**TransferSweepID**](TransferSweepID.md) |  | 
**sweep_amount** | [**TransferSweepAmount**](TransferSweepAmount.md) | [**TransferSweepAmount**](TransferSweepAmount.md) |  | 
**failure_reason** | [**TransferFailure**](TransferFailure.md) | [**TransferFailure**](TransferFailure.md) |  | 
**transfer_id** | str,  | str,  | Plaid’s unique identifier for a transfer. | 
**refund_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for a refund. A non-null value indicates the event is for the associated refund of the transfer. | 
**funding_account_id** | [**TransferFundingAccountIDResponseNullable**](TransferFundingAccountIDResponseNullable.md) | [**TransferFundingAccountIDResponseNullable**](TransferFundingAccountIDResponseNullable.md) |  | 
**originator_client_id** | None, str,  | NoneClass, str,  | The Plaid client ID that is the originator of the transfer that this event applies to. Only present if the transfer was created on behalf of another client as a third-party sender (TPS). | 
**account_id** | str,  | str,  | The account ID associated with the transfer. | 
**event_id** | decimal.Decimal, int,  | decimal.Decimal,  | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers. | 
**event_type** | [**TransferEventType**](TransferEventType.md) | [**TransferEventType**](TransferEventType.md) |  | 
**transfer_amount** | str,  | str,  | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**origination_account_id** | None, str,  | NoneClass, str,  | The ID of the origination account that this balance belongs to. | 
**transfer_type** | [**TransferType**](TransferType.md) | [**TransferType**](TransferType.md) |  | 
**timestamp** | str, datetime,  | str,  | The datetime when this event occurred. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

