# InvestmentsTransactionsGetRequestOptions

An optional object to filter `/investments/transactions/get` results. If provided, must be non-`null`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | An array of &#x60;account_ids&#x60; to retrieve for the Item. | [optional] 
**count** | **int** | The number of transactions to fetch.  | [optional]  if omitted the server will use the default value of 100
**offset** | **int** | The number of transactions to skip when fetching transaction history | [optional]  if omitted the server will use the default value of 0
**async_update** | **bool** | If the Item was not initialized with the investments product via the &#x60;products&#x60; array when calling &#x60;/link/token/create&#x60;, and &#x60;async_update&#x60; is set to true, the initial Investments extraction will happen asynchronously. Plaid will subsequently fire a &#x60;HISTORICAL_UPDATE&#x60; webhook when the extraction completes. When &#x60;false&#x60;, Plaid will wait to return a response until extraction completion and no &#x60;HISTORICAL_UPDATE&#x60; webhook will fire. Note that while the extraction is happening asynchronously, calls to &#x60;/investments/transactions/get&#x60; and &#x60;/investments/refresh&#x60; will return &#x60;PRODUCT_NOT_READY&#x60; errors until the extraction completes. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


