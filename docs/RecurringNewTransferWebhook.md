# RecurringNewTransferWebhook

Fired when a new transfer of a recurring transfer is originated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSFER&#x60; | 
**webhook_code** | **str** | &#x60;RECURRING_NEW_TRANSFER&#x60; | 
**recurring_transfer_id** | **str** | Plaid’s unique identifier for a recurring transfer. | 
**transfer_id** | **str** | Plaid’s unique identifier for a transfer. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


