# RecurringTransactionsUpdateWebhook

Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when a new transaction is added to an existing recurring stream. The `RECURRING_TRANSACTIONS_UPDATE` webhook will also fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update, or removal of transactions to the stream.  After receipt of this webhook, the updated data can be fetched from `/transactions/recurring/get`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSACTIONS&#x60; | 
**webhook_code** | **str** | &#x60;RECURRING_TRANSACTIONS_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**account_ids** | **[str]** | A list of &#x60;account_ids&#x60; for accounts that have new or updated recurring transactions data. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


