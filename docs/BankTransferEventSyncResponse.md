# BankTransferEventSyncResponse

Defines the response schema for `/bank_transfer/event/sync`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transfer_events** | [**[BankTransferEvent]**](BankTransferEvent.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


