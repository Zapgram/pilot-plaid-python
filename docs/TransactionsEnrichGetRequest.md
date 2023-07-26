# TransactionsEnrichGetRequest

TransactionsEnrichGetRequest defines the request schema for `/transactions/enrich`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** | The account type for the requested transactions (either &#x60;depository&#x60; or &#x60;credit&#x60;). | 
**transactions** | [**[ClientProvidedTransaction]**](ClientProvidedTransaction.md) | An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**TransactionsEnrichRequestOptions**](TransactionsEnrichRequestOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


