# plaid.model.transactions_enhance_get_request.TransactionsEnhanceGetRequest

TransactionsEnhanceGetRequest defines the request schema for `/transactions/enhance`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TransactionsEnhanceGetRequest defines the request schema for &#x60;/transactions/enhance&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_type** | str,  | str,  | The type of account for the requested transactions (&#x60;depository&#x60; or &#x60;credit&#x60;). | 
**[transactions](#transactions)** | list, tuple,  | tuple,  | An array of raw transactions to be enhanced. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

An array of raw transactions to be enhanced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of raw transactions to be enhanced. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientProvidedRawTransaction**](ClientProvidedRawTransaction.md) | [**ClientProvidedRawTransaction**](ClientProvidedRawTransaction.md) | [**ClientProvidedRawTransaction**](ClientProvidedRawTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

