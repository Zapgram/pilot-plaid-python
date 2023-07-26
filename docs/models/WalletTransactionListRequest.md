# plaid.model.wallet_transaction_list_request.WalletTransactionListRequest

WalletTransactionListRequest defines the request schema for `/wallet/transaction/list`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | WalletTransactionListRequest defines the request schema for &#x60;/wallet/transaction/list&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wallet_id** | str,  | str,  | The ID of the e-wallet to fetch transactions from | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**cursor** | str,  | str,  | A base64 value representing the latest transaction that has already been requested. Set this to &#x60;next_cursor&#x60; received from the previous &#x60;/wallet/transaction/list&#x60; request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the &#x60;created_at&#x60; time. | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transactions to fetch | [optional] if omitted the server will use the default value of 10
**options** | [**WalletTransactionListRequestOptions**](WalletTransactionListRequestOptions.md) | [**WalletTransactionListRequestOptions**](WalletTransactionListRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

