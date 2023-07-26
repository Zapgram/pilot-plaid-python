# ProductPermissionsRequiredIdentityWebhook

Fired when an `ACCESS_NOT_GRANTED` error is hit for Identity. The error can be resolved by putting the user through update mode with `identity` in the `products` array, as well as through the limited beta for update mode Identity product validations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;IDENTITY&#x60; | 
**webhook_code** | **str** | &#x60;PRODUCT_PERMISSIONS_REQUIRED&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


