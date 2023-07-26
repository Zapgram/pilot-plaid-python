# WalletTransactionListResponse

WalletTransactionListResponse defines the response schema for `/wallet/transaction/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**[WalletTransaction]**](WalletTransaction.md) | An array of transactions of an e-wallet, associated with the given &#x60;wallet_id&#x60; | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**next_cursor** | **str** | Cursor used for fetching transactions created before the latest transaction provided in this response | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


