# LinkDeliveryCallbackWebhook

Webhook containing metadata proxied over from Link callback e.g `onEvent`, `onExit`, `onSuccess`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;LINK_DELIVERY&#x60; | 
**webhook_code** | **str** | &#x60;LINK_CALLBACK&#x60; | 
**link_delivery_session_id** | **str** | The ID of the Hosted Link session. | 
**timestamp** | **str** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**link_callback_metadata** | [**LinkCallbackMetadata**](LinkCallbackMetadata.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


