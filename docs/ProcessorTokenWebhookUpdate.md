# ProcessorTokenWebhookUpdate

This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).  Fired when a processor updates the webhook URL for a processor token via `/processor/token/webhook/update`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;PROCESSOR_TOKEN&#x60; | 
**webhook_code** | **str** | &#x60;WEBHOOK_UPDATE_ACKNOWLEDGED&#x60; | 
**account_id** | **str** | The ID of the account. | 
**new_webhook_url** | **str** | The new webhook URL. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


