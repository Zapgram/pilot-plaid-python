# plaid.model.user_permission_revoked_webhook.UserPermissionRevokedWebhook

The `USER_PERMISSION_REVOKED` webhook may be fired when an end user has used either the [my.plaid.com portal](https://my.plaid.com) or the financial institution’s OAuth consent portal to revoke the permission that they previously granted to access an Item. This webhook is not guaranteed to always be fired upon consent revocation, since some institutions’ consent portals do not trigger this webhook. Once access to an Item has been revoked, it cannot be restored. If the user subsequently returns to your application, a new Item must be created for the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The &#x60;USER_PERMISSION_REVOKED&#x60; webhook may be fired when an end user has used either the [my.plaid.com portal](https://my.plaid.com) or the financial institution’s OAuth consent portal to revoke the permission that they previously granted to access an Item. This webhook is not guaranteed to always be fired upon consent revocation, since some institutions’ consent portals do not trigger this webhook. Once access to an Item has been revoked, it cannot be restored. If the user subsequently returns to your application, a new Item must be created for the user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;ITEM&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhook_code** | str,  | str,  | &#x60;USER_PERMISSION_REVOKED&#x60; | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

