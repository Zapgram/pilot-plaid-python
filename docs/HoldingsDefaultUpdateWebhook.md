# HoldingsDefaultUpdateWebhook

Fired when new or updated holdings have been detected on an investment account. The webhook typically fires in response to any newly added holdings or price changes to existing holdings, most commonly after market close.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;HOLDINGS&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**new_holdings** | **float** | The number of new holdings reported since the last time this webhook was fired. | 
**updated_holdings** | **float** | The number of updated holdings reported since the last time this webhook was fired. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


