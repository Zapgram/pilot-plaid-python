# IdentityDefaultUpdateWebhook

Fired when a change to identity data has been detected on an Item. Items are checked for identity updates every 30-90 days. We recommend that upon receiving this webhook you make another call to `/identity/get` to fetch the user's latest identity data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;IDENTITY&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**account_ids_with_updated_identity** | [**AccountIdsWithUpdatedIdentity**](AccountIdsWithUpdatedIdentity.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


