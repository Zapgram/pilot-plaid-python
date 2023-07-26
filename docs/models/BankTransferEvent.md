# plaid.model.bank_transfer_event.BankTransferEvent

Represents an event in the Bank Transfers API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents an event in the Bank Transfers API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | str,  | str,  | The account ID associated with the bank transfer. | 
**event_id** | decimal.Decimal, int,  | decimal.Decimal,  | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers. | 
**event_type** | [**BankTransferEventType**](BankTransferEventType.md) | [**BankTransferEventType**](BankTransferEventType.md) |  | 
**bank_transfer_amount** | str,  | str,  | The bank transfer amount. | 
**bank_transfer_id** | str,  | str,  | Plaid’s unique identifier for a bank transfer. | 
**bank_transfer_type** | [**BankTransferType**](BankTransferType.md) | [**BankTransferType**](BankTransferType.md) |  | 
**origination_account_id** | None, str,  | NoneClass, str,  | The ID of the origination account that this balance belongs to. | 
**failure_reason** | [**BankTransferFailure**](BankTransferFailure.md) | [**BankTransferFailure**](BankTransferFailure.md) |  | 
**bank_transfer_iso_currency_code** | str,  | str,  | The currency of the bank transfer amount. | 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) | [**BankTransferDirection**](BankTransferDirection.md) |  | 
**timestamp** | str, datetime,  | str,  | The datetime when this event occurred. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

