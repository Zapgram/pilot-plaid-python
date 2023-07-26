# plaid.model.wallet_transaction_list_response.WalletTransactionListResponse

WalletTransactionListResponse defines the response schema for `/wallet/transaction/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | WalletTransactionListResponse defines the response schema for &#x60;/wallet/transaction/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[transactions](#transactions)** | list, tuple,  | tuple,  | An array of transactions of an e-wallet, associated with the given &#x60;wallet_id&#x60; | 
**request_id** | str,  | str,  | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**next_cursor** | str,  | str,  | Cursor used for fetching transactions created before the latest transaction provided in this response | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

An array of transactions of an e-wallet, associated with the given `wallet_id`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of transactions of an e-wallet, associated with the given &#x60;wallet_id&#x60; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WalletTransaction**](WalletTransaction.md) | [**WalletTransaction**](WalletTransaction.md) | [**WalletTransaction**](WalletTransaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

