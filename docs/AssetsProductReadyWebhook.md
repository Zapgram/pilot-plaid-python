# AssetsProductReadyWebhook

Fired when the Asset Report has been generated and `/asset_report/get` is ready to be called.  If you attempt to retrieve an Asset Report before this webhook has fired, you’ll receive a response with the HTTP status code 400 and a Plaid error code of `PRODUCT_NOT_READY`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;ASSETS&#x60; | 
**webhook_code** | **str** | &#x60;PRODUCT_READY&#x60; | 
**asset_report_id** | **str** | The &#x60;asset_report_id&#x60; corresponding to the Asset Report the webhook has fired for. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**report_type** | **str** | The report type, indicating whether the Asset Report is a &#x60;full&#x60; or &#x60;fast&#x60; report. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


