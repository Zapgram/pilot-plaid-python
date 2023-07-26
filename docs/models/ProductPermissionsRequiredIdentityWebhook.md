# plaid.model.product_permissions_required_identity_webhook.ProductPermissionsRequiredIdentityWebhook

Fired when an `ACCESS_NOT_GRANTED` error is hit for Identity. The error can be resolved by putting the user through update mode with `identity` in the `products` array, as well as through the limited beta for update mode Identity product validations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when an &#x60;ACCESS_NOT_GRANTED&#x60; error is hit for Identity. The error can be resolved by putting the user through update mode with &#x60;identity&#x60; in the &#x60;products&#x60; array, as well as through the limited beta for update mode Identity product validations. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;IDENTITY&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhook_code** | str,  | str,  | &#x60;PRODUCT_PERMISSIONS_REQUIRED&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

