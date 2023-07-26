# WalletListResponse

WalletListResponse defines the response schema for `/wallet/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallets** | [**[Wallet]**](Wallet.md) | An array of e-wallets | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**next_cursor** | **str** | Cursor used for fetching e-wallets created before the latest e-wallet provided in this response | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


