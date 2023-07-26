# plaid.model.transactions_sync_response.TransactionsSyncResponse

TransactionsSyncResponse defines the response schema for `/transactions/sync`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TransactionsSyncResponse defines the response schema for &#x60;/transactions/sync&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next_cursor** | str,  | str,  | Cursor used for fetching any future updates after the latest update provided in this response. The cursor obtained after all pages have been pulled (indicated by &#x60;has_more&#x60; being &#x60;false&#x60;) will be valid for at least 1 year. This cursor should be persisted for later calls. If transactions are not yet available, this will be an empty string. | 
**[removed](#removed)** | list, tuple,  | tuple,  | Transactions that have been removed from the Item since &#x60;cursor&#x60; ordered by ascending last modified time. | 
**[added](#added)** | list, tuple,  | tuple,  | Transactions that have been added to the Item since &#x60;cursor&#x60; ordered by ascending last modified time. | 
**[modified](#modified)** | list, tuple,  | tuple,  | Transactions that have been modified on the Item since &#x60;cursor&#x60; ordered by ascending last modified time. | 
**has_more** | bool,  | BoolClass,  | Represents if more than requested count of transaction updates exist. If true, the additional updates can be fetched by making an additional request with &#x60;cursor&#x60; set to &#x60;next_cursor&#x60;. If &#x60;has_more&#x60; is true, it’s important to pull all available pages, to make it less likely for underlying data changes to conflict with pagination. | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# added

Transactions that have been added to the Item since `cursor` ordered by ascending last modified time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transactions that have been added to the Item since &#x60;cursor&#x60; ordered by ascending last modified time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

# modified

Transactions that have been modified on the Item since `cursor` ordered by ascending last modified time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transactions that have been modified on the Item since &#x60;cursor&#x60; ordered by ascending last modified time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) | [**Transaction**](Transaction.md) |  | 

# removed

Transactions that have been removed from the Item since `cursor` ordered by ascending last modified time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transactions that have been removed from the Item since &#x60;cursor&#x60; ordered by ascending last modified time. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RemovedTransaction**](RemovedTransaction.md) | [**RemovedTransaction**](RemovedTransaction.md) | [**RemovedTransaction**](RemovedTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

