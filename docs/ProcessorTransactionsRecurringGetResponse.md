# ProcessorTransactionsRecurringGetResponse

ProcessorTransactionsRecurringGetResponse defines the response schema for `/processor/transactions/recurring/get`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflow_streams** | [**[TransactionStream]**](TransactionStream.md) | An array of depository transaction streams. | 
**outflow_streams** | [**[TransactionStream]**](TransactionStream.md) | An array of expense transaction streams. | 
**updated_datetime** | **datetime** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the last time transaction streams for the given account were updated on | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


