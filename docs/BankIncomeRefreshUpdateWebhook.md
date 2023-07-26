# BankIncomeRefreshUpdateWebhook

Fired when a change to the user's income is detected. You should call `/credit/bank_income/refresh` to get updated income data for the user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;INCOME&#x60; | 
**webhook_code** | **str** | &#x60;BANK_INCOME_REFRESH_UPDATE&#x60; | 
**user_id** | **str** | The &#x60;user_id&#x60; corresponding to the user the webhook has fired for. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


