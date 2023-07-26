# plaid.model.investments_transactions_get_request_options.InvestmentsTransactionsGetRequestOptions

An optional object to filter `/investments/transactions/get` results. If provided, must be non-`null`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An optional object to filter &#x60;/investments/transactions/get&#x60; results. If provided, must be non-&#x60;null&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[account_ids](#account_ids)** | list, tuple,  | tuple,  | An array of &#x60;account_ids&#x60; to retrieve for the Item. | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transactions to fetch.  | [optional] if omitted the server will use the default value of 100
**offset** | decimal.Decimal, int,  | decimal.Decimal,  | The number of transactions to skip when fetching transaction history | [optional] if omitted the server will use the default value of 0
**async_update** | bool,  | BoolClass,  | If the Item was not initialized with the investments product via the &#x60;products&#x60; array when calling &#x60;/link/token/create&#x60;, and &#x60;async_update&#x60; is set to true, the initial Investments extraction will happen asynchronously. Plaid will subsequently fire a &#x60;HISTORICAL_UPDATE&#x60; webhook when the extraction completes. When &#x60;false&#x60;, Plaid will wait to return a response until extraction completion and no &#x60;HISTORICAL_UPDATE&#x60; webhook will fire. Note that while the extraction is happening asynchronously, calls to &#x60;/investments/transactions/get&#x60; and &#x60;/investments/refresh&#x60; will return &#x60;PRODUCT_NOT_READY&#x60; errors until the extraction completes. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account_ids

An array of `account_ids` to retrieve for the Item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of &#x60;account_ids&#x60; to retrieve for the Item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

