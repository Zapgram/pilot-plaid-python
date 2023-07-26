# BankTransfersEventsUpdateWebhookForAuth

Fired when new ACH events are available. To begin receiving this webhook, you must first register your webhook listener endpoint via the [webhooks page in the Dashboard](https://dashboard.plaid.com/team/webhooks). The `BANK_TRANSFERS_EVENTS_UPDATE` webhook can be used to track the progress of ACH transfers used in [micro-deposit verification](/docs/auth/coverage/microdeposit-events/). Receiving this webhook indicates you should fetch the new events from `/bank_transfer/event/sync`. Note that [Transfer](https://plaid.com/docs/transfer) customers should use Transfer webhooks instead of using `BANK_TRANSFERS_EVENTS_UPDATE`; see [micro-deposit events documentation](https://plaid.com/docs/auth/coverage/microdeposit-events/) for more details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;BANK_TRANSFERS&#x60; | 
**webhook_code** | **str** | &#x60;BANK_TRANSFERS_EVENTS_UPDATE&#x60; | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


