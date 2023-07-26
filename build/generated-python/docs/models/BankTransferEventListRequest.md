# plaid.model.bank_transfer_event_list_request.BankTransferEventListRequest

Defines the request schema for `/bank_transfer/event/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the request schema for &#x60;/bank_transfer/event/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_date** | None, str, datetime,  | NoneClass, str,  | The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] value must conform to RFC-3339 date-time
**end_date** | None, str, datetime,  | NoneClass, str,  | The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] value must conform to RFC-3339 date-time
**bank_transfer_id** | None, str,  | NoneClass, str,  | Plaid’s unique identifier for a bank transfer. | [optional] 
**account_id** | None, str,  | NoneClass, str,  | The account ID to get events for all transactions to/from an account. | [optional] 
**bank_transfer_type** | [**BankTransferEventListBankTransferType**](BankTransferEventListBankTransferType.md) | [**BankTransferEventListBankTransferType**](BankTransferEventListBankTransferType.md) |  | [optional] 
**[event_types](#event_types)** | list, tuple,  | tuple,  | Filter events by event type. | [optional] 
**count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than &#x60;count&#x60;, the most recent events will be returned. | [optional] if omitted the server will use the default value of 25
**offset** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The offset into the list of bank transfer events. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;0, the first 25 events will be returned. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;25, the next 25 bank transfer events will be returned. | [optional] if omitted the server will use the default value of 0
**origination_account_id** | None, str,  | NoneClass, str,  | The origination account ID to get events for transfers from a specific origination account. | [optional] 
**direction** | [**BankTransferEventListDirection**](BankTransferEventListDirection.md) | [**BankTransferEventListDirection**](BankTransferEventListDirection.md) |  | [optional] 
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
[**BankTransferEventType**](BankTransferEventType.md) | [**BankTransferEventType**](BankTransferEventType.md) | [**BankTransferEventType**](BankTransferEventType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

