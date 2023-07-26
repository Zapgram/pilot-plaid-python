# BankIncomeRefreshCompleteWebhook

Fired when a refreshed bank income report has finished generating or failed to generate, triggered by calling `/credit/bank_income/refresh`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;INCOME&#x60; | 
**webhook_code** | **str** | &#x60;BANK_INCOME_REFRESH_COMPLETE&#x60; | 
**user_id** | **str** | The &#x60;user_id&#x60; corresponding to the user the webhook has fired for. | 
**result** | [**BankIncomeRefreshCompleteResult**](BankIncomeRefreshCompleteResult.md) |  | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


