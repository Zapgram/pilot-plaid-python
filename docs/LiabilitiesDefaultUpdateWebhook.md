# LiabilitiesDefaultUpdateWebhook

The webhook of type `LIABILITIES` and code `DEFAULT_UPDATE` will be fired when new or updated liabilities have been detected on a liabilities item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;LIABILITIES&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**error** | [**PlaidError**](PlaidError.md) |  | 
**account_ids_with_new_liabilities** | **[str]** | An array of &#x60;account_id&#x60;&#39;s for accounts that contain new liabilities.&#39; | 
**account_ids_with_updated_liabilities** | [**LiabilitiesAccountIdsWithUpdatedLiabilities**](LiabilitiesAccountIdsWithUpdatedLiabilities.md) |  | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


