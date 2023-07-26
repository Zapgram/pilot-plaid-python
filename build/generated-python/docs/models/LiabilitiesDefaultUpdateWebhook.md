# plaid.model.liabilities_default_update_webhook.LiabilitiesDefaultUpdateWebhook

The webhook of type `LIABILITIES` and code `DEFAULT_UPDATE` will be fired when new or updated liabilities have been detected on a liabilities item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The webhook of type &#x60;LIABILITIES&#x60; and code &#x60;DEFAULT_UPDATE&#x60; will be fired when new or updated liabilities have been detected on a liabilities item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;LIABILITIES&#x60; | 
**item_id** | str,  | str,  | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**account_ids_with_updated_liabilities** | [**LiabilitiesAccountIdsWithUpdatedLiabilities**](LiabilitiesAccountIdsWithUpdatedLiabilities.md) | [**LiabilitiesAccountIdsWithUpdatedLiabilities**](LiabilitiesAccountIdsWithUpdatedLiabilities.md) |  | 
**webhook_code** | str,  | str,  | &#x60;DEFAULT_UPDATE&#x60; | 
**[account_ids_with_new_liabilities](#account_ids_with_new_liabilities)** | list, tuple,  | tuple,  | An array of &#x60;account_id&#x60;&#x27;s for accounts that contain new liabilities.&#x27; | 
**error** | [**PlaidError**](PlaidError.md) | [**PlaidError**](PlaidError.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_ids_with_new_liabilities

An array of `account_id`'s for accounts that contain new liabilities.'

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of &#x60;account_id&#x60;&#x27;s for accounts that contain new liabilities.&#x27; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

