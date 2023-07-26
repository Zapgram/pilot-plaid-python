# WalletListRequest

WalletListRequest defines the request schema for `/wallet/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**iso_currency_code** | [**WalletISOCurrencyCode**](WalletISOCurrencyCode.md) |  | [optional] 
**cursor** | **str** | A base64 value representing the latest e-wallet that has already been requested. Set this to &#x60;next_cursor&#x60; received from the previous &#x60;/wallet/list&#x60; request. If provided, the response will only contain e-wallets created before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in descending order. | [optional] 
**count** | **int** | The number of e-wallets to fetch | [optional]  if omitted the server will use the default value of 10
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


