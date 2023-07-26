# plaid.model.transactions_enhance_get_response.TransactionsEnhanceGetResponse

TransactionsEnhanceGetResponse defines the response schema for `/beta/transactions/v1/enhance`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TransactionsEnhanceGetResponse defines the response schema for &#x60;/beta/transactions/v1/enhance&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[enhanced_transactions](#enhanced_transactions)** | list, tuple,  | tuple,  | An array of enhanced transactions. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# enhanced_transactions

An array of enhanced transactions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of enhanced transactions. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientProvidedEnhancedTransaction**](ClientProvidedEnhancedTransaction.md) | [**ClientProvidedEnhancedTransaction**](ClientProvidedEnhancedTransaction.md) | [**ClientProvidedEnhancedTransaction**](ClientProvidedEnhancedTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

