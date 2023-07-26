# plaid.model.transactions_enrich_get_response.TransactionsEnrichGetResponse

TransactionsEnrichGetResponse defines the response schema for `/transactions/enrich`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TransactionsEnrichGetResponse defines the response schema for &#x60;/transactions/enrich&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[enriched_transactions](#enriched_transactions)** | list, tuple,  | tuple,  | A list of enriched transactions. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# enriched_transactions

A list of enriched transactions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of enriched transactions. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientProvidedEnrichedTransaction**](ClientProvidedEnrichedTransaction.md) | [**ClientProvidedEnrichedTransaction**](ClientProvidedEnrichedTransaction.md) | [**ClientProvidedEnrichedTransaction**](ClientProvidedEnrichedTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

