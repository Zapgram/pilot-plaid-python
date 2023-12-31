# AutomaticallyVerifiedWebhook

Fired when an Item is verified via automated micro-deposits. We recommend communicating to your users when this event is received to notify them that their account is verified and ready for use.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;AUTH&#x60; | 
**webhook_code** | **str** | &#x60;AUTOMATICALLY_VERIFIED&#x60; | 
**account_id** | **str** | The &#x60;account_id&#x60; of the account associated with the webhook | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


