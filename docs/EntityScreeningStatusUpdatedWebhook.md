# EntityScreeningStatusUpdatedWebhook

Fired when an entity screening status has changed, which can occur manually via the dashboard or during ongoing monitoring.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;ENTITY_SCREENING&#x60; | 
**webhook_code** | **str** | &#x60;STATUS_UPDATED&#x60; | 
**screening_id** | **str** | The ID of the associated screening. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


