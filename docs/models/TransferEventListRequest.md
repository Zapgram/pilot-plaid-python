# plaid.model.transfer_event_list_request.TransferEventListRequest

Defines the request schema for `/transfer/event/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/transfer/event/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_date** | None, str, datetime,  | NoneClass, str,  | The start datetime of transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] value must conform to RFC-3339 date-time
**end_date** | None, str, datetime,  | NoneClass, str,  | The end datetime of transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] value must conform to RFC-3339 date-time
**transfer_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for a transfer. | [optional] 
**account_id** | None, str,  | NoneClass, str,  | The account ID to get events for all transactions to/from an account. | [optional] 
**transfer_type** | [**TransferEventListTransferType**](TransferEventListTransferType.md) | [**TransferEventListTransferType**](TransferEventListTransferType.md) |  | [optional] 
**[event_types](#event_types)** | list, tuple,  | tuple,  | Filter events by event type. | [optional] 
**sweep_id** | str,  | str,  | Plaid’s unique identifier for a sweep. | [optional] 
**count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum number of transfer events to return. If the number of events matching the above parameters is greater than &#x60;count&#x60;, the most recent events will be returned. | [optional] if omitted the server will use the default value of 25
**offset** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The offset into the list of transfer events. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;0, the first 25 events will be returned. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;25, the next 25 events will be returned. | [optional] if omitted the server will use the default value of 0
**origination_account_id** | None, str,  | NoneClass, str,  | The origination account ID to get events for transfers from a specific origination account. | [optional] 
**originator_client_id** | None, str,  | NoneClass, str,  | Filter transfer events to only those with the specified originator client. | [optional] 
**funding_account_id** | None, str,  | NoneClass, str,  | Filter transfer events to only those with the specified &#x60;funding_account_id&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# event_types

Filter events by event type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter events by event type. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransferEventType**](TransferEventType.md) | [**TransferEventType**](TransferEventType.md) | [**TransferEventType**](TransferEventType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

