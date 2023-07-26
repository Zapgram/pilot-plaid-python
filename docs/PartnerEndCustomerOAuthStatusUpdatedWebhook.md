# PartnerEndCustomerOAuthStatusUpdatedWebhook

The webhook of type `PARTNER` and code `END_CUSTOMER_OAUTH_STATUS_UPDATED` will be fired when a partner's end customer has an update on their OAuth registration status with an institution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;PARTNER&#x60; | 
**webhook_code** | **str** | &#x60;END_CUSTOMER_OAUTH_STATUS_UPDATED&#x60; | 
**end_customer_client_id** | **str** | The client ID of the end customer | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**institution_id** | **str** | The institution ID | 
**institution_name** | **str** | The institution name | 
**status** | [**PartnerEndCustomerOAuthStatusUpdatedValues**](PartnerEndCustomerOAuthStatusUpdatedValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


