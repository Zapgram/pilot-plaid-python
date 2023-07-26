# plaid.model.transactions_sync_request.TransactionsSyncRequest

TransactionsSyncRequest defines the request schema for `/transactions/sync`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TransactionsSyncRequest defines the request schema for &#x60;/transactions/sync&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The access token associated with the Item data is being requested for. | 
**client_id** | str,  | str,  | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | str,  | str,  | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**cursor** | str,  | str,  | The cursor value represents the last update requested. Providing it will cause the response to only return changes after this update. If omitted, the entire history of updates will be returned, starting with the first-added transactions on the Item. The cursor also accepts the special value of &#x60;\&quot;now\&quot;&#x60;, which can be used to fast-forward the cursor as part of migrating an existing Item from &#x60;/transactions/get&#x60; to &#x60;/transactions/sync&#x60;. For more information, see the [Transactions sync migration guide](https://plaid.com/docs/transactions/sync-migration/). Note that using the &#x60;\&quot;now&#x60; value is not supported for any use case other than migrating existing Items from &#x60;/transactions/get&#x60;.  The upper-bound length of this cursor is 256 characters of base64. | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transaction updates to fetch. | [optional] if omitted the server will use the default value of 100
**options** | [**TransactionsSyncRequestOptions**](TransactionsSyncRequestOptions.md) | [**TransactionsSyncRequestOptions**](TransactionsSyncRequestOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

