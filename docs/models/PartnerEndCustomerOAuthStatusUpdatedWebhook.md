# plaid.model.partner_end_customer_o_auth_status_updated_webhook.PartnerEndCustomerOAuthStatusUpdatedWebhook

The webhook of type `PARTNER` and code `END_CUSTOMER_OAUTH_STATUS_UPDATED` will be fired when a partner's end customer has an update on their OAuth registration status with an institution.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The webhook of type &#x60;PARTNER&#x60; and code &#x60;END_CUSTOMER_OAUTH_STATUS_UPDATED&#x60; will be fired when a partner&#x27;s end customer has an update on their OAuth registration status with an institution. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end_customer_client_id** | str,  | str,  | The client ID of the end customer | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**webhook_type** | str,  | str,  | &#x60;PARTNER&#x60; | 
**webhook_code** | str,  | str,  | &#x60;END_CUSTOMER_OAUTH_STATUS_UPDATED&#x60; | 
**institution_name** | str,  | str,  | The institution name | 
**institution_id** | str,  | str,  | The institution ID | 
**status** | [**PartnerEndCustomerOAuthStatusUpdatedValues**](PartnerEndCustomerOAuthStatusUpdatedValues.md) | [**PartnerEndCustomerOAuthStatusUpdatedValues**](PartnerEndCustomerOAuthStatusUpdatedValues.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

