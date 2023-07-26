# plaid.model.transactions_enrich_get_request.TransactionsEnrichGetRequest

TransactionsEnrichGetRequest defines the request schema for `/transactions/enrich`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TransactionsEnrichGetRequest defines the request schema for &#x60;/transactions/enrich&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_type** | str,  | str,  | The account type for the requested transactions (either &#x60;depository&#x60; or &#x60;credit&#x60;). | 
**[transactions](#transactions)** | list, tuple,  | tuple,  | An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**options** | [**TransactionsEnrichRequestOptions**](TransactionsEnrichRequestOptions.md) | [**TransactionsEnrichRequestOptions**](TransactionsEnrichRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientProvidedTransaction**](ClientProvidedTransaction.md) | [**ClientProvidedTransaction**](ClientProvidedTransaction.md) | [**ClientProvidedTransaction**](ClientProvidedTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

