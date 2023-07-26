# TransferEventsUpdateWebhook

Fired when new transfer events are available. Receiving this webhook indicates you should fetch the new events from `/transfer/event/sync`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSFER&#x60; | 
**webhook_code** | **str** | &#x60;TRANSFER_EVENTS_UPDATE&#x60; | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


