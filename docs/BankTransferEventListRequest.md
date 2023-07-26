# BankTransferEventListRequest

Defines the request schema for `/bank_transfer/event/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**start_date** | **datetime, none_type** | The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**end_date** | **datetime, none_type** | The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**bank_transfer_id** | **str, none_type** | Plaid’s unique identifier for a bank transfer. | [optional] 
**account_id** | **str, none_type** | The account ID to get events for all transactions to/from an account. | [optional] 
**bank_transfer_type** | [**BankTransferEventListBankTransferType**](BankTransferEventListBankTransferType.md) |  | [optional] 
**event_types** | [**[BankTransferEventType]**](BankTransferEventType.md) | Filter events by event type. | [optional] 
**count** | **int, none_type** | The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than &#x60;count&#x60;, the most recent events will be returned. | [optional]  if omitted the server will use the default value of 25
**offset** | **int, none_type** | The offset into the list of bank transfer events. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;0, the first 25 events will be returned. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;25, the next 25 bank transfer events will be returned. | [optional]  if omitted the server will use the default value of 0
**origination_account_id** | **str, none_type** | The origination account ID to get events for transfers from a specific origination account. | [optional] 
**direction** | [**BankTransferEventListDirection**](BankTransferEventListDirection.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


