# plaid.model.item_login_repaired_webhook.ItemLoginRepairedWebhook

Fired when an Item login is repaired and the Item no longer needs to go through update mode. This will occur when the user completed the update mode flow for the Item, either in your application or in another Plaid-connected app. If you have messaging that tells the user to complete the update mode flow (such as in-app banners or out-of-band notifications) you should silence this messaging upon receiving the `LOGIN_REPAIRED` webhook.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Fired when an Item login is repaired and the Item no longer needs to go through update mode. This will occur when the user completed the update mode flow for the Item, either in your application or in another Plaid-connected app. If you have messaging that tells the user to complete the update mode flow (such as in-app banners or out-of-band notifications) you should silence this messaging upon receiving the &#x60;LOGIN_REPAIRED&#x60; webhook. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;ITEM&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhook_code** | str,  | str,  | &#x60;LOGIN_REPAIRED&#x60; | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

