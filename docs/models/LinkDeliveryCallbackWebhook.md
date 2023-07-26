# plaid.model.link_delivery_callback_webhook.LinkDeliveryCallbackWebhook

Webhook containing metadata proxied over from Link callback e.g `onEvent`, `onExit`, `onSuccess`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Webhook containing metadata proxied over from Link callback e.g &#x60;onEvent&#x60;, &#x60;onExit&#x60;, &#x60;onSuccess&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**webhook_type** | str,  | str,  | &#x60;LINK_DELIVERY&#x60; | 
**link_callback_metadata** | [**LinkCallbackMetadata**](LinkCallbackMetadata.md) | [**LinkCallbackMetadata**](LinkCallbackMetadata.md) |  | 
**link_delivery_session_id** | str,  | str,  | The ID of the Hosted Link session. | 
**webhook_code** | str,  | str,  | &#x60;LINK_CALLBACK&#x60; | 
**timestamp** | str,  | str,  | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

