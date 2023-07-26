# ProcessorDefaultUpdateWebhook

This webhook is only sent to [Plaid processor partners](https://plaid.com/docs/auth/partnerships/).  Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day.  This webhook is intended for use with `/processor/transactions/get`; if you are using the newer `/processor/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSACTIONS&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**new_transactions** | **float** | The number of new transactions detected since the last time this webhook was fired. | 
**account_id** | **str** | The ID of the account. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


