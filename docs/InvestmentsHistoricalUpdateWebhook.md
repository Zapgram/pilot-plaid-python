# InvestmentsHistoricalUpdateWebhook

Fired after an asynchronous extraction on an investments account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;INVESTMENTS_TRANSACTIONS&#x60; | 
**webhook_code** | **str** | &#x60;HISTORICAL_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**new_investments_transactions** | **float** | The number of new transactions reported since the last time this webhook was fired. | 
**canceled_investments_transactions** | **float** | The number of canceled transactions reported since the last time this webhook was fired. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


