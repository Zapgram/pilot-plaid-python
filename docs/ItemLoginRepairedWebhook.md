# ItemLoginRepairedWebhook

Fired when an Item login is repaired and the Item no longer needs to go through update mode. This will occur when the user completed the update mode flow for the Item, either in your application or in another Plaid-connected app. If you have messaging that tells the user to complete the update mode flow (such as in-app banners or out-of-band notifications) you should silence this messaging upon receiving the `LOGIN_REPAIRED` webhook.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;ITEM&#x60; | 
**webhook_code** | **str** | &#x60;LOGIN_REPAIRED&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


