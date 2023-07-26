# UserPermissionRevokedWebhook

The `USER_PERMISSION_REVOKED` webhook may be fired when an end user has used either the [my.plaid.com portal](https://my.plaid.com) or the financial institution’s OAuth consent portal to revoke the permission that they previously granted to access an Item. This webhook is not guaranteed to always be fired upon consent revocation, since some institutions’ consent portals do not trigger this webhook. Once access to an Item has been revoked, it cannot be restored. If the user subsequently returns to your application, a new Item must be created for the user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;ITEM&#x60; | 
**webhook_code** | **str** | &#x60;USER_PERMISSION_REVOKED&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


